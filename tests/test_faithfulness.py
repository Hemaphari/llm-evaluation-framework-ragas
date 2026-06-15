import pytest
from pytest_benchmark import fixture
from ragas import SingleTurnSample
from ragas.metrics import Faithfulness

from conftest import llm_wrapper
from utils import load_test_data, rag_llm_response


@pytest.mark.parametrize("getdata",load_test_data("faithfulness.json"),indirect=True)

@pytest.mark.asyncio
async def test_faithfulness(llm_wrapper,getdata):
    #faithfullness class to check the metric faithfulness
    metric=Faithfulness(llm=llm_wrapper)
    score=await metric.single_turn_ascore(getdata)
    print(score)
    assert score>0.8


@pytest.fixture
#Pytest creates a special request object
def getdata(request):
    test_data=request.param
    response_dict=rag_llm_response(test_data)
    sample = SingleTurnSample(
        user_input=test_data["question"],
        response=response_dict["answer"],
        retrieved_contexts=
        [doc["page_content"]
         for doc in response_dict["retrieved_docs"]
         ]
           )
    return sample