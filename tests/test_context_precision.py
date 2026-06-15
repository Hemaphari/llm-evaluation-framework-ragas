import asyncio
import pytest
import requests
from ragas.dataset_schema import SingleTurnSample
from ragas.llms.base import LangchainLLMWrapper
from ragas.metrics._context_precision import LLMContextPrecisionWithoutReference

from utils import load_test_data, rag_llm_response


@pytest.mark.parametrize("getdata",
                         load_test_data("context_precision.json"),indirect=True)
@pytest.mark.asyncio
async def test_context_precision(llm_wrapper,getdata):

    metric=LLMContextPrecisionWithoutReference(llm=llm_wrapper)
    score = await metric.single_turn_ascore(getdata)
    print(score)

@pytest.fixture
def getdata(request):
        # catch param
        test_data = request.param
        response_dict = rag_llm_response(test_data)
        sample=SingleTurnSample(
        user_input=test_data["question"],
        response=response_dict["answer"],
        retrieved_contexts=
        [doc["page_content"]
            for doc in response_dict["retrieved_docs"]
        ]
    )
        return sample
