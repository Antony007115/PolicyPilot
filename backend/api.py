from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from rag_pipeline import answer_policy_question
from llm import GeminiUnavailableError


app = FastAPI(
    title="PolicyPilot API",
    description="Enterprise Policy Question-Answering API",
    version="1.0.0"
)


# -----------------------------
# Request Model
# -----------------------------

class QuestionRequest(BaseModel):
    question: str


# -----------------------------
# Source Response Model
# -----------------------------

class SourceInfo(BaseModel):
    source: str | None = None
    document_id: str | None = None
    chunk_id: int | None = None
    version: str | None = None


# -----------------------------
# Answer Response Model
# -----------------------------

class AnswerResponse(BaseModel):
    answer: str
    sources: list[SourceInfo]


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
def root():
    return {
        "message": "PolicyPilot API is running",
        "status": "success"
    }


# -----------------------------
# Health Check Endpoint
# -----------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PolicyPilot API"
    }


# -----------------------------
# Ask Policy Endpoint
# -----------------------------

@app.post("/ask", response_model=AnswerResponse)
def ask_policy(request: QuestionRequest):

    # Validate empty question
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:

        result = answer_policy_question(
            request.question
        )

        return result

    # Invalid request / validation-related error
    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    # Gemini temporarily unavailable
    except GeminiUnavailableError:

        raise HTTPException(
            status_code=503,
            detail=(
                "The AI service is temporarily unavailable. "
                "Please try again later."
            )
        )

    # Any unexpected application error
    except Exception as error:

        print(
            f"Unexpected API error: {error}"
        )

        raise HTTPException(
            status_code=500,
            detail="An unexpected internal server error occurred."
        )