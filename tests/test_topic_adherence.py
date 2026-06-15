import pytest
from pytest_benchmark import fixture
from ragas import SingleTurnSample, MultiTurnSample
from ragas.messages import HumanMessage, AIMessage
from ragas.metrics import Faithfulness, TopicAdherenceScore

from conftest import llm_wrapper
from utils import load_test_data, rag_llm_response
#.........................
#Evaluate multi conversation

#@pytest.mark.parametrize("getdata",load_test_data("faithfulness.json"),indirect=True)

@pytest.mark.asyncio
#check how strict the conversation sticking to the topic
async def test_topicAdherence(llm_wrapper,getdata):
    #faithfulness class to check the metric faithfulness
    topic_score=TopicAdherenceScore(llm=llm_wrapper)
    score=await topic_score.multi_turn_ascore(getdata)
    print(score)
    assert score>0.8


@pytest.fixture
#Pytest creates a special request object
def getdata(request):
    #test_data=request.param
    #response_dict=rag_llm_response(test_data)
    conversation=[
        HumanMessage(content="How many articles are there in the selenium WebDriver python course?"),
        AIMessage(content="There are 23 articles in the selenium WebDriver python course"),
        HumanMessage(content="How many downloadable resources are there in this course? "),
        AIMessage(content="There are 9 downloadable resources in the course")
    ]
    reference=["""
        The AI should:
        1.give results related to selenium webdriver python course
        2. there are 23 articles and 9 downloadable resources in the course"""
    ]
    sample = MultiTurnSample(user_input=conversation,reference_topics=reference)
    return sample