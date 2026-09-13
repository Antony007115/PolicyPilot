# PolicyPilot

**PolicyPilot** is a Retrieval-Augmented Generation (RAG) based enterprise policy question-answering system. It allows users to ask natural-language questions about approved company policy documents and receive evidence-grounded answers with document source information.

## Key Features

* Natural-language policy question answering
* Retrieval-Augmented Generation (RAG)
* Semantic document retrieval using sentence embeddings
* ChromaDB vector database
* Google Gemini for answer generation
* Source-aware responses with document metadata
* Relevance filtering to reduce unsupported answers
* Graceful handling of irrelevant questions
* FastAPI REST API
* Automated tests using pytest
* Health-check endpoint
* Retry and error handling for temporary AI-service failures

## System Workflow

```text
Policy Documents
       |
       v
Document Loading
       |
       v
Text Chunking
       |
       v
Sentence Embeddings
       |
       v
ChromaDB Vector Store
       |
       v
User Question
       |
       v
Query Embedding
       |
       v
Semantic Retrieval
       |
       v
Relevance Filtering
       |
       v
Gemini LLM
       |
       v
Answer + Source Metadata
```

## Project Structure

```text
PolicyPilot/
|
├── backend/
│   ├── api.py
│   ├── chunker.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── __init__.py
|
├── data/
│   ├── policies/
│   │   └── employee_leave_policy.txt
│   └── vector_db/
|
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   ├── limitations.md
│   └── requirements.md
|
├── evaluation/
├── tests/
│   └── test_policy_pilot.py
|
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Technology Stack

| Component              | Technology       |
| ---------------------- | ---------------- |
| Programming Language   | Python           |
| API Framework          | FastAPI          |
| LLM                    | Google Gemini    |
| Embedding Model        | all-MiniLM-L6-v2 |
| Vector Database        | ChromaDB         |
| PDF Processing         | pypdf            |
| Validation             | Pydantic         |
| Testing                | pytest           |
| Environment Management | python-dotenv    |
| Server                 | Uvicorn          |

## RAG Pipeline

PolicyPilot follows four major stages.

### 1. Document Processing

Approved policy documents are loaded from the `data/policies/` directory and divided into manageable text chunks.

### 2. Embedding and Storage

Each chunk is converted into a semantic vector using the `all-MiniLM-L6-v2` sentence-transformer model and stored in ChromaDB along with document metadata.

### 3. Retrieval

When a user asks a question, the question is converted into an embedding. ChromaDB performs semantic similarity search to retrieve relevant policy content.

A relevance threshold is applied so that unrelated questions do not automatically produce unsupported answers.

### 4. Answer Generation

The most relevant policy context is passed to Google Gemini. The generated response is returned together with the source document metadata.

## API Endpoints

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "service": "PolicyPilot API"
}
```

### Ask a Policy Question

```http
POST /ask
```

Request:

```json
{
  "question": "How many sick leave days are available?"
}
```

Example response:

```json
{
  "answer": "Employees may take up to 12 days of sick leave per calendar year.",
  "sources": [
    {
      "source": "employee_leave_policy.txt",
      "document_id": "HR-LEAVE-001",
      "chunk_id": 1,
      "version": "1.0"
    }
  ]
}
```

## Setup

### 1. Clone the project

```bash
git clone <repository-url>
cd PolicyPilot
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add the required Gemini API configuration.

Do not commit API keys or other secrets to Git.

### 5. Start the API

```powershell
cd backend
uvicorn api:app --reload
```

The interactive FastAPI documentation is available at:

```text
/docs
```

## Testing

Run the automated test suite from the project root:

```powershell
pytest -v
```

The current test suite covers:

* Sick leave retrieval
* Annual leave retrieval
* Annual leave notice-period retrieval
* Irrelevant-question rejection

Current result:

```text
4 passed
```

## Example Questions

The current demo policy can answer questions such as:

```text
How many sick leave days are available?

How many annual leave days do employees get?

How much notice is required for annual leave?
```

For unsupported questions such as:

```text
What is the company salary structure?
```

the system returns:

```text
I could not find this information in the provided policy.
```

This helps prevent unrelated information from being presented as a policy answer.

## Error Handling

PolicyPilot includes handling for:

* Empty questions
* Invalid requests
* No relevant policy information
* Temporary Gemini service unavailability
* Unexpected internal API errors

Temporary AI-service failures are returned as an HTTP `503` response instead of a generic application failure.

## Current Limitations

* The current demonstration uses a limited policy dataset.
* Retrieval quality depends on document quality and chunking.
* The system depends on an external LLM service for answer generation.
* The current implementation is an internship/project prototype rather than a production enterprise deployment.
* Authentication and authorization are not currently implemented.
* Advanced document-level access control is not currently implemented.

## Future Improvements

* Support multiple policy document formats
* Automatic document ingestion and indexing
* Document version management
* Role-based access control
* Improved evaluation datasets and retrieval metrics
* Conversation history
* Admin interface for policy management
* Production database and deployment
* Monitoring and observability
* Advanced hybrid retrieval

## Project Goal

PolicyPilot demonstrates how RAG can be used to build a reliable enterprise knowledge assistant that answers questions from approved internal documents while providing source information and avoiding unsupported answers.

## Status

**Core RAG pipeline:** Complete

**REST API:** Complete

**Source citation:** Complete

**Automated tests:** Complete

**Documentation:** Complete