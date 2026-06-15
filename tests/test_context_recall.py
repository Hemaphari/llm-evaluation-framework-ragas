import os
import pytest
import requests
from langchain_openai import ChatOpenAI
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import ContextRecall

from utils import rag_llm_response, load_test_data



#parametrise test with diffent data set
#first argument: to which fixture we are sending data, what you want to feed(list with multiple test data), instead of applying this data to test first use it in fixture
@pytest.mark.parametrize("getdata",
                         load_test_data("context_recall.json"),indirect=True)
@pytest.mark.asyncio
async def test_context_recall(llm_wrapper,getdata):

    
    metric = ContextRecall(llm=llm_wrapper)
    score=await metric.single_turn_ascore(getdata)
    print("value=",score)
    #assert score>0.7

@pytest.fixture
def getdata(request):
    # catch param
    test_data = request.param
    response_dict=rag_llm_response(test_data)

    sample = SingleTurnSample(
        user_input=test_data["question"],
        retrieved_contexts=
        [doc["page_content"]
         for doc in response_dict["retrieved_docs"]
         ],
        reference=test_data["reference"]

    )
    return sample