from retriever import retrieve_documents
from llm import generate_answer


def answer_policy_question(question: str, top_k: int = 1) -> dict:
    """
    Complete RAG pipeline:
    1. Retrieve relevant policy chunks
    2. Build context from those chunks
    3. Generate an answer using Gemini
    4. Return answer with source information
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    # Step 1: Retrieve relevant policy chunks
    results = retrieve_documents(question, top_k=top_k)

    # Step 2: Extract retrieved documents and metadata
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return {
            "answer": "I could not find this information in the provided policy.",
            "sources": []
        }

    # Step 3: Combine retrieved chunks into context
    context = "\n\n".join(documents)

    # Step 4: Generate grounded answer using Gemini
    answer = generate_answer(
        question=question,
        context=context
    )

    # Step 5: Prepare source information
    sources = []

    for metadata in metadatas:
        if metadata:
            sources.append({
                "source": metadata.get("source"),
                "document_id": metadata.get("document_id"),
                "chunk_id": metadata.get("chunk_id"),
                "version": metadata.get("version")
            })

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":

    print("=" * 60)
    print("POLICYPILOT RAG PIPELINE TEST")
    print("=" * 60)

    question = "How many sick leave days can an employee take?"

    print("\nQuestion:")
    print(question)

    print("\nRetrieving policy information and generating answer...\n")

    result = answer_policy_question(question)

    print("Answer:")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print(source)

    print("\n" + "=" * 60)
    print("RAG PIPELINE TEST COMPLETED")
    print("=" * 60)