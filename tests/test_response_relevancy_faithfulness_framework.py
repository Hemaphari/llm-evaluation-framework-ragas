import pytest

from ragas import SingleTurnSample, EvaluationDataset, evaluate
from ragas.metrics import ResponseRelevancy, FactualCorrectness
from urllib3.util import request

from utils import load_test_data, rag_llm_response


@pytest.mark.parametrize("get_data",load_test_data("response_relevancy_faithfulness.json"),indirect=True)

@pytest.mark.asyncio
async def test_response_relevancy_faithfulness(llm_wrapper, get_data):
    metrics=[ResponseRelevancy(llm=llm_wrapper),
            FactualCorrectness(llm=llm_wrapper)]
    #get sample data and convert into ragas dataset format
    eval_dataset=EvaluationDataset([get_data])
    #evaluate metric results
    results=evaluate(dataset=eval_dataset,metrics=metrics)
    #if we dont mention the metric to test, ragas can do test for some basic metrics using following code
    #results=evaluate(dataset=eval_dataset)
    print(results)



@pytest.fixture
def get_data(request):
     test_data=request.param
     response_dict=rag_llm_response(test_data)
     sample= SingleTurnSample(
         user_input=test_data["question"],
         response=response_dict["answer"],
         retrieved_contexts=
         [doc["page_content"]
          for doc in response_dict["retrieved_docs"]
         ],
         reference=test_data["reference"]
     )
     return sample