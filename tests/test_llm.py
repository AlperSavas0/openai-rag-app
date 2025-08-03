from app.llm import get_answer

# Test for generating an answer from question and context using LLM

def test_get_answer_returns_response():
    context = ["Bu belge yapay zeka konularını ele almaktadır."]
    question = "Bu belge ne hakkında?"
    answer = get_answer(question, context)
    assert isinstance(answer, str)
    assert len(answer) > 0