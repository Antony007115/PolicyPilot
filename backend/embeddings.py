from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def create_embedding_model():
    """
    Load the sentence-transformer embedding model.
    """

    print(f"Loading embedding model: {MODEL_NAME}")

    model = SentenceTransformer(MODEL_NAME)

    print("Embedding model loaded successfully.")

    return model


def generate_embeddings(model, texts):
    """
    Convert a list of text chunks into embeddings.
    """

    if not texts:
        raise ValueError("Cannot generate embeddings for empty text.")

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings


if __name__ == "__main__":

    model = create_embedding_model()

    sample_texts = [
        "Employees may take up to 12 days of sick leave per calendar year.",
        "Full-time employees are entitled to 18 days of annual leave per year."
    ]

    embeddings = generate_embeddings(model, sample_texts)

    print("\nEmbedding generation successful.")
    print(f"Number of texts: {len(sample_texts)}")
    print(f"Embedding dimensions: {embeddings.shape[1]}")

    print("\nFirst embedding preview:")
    print(embeddings[0][:10])