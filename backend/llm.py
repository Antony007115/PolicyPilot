import os
import time
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.8-flash"


class GeminiUnavailableError(Exception):
    """Raised when Gemini is temporarily unavailable."""
    pass


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using only the provided policy context.

    Retries Gemini requests if the service temporarily fails.
    """

    prompt = f"""
You are PolicyPilot, an enterprise policy question-answering assistant.

Your job is to answer the user's question using ONLY the policy
information provided in the CONTEXT.

STRICT RULES:
1. Use only information present in the CONTEXT.
2. Do not invent or assume policy information.
3. If the answer cannot be found in the CONTEXT, say:
   "I could not find this information in the provided policy."
4. Give a concise and clear answer.
5. Do not use outside knowledge.

CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            if response.text:
                return response.text.strip()

            raise GeminiUnavailableError(
                "Gemini returned an empty response."
            )

        except Exception as error:

            print(
                f"Gemini request failed "
                f"(attempt {attempt + 1}/{max_retries}): {error}"
            )

            # If this was the final attempt, stop retrying
            if attempt == max_retries - 1:
                raise GeminiUnavailableError(
                    "Gemini service is temporarily unavailable."
                )

            # Wait before retrying
            time.sleep(2)


if __name__ == "__main__":

    test_question = "How many sick leave days can an employee take?"

    test_context = """
    Employees may take up to 12 days of sick leave per calendar year.
    """

    try:
        answer = generate_answer(
            test_question,
            test_context
        )

        print("=" * 60)
        print("GEMINI TEST")
        print("=" * 60)
        print("Question:", test_question)
        print()
        print("Answer:", answer)

    except GeminiUnavailableError as error:
        print("Gemini unavailable:", error)