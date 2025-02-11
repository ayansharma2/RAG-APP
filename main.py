import logging
import os
import sys
import traceback
from datetime import timedelta

import streamlit as st

from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.exceptions import CouchbaseException
from couchbase.options import ClusterOptions

from langchain_core.embeddings.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_couchbase.vectorstores import CouchbaseVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers.string import StrOutputParser

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


def get_env_variable(var_name: str) -> str:
    """
    Retrieve a required environment variable. If it's missing, log an error,
    display an error on Streamlit, and exit the application.
    
    Args:
        var_name (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable.

    Exits:
        Exits the application if the environment variable is not set.
    """
    value = os.environ.get(var_name)
    if value is None:
        error_message = f"Required environment variable '{var_name}' is missing."
        logger.error(error_message)
        st.error(error_message)
        sys.exit(1)
    return value


def initialize_cluster(connection_string: str, username: str, password: str) -> Cluster:
    """
    Initialize and return a Couchbase cluster.

    Args:
        connection_string (str): The connection string for the Couchbase cluster.
        username (str): Couchbase username.
        password (str): Couchbase password.

    Returns:
        Cluster: An initialized Couchbase cluster instance.
    """
    auth = PasswordAuthenticator(username, password)
    options = ClusterOptions(auth)
    try:
        cluster = Cluster(connection_string, options)
        cluster.wait_until_ready(timedelta(seconds=5))
        logger.info("Successfully connected to Couchbase cluster.")
        return cluster
    except CouchbaseException as e:
        logger.error("Error connecting to Couchbase cluster: %s", e)
        raise


def build_rag_chain(cluster: Cluster,
                    bucket_name: str,
                    scope_name: str,
                    collection_name: str,
                    search_index_name: str) -> callable:
    """
    Build and return a Retrieval Augmented Generation (RAG) chain.

    The chain retrieves relevant content from Couchbase and uses GPT-4
    to generate the answer.

    Args:
        cluster (Cluster): An instance of the Couchbase cluster.
        bucket_name (str): Name of the target bucket.
        scope_name (str): Name of the target scope.
        collection_name (str): Name of the target collection.
        search_index_name (str): Name of the search index in Couchbase.

    Returns:
        callable: A function that accepts a question and returns the generated response.
    """
    # Initialize the embeddings using OpenAI's model.
    embeddings: Embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = CouchbaseVectorStore(
        cluster=cluster,
        bucket_name=bucket_name,
        scope_name=scope_name,
        collection_name=collection_name,
        embedding=embeddings,
        embedding_key="embedding",
        text_key="review",
        index_name=search_index_name
    )

    # Create a retriever from the vector store.
    retriever = vector_store.as_retriever()

    # Define the prompt template.
    template = (
        "You are a helpful bot. If you cannot answer based on the context provided, "
        "respond with a generic answer. Answer the question as truthfully as possible "
        "using the context below:\n\n{context}\n\nQuestion: {question}"
    )
    prompt = ChatPromptTemplate.from_template(template)

    # Initialize the GPT-4 model for generating responses.
    llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview", streaming=True)

    # Create the RAG chain by composing the retriever, prompt, LLM, and output parser.
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain.invoke


def main():
    """Main function for the Streamlit Hotel Recommendation System."""
    st.title("Hotel Recommendation System")
    st.write("Ask a question about hotels and get recommendations based on context.")

    # Check and read all required environment variables.
    couchbase_connection_string = get_env_variable("COUCHBASE_CONNECTION_STRING")
    db_username = get_env_variable("COUCHBASE_USERNAME")
    db_password = get_env_variable("COUCHBASE_PASSWORD")
    bucket_name = get_env_variable("COUCHBASE_BUCKET")
    scope_name = get_env_variable("COUCHBASE_SCOPE")
    collection_name = get_env_variable("COUCHBASE_COLLECTION")
    search_index_name = get_env_variable("COUCHBASE_SEARCH_INDEX")

    try:
        # Initialize the Couchbase cluster.
        cluster = initialize_cluster(couchbase_connection_string, db_username, db_password)
        # Build the RAG chain.
        rag_invoke = build_rag_chain(cluster, bucket_name, scope_name, collection_name, search_index_name)

        # Collect user input via Streamlit.
        question = st.text_input("Enter your question about hotels:")
        if question:
            with st.spinner("Processing your query..."):
                response = rag_invoke(question)
            st.write("Response:")
            st.write(response)
            logger.info("Query processed successfully.")

    except Exception as e:
        st.error("An error occurred while processing your request.")
        error_details = traceback.format_exc()
        st.error(error_details)
        logger.error("Exception occurred: %s", e, exc_info=True)


if __name__ == "__main__":
    main()