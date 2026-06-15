import os

import pytest
from langchain_openai import ChatOpenAI
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import ContextRecall


@pytest.fixture
def llm_wrapper():
    os.environ[
        "OPENAI_API_KEY"] = "KEY"
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    langchain_llm = LangchainLLMWrapper(llm)  # object of openai llm which can understand by ragas
    return langchain_llm