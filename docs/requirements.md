# PolicyPilot — RAG Knowledge Assistant

## 1. Project Overview

PolicyPilot is a Retrieval-Augmented Generation (RAG) based
knowledge assistant designed to answer questions from a curated
collection of company-policy documents.

The system retrieves relevant information from the provided
documents and uses an LLM to generate grounded responses with
source citations.

## 2. Problem Statement

Employees often need to search lengthy company-policy documents
to find specific information.

Manually locating relevant information can be time-consuming and
may result in misunderstanding or incomplete answers.

PolicyPilot aims to provide a reliable conversational interface
that retrieves relevant policy information and generates answers
grounded in the approved document collection.

## 3. Target Users

- Employees
- HR personnel
- Managers
- Internal support teams

## 4. Stakeholder

Primary stakeholder:

Internal HR / employee-support team.

## 5. Inputs

The system accepts:

- Curated company-policy documents
- User questions

Supported document formats will initially include PDF and text
documents.

## 6. Outputs

The system will provide:

- Answer to the user's question
- Relevant source citation
- Confidence/relevance information where applicable
- Safe fallback response when information is unavailable

## 7. Core Features

1. Document ingestion
2. Text extraction
3. Text chunking
4. Embedding generation
5. Vector database storage
6. Semantic retrieval
7. LLM-based answer generation
8. Source citations
9. Structured output validation
10. Hallucination protection
11. Evaluation framework
12. API interface

## 8. Scope

### In Scope

- Company-policy documents
- Question answering
- Semantic search
- Retrieval-augmented generation
- Source citations
- Validation
- Evaluation
- Safety controls

### Out of Scope

- Making HR decisions
- Modifying company policies
- Accessing confidential employee records
- Taking autonomous organizational actions

## 9. Success Metrics

The project will be considered successful if:

- Relevant documents are retrieved for supported questions.
- Answers remain grounded in retrieved content.
- Responses contain appropriate source citations.
- The system refuses or safely responds when information is unavailable.
- Evaluation cases demonstrate acceptable retrieval and answer quality.
- The project can be reproduced using the submitted documentation.

## 10. Safety Requirements

The system must:

- Avoid inventing information not present in the documents.
- Clearly indicate when information cannot be found.
- Use only approved/curated documents.
- Handle invalid or ambiguous questions safely.
- Protect against prompt-injection attempts.
- Avoid exposing sensitive information.

## 11. Acceptance Criteria

- [ ] Documents can be ingested successfully.
- [ ] Documents are converted into searchable chunks.
- [ ] Embeddings are generated successfully.
- [ ] Vector database stores document representations.
- [ ] Relevant chunks are retrieved for user questions.
- [ ] LLM generates grounded answers.
- [ ] Answers include source citations.
- [ ] Unknown questions receive a safe fallback response.
- [ ] Structured output is validated.
- [ ] Evaluation test cases are completed.
- [ ] Known limitations are documented.
- [ ] README provides reproducible setup instructions.
- [ ] Final demonstration can explain the complete workflow.

## 12. Expected Deliverables

- Source code
- Requirements document
- Architecture documentation
- Evaluation dataset
- Test/validation evidence
- README
- Final presentation/demo
- GitHub repository
- Decision log
- Limitations and future improvements