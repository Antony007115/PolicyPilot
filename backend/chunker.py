from document_loader import load_text_file
from pathlib import Path
import re


def chunk_text(text: str, max_chars: int = 700):
    """
    Split a document into meaningful chunks while trying to preserve
    paragraphs and sentences.
    """

    if not text or not text.strip():
        raise ValueError("Cannot chunk an empty document.")

    paragraphs = re.split(r"\n\s*\n", text.strip())

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        # If adding this paragraph stays within the limit,
        # keep it with the current chunk.
        if len(current_chunk) + len(paragraph) + 2 <= max_chars:
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph

        else:
            # Save the current chunk before starting a new one.
            if current_chunk:
                chunks.append(current_chunk)

            # If a single paragraph is too large, split it by sentences.
            if len(paragraph) > max_chars:
                sentences = re.split(r"(?<=[.!?])\s+", paragraph)

                current_chunk = ""

                for sentence in sentences:
                    if len(current_chunk) + len(sentence) + 1 <= max_chars:
                        if current_chunk:
                            current_chunk += " " + sentence
                        else:
                            current_chunk = sentence
                    else:
                        if current_chunk:
                            chunks.append(current_chunk)

                        current_chunk = sentence

            else:
                current_chunk = paragraph

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    document_path = (
        project_root
        / "data"
        / "policies"
        / "employee_leave_policy.txt"
    )

    document_text = load_text_file(str(document_path))

    chunks = chunk_text(document_text)

    print("Document successfully loaded.")
    print(f"Total chunks created: {len(chunks)}")

    print("\n" + "=" * 60)

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nCHUNK {index}")
        print("-" * 60)
        print(chunk)