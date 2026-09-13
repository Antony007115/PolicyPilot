from sentence_transformers import SentenceTransformer

from vector_store import create_vector_store


MODEL_NAME = "all-MiniLM-L6-v2"

# ChromaDB distance threshold
# Lower distance = more relevant
DISTANCE_THRESHOLD = 1.3


def retrieve_documents(query: str, top_k: int = 2):

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    # Load embedding model
    model = SentenceTransformer(MODEL_NAME)

    # Create query embedding
    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    # Get ChromaDB collection
    collection = create_vector_store()

    # Search for similar chunks
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    # Extract results
    documents = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    # Keep only relevant documents
    filtered_documents = []
    filtered_distances = []
    filtered_metadatas = []

    for document, distance, metadata in zip(
        documents,
        distances,
        metadatas
    ):

        if distance <= DISTANCE_THRESHOLD:

            filtered_documents.append(document)
            filtered_distances.append(distance)
            filtered_metadatas.append(metadata)

    # Return filtered results in the same structure
    return {
        "documents": [filtered_documents],
        "distances": [filtered_distances],
        "metadatas": [filtered_metadatas]
    }


if __name__ == "__main__":

    query = "What is the company salary structure?"

    print("=" * 60)
    print("QUERY")
    print("=" * 60)
    print(query)

    results = retrieve_documents(query)

    print("\n" + "=" * 60)
    print("RETRIEVED DOCUMENTS")
    print("=" * 60)

    documents = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        print("\nNo relevant policy information found.")

    for index, document in enumerate(documents):

        print(f"\nRESULT {index + 1}")
        print("-" * 60)

        print("Distance:", distances[index])
        print("Metadata:", metadatas[index])

        print("\nDocument:")
        print(document)