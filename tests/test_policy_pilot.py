import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from rag_pipeline import answer_policy_question


def test_sick_leave():
    result = answer_policy_question(
        "How many sick leave days are available?"
    )

    assert "12" in result["answer"]
    assert len(result["sources"]) > 0


def test_annual_leave():
    result = answer_policy_question(
        "How many annual leave days do employees get?"
    )

    assert "18" in result["answer"]
    assert len(result["sources"]) > 0


def test_notice_period():
    result = answer_policy_question(
        "How much notice is required for annual leave?"
    )

    assert "5 working days" in result["answer"]
    assert len(result["sources"]) > 0


def test_irrelevant_question():
    result = answer_policy_question(
        "What is the company salary structure?"
    )

    assert len(result["sources"]) == 0
    assert "could not find" in result["answer"].lower()
    
    