from pathlib import Path


def load_text_file(file_path: str) -> str:
    """
    Load a text document and return its contents.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported at this stage.")

    text = path.read_text(encoding="utf-8")

    if not text.strip():
        raise ValueError("The document is empty.")

    return text


if __name__ == "__main__":
    # Find the PolicyPilot project root
    project_root = Path(__file__).resolve().parent.parent

    # Locate the policy document
    document_path = (
        project_root
        / "data"
        / "policies"
        / "employee_leave_policy.txt"
    )

    document_text = load_text_file(str(document_path))

    print("Document loaded successfully!")
    print("-" * 50)
    print(document_text)