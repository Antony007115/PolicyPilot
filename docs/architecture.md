# PolicyPilot — System Architecture

## 1. Architecture Overview

PolicyPilot follows a Retrieval-Augmented Generation (RAG)
architecture.

The system retrieves relevant information from approved company
policy documents before generating an answer using an LLM.

## 2. High-Level Workflow

User Question
      ↓
FastAPI API
      ↓
Question Processing
      ↓
Embedding Generation
      ↓
Vector Database Search
      ↓
Relevant Document Chunks
      ↓
Prompt Construction
      ↓
LLM
      ↓
Structured Output Validation
      ↓
Safety / Hallucination Check
      ↓
Answer + Source Citation

## 3. Document Ingestion Workflow

Policy Documents
      ↓
Document Loader
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Database

## 4. Main Components

### Document Loader

Loads approved policy documents from the data directory.

### Text Processor

Extracts and cleans textual content from documents.

### Chunking Module

Splits large documents into smaller meaningful sections for
retrieval.

### Embedding Module

Converts document chunks and user questions into vector
representations.

### Vector Database

Stores document embeddings and retrieves semantically relevant
chunks.

### Retriever

Finds the most relevant document chunks for a user question.

### LLM Generator

Generates an answer using only the retrieved context.

### Output Validator

Checks whether the generated response follows the expected
structured format.

### Safety Layer

Reduces hallucinations and handles questions that cannot be
answered from the approved documents.

### FastAPI Backend

Provides API endpoints for the application.

## 5. Data Flow

Documents are processed during ingestion and stored as vector
representations.

When a user asks a question, the question is converted into an
embedding and compared with stored document embeddings.

The most relevant chunks are retrieved and provided to the LLM
as grounded context.

The generated response is validated before being returned to
the user.

## 6. Security and Responsible Use

The system will use only approved/public/simulated documents.

The system will not access real company systems or confidential
employee records.

Prompt-injection and unsupported questions will be handled using
safety controls.

## 7. Reproducibility

The project will maintain:

- Version-controlled source code
- Requirements documentation
- Configuration documentation
- Evaluation cases
- Test evidence
- README instructions
- Decision log