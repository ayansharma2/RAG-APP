# Hotel Recommendation System

This project is a hotel recommendation system that leverages Couchbase for vector storage, LangChain to build a Retrieval Augmented Generation (RAG) chain, and OpenAI's GPT-4 to generate responses. The user interacts with the system via a Streamlit-based web application.

## Directory Structure

The repository is organized as follows:

```
root/
├── requirements.txt
├── main.py
└── local.env
```

- **requirements.txt**: Contains all the Python package dependencies.
- **main.py**: The main script of the application.
- **local.env**: A file where you can store your environment variables (e.g., Couchbase credentials). This file should be kept secret and not committed to production repositories.

## Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Streamlit](https://streamlit.io/)

## Installation

1. **Clone the repository:**

   Open your terminal and run:

   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment (recommended):**

   On macOS and Linux:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. **Set Up Environment Variables:**

   The application reads required configuration values from environment variables. Open the `local.env` file and update the variables with your actual credentials. A sample `local.env` might look like:

   ```
   # Couchbase configuration
   COUCHBASE_CONNECTION_STRING=couchbases://your-couchbase-endpoint
   COUCHBASE_USERNAME=your_username
   COUCHBASE_PASSWORD=your_password
   COUCHBASE_BUCKET=travel-sample
   COUCHBASE_SCOPE=inventory
   COUCHBASE_COLLECTION=hotel
   COUCHBASE_SEARCH_INDEX=vector-index-1
   ```

2. **Load the Environment Variables:**

   Before starting the application, you need to load the environment variables from the `local.env` file. You can do this using a tool like [python-dotenv](https://pypi.org/project/python-dotenv/) or simply source the file in your shell.

   **Option 1: Using python-dotenv**

   - Install python-dotenv if necessary:Below is an example README.md file tailored to your directory structure, along with detailed instructions on how to run the application.

──────────────────────────────────────────────────────────────  
README.md  
──────────────────────────────────────────────────────────────

# Hotel Recommendation System

This project is a hotel recommendation system that leverages Couchbase for vector storage, LangChain to build a Retrieval Augmented Generation (RAG) chain, and OpenAI's GPT-4 to generate responses. The user interacts with the system via a Streamlit-based web application.

## Directory Structure

The repository is organized as follows:

```
root/
├── requirements.txt
├── main.py
└── local.env
```

- **requirements.txt**: Contains all the Python package dependencies.
- **main.py**: The main script of the application.
- **local.env**: A file where you can store your environment variables (e.g., Couchbase credentials). This file should be kept secret and not committed to production repositories.

## Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Streamlit](https://streamlit.io/)

## Installation

1. **Clone the repository:**

   Open your terminal and run:

   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment (recommended):**

   On macOS and Linux:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. **Set Up Environment Variables:**

   The application reads required configuration values from environment variables. Open the `local.env` file and update the variables with your actual credentials. A sample `local.env` might look like:

   ```
   # Couchbase configuration
   COUCHBASE_CONNECTION_STRING=couchbases://your-couchbase-endpoint
   COUCHBASE_USERNAME=your_username
   COUCHBASE_PASSWORD=your_password
   COUCHBASE_BUCKET=travel-sample
   COUCHBASE_SCOPE=inventory
   COUCHBASE_COLLECTION=hotel
   COUCHBASE_SEARCH_INDEX=vector-index-1
   ```

2. **Load the Environment Variables:**

   Before starting the application, you need to load the environment variables from the `local.env` file. You can do this using a tool like [python-dotenv](https://pypi.org/project/python-dotenv/) or simply source the file in your shell.

   **Option 1: Using python-dotenv**

   - Install python-dotenv if necessary:
     ```
     pip install python-dotenv
     ```
   - Modify your `main.py` (if not already done) to load the variables at startup:
     ```
     from dotenv import load_dotenv
     load_dotenv('local.env')
     ```

   **Option 2: Sourcing the file in your terminal (Linux/macOS):**

   ```
   source local.env
   ```

   For Windows Command Prompt, you might need to set each variable manually or use a tool that loads environment files.

## Running the Application

Once you have installed the dependencies and loaded your environment variables, you can run the application using Streamlit:

```
streamlit run main.py
```

After running the command above, Streamlit will start a local web server and provide you a URL (usually http://localhost:8501). Open the URL in your browser to interact with the Hotel Recommendation System.

## Troubleshooting

- **Missing Environment Variables**:  
  The application performs checks at startup. If any required environment variable is missing, an error message will display in the terminal and on the Streamlit interface. Ensure that your `local.env` file is properly configured and loaded.

- **Dependencies Issues**:  
  Make sure you have installed all packages by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License.

──────────────────────────────────────────────────────────────

This README provides a complete guide from installation to running the application, ensuring that users have all the information needed to get started with your hotel recommendation system.
`     pip install python-dotenv
    `

- Modify your `main.py` (if not already done) to load the variables at startup:
  ```
  from dotenv import load_dotenv
  load_dotenv('local.env')
  ```

**Option 2: Sourcing the file in your terminal (Linux/macOS):**

```
source local.env
```

For Windows Command Prompt, you might need to set each variable manually or use a tool that loads environment files.

## Running the Application

Once you have installed the dependencies and loaded your environment variables, you can run the application using Streamlit:

```
streamlit run main.py
```

After running the command above, Streamlit will start a local web server and provide you a URL (usually http://localhost:8501). Open the URL in your browser to interact with the Hotel Recommendation System.

## Troubleshooting

- **Missing Environment Variables**:  
  The application performs checks at startup. If any required environment variable is missing, an error message will display in the terminal and on the Streamlit interface. Ensure that your `local.env` file is properly configured and loaded.

- **Dependencies Issues**:  
  Make sure you have installed all packages by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License.

──────────────────────────────────────────────────────────────

This README provides a complete guide from installation to running the application, ensuring that users have all the information needed to get started with your hotel recommendation system.
