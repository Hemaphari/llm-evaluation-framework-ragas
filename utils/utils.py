#store reusable code here, like the api call code
import json
from pathlib import Path

import requests
#get json data from the json file location and just save it as json, f is the entire file content as object , go to the file and read it and add it in the object f and then convert it into proper json
def load_test_data(file_name):
    #getting path of the parent directory
    project_directory=Path(__file__).parent.absolute()
    test_data_path=project_directory/"testdata"/file_name
    with open(test_data_path) as f:
       return json.load(f)

def rag_llm_response(test_data):
    response_dict = requests.post("https://rahulshettyacademy.com/rag-llm/ask",
                              json={
                                  "question": test_data["question"],
                                  "chat_history": [

                                  ]
                              }).json()
    return response_dict