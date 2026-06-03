import pytest
from autohf.agents.task_agent import detect_task, TaskAgent


def test_keyword_detection():
    # Exact keyword mapping
    res = detect_task("sentiment analysis of reviews")
    assert res.task_type == "text-classification"
    assert res.confidence == 1.0

    # Another one
    res = detect_task("named entity recognition for medical text")
    assert res.task_type == "token-classification"
    assert res.confidence == 1.0


def test_fuzzy_fallback():
    # Fuzzy match
    res = detect_task("extract entities")
    assert res.task_type == "token-classification"
    assert res.confidence >= 0.65


def test_task_agent_history():
    agent = TaskAgent(router="keyword")
    assert len(agent.history) == 0
    
    agent("sentiment of movie reviews")
    assert len(agent.history) == 1
    assert agent.history[0].task_type == "text-classification"
    
    agent.reset()
    assert len(agent.history) == 0
