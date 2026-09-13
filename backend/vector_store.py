import chromadb
from pathlib import Path

from chunker import chunk_text
from document_loader import load_text_file
from embeddings import create_embedding_model, generate_embeddings


COLLECTION_NAME = "policy_documents"


def create_vector_store():
    """
    Create a persistent ChromaDB vector store.
    """

    project_root = Path(__file__).resolve().parent.parent

    db_path = project_root / "data" / "vector_db"

    client = chromadb.PersistentClient(
        path=str(db_path)
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection


def index_policy_document():

    project_root = Path(__file__).resolve().parent.parent

    document_path = (
        project_root
        / "data"
        / "policies"
        / "employee_leave_policy.txt"
    )

    # 1. Load document
    document_text = load_text_file(str(document_path))

    # 2. Create chunks
    chunks = chunk_text(document_text)

    print(f"Total chunks created: {len(chunks)}")

    # 3. Load embedding model
    model = create_embedding_model()

    # 4. Generate embeddings
    embeddings = generate_embeddings(
        model,
        chunks
    )

    # 5. Create vector store
    collection = create_vector_store()

    # 6. Store chunks + embeddings + metadata
    ids = []
    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(
            f"HR-LEAVE-001_chunk_{index + 1}"
        )

        metadatas.append(
            {
                "document_id": "HR-LEAVE-001",
                "version": "1.0",
                "source": "employee_leave_policy.txt",
                "chunk_id": index + 1
            }
        )

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print("\nPolicy successfully indexed!")
    print(f"Collection: {COLLECTION_NAME}")
    print(f"Documents stored: {collection.count()}")


if __name__ == "__main__":
    index_policy_document()