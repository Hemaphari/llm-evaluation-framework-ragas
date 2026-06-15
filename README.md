# llm-evaluation-framework-ragas
QA-focused LLM evaluation framework for assessing response quality, faithfulness, relevance, and retrieval effectiveness in RAG applications using RAGAS.

# Overview
This project demonstrates automated evaluation and testing of Retrieval-Augmented Generation (RAG) applications using RAGAS, Python, and Pytest.
Traditional software testing validates deterministic outputs, while Large Language Models (LLMs) require evaluation of response quality, factual accuracy, context utilization, and adherence to expected topics. This framework automates the assessment of AI-generated responses using industry-recognized evaluation metrics.
The project was developed as part of my exploration into AI Quality Assurance, LLM Testing, and Generative AI evaluation techniques.

# Objectives
Evaluate the quality of LLM-generated responses using structured evaluation metrics.
Assess retrieval effectiveness in Retrieval-Augmented Generation (RAG) applications.
Measure context relevance and completeness using context precision and context recall.
Validate response quality through faithfulness, response relevancy, and topic adherence.
Apply automated evaluation using Pytest with RAGAS-based scoring methods.

# Evaluation Metrics Implemented

# Context Precision:
Measures how relevant the retrieved context is to the generated response.

Why it matters: High context precision indicates that retrieved documents contain information directly useful for answering the user's question.

# Context Recall:
Measures whether the retrieved context contains all the information necessary to answer the user's query.

Why it matters: High context recall ensures important information was not missed during retrieval.

# Faithfulness:
Evaluates whether the generated response is supported by the retrieved context.

Why it matters: Helps identify hallucinations and unsupported statements.

# Response Relevancy:
Measures how well the generated response addresses the user's question.

Why it matters: Ensures the model remains focused on the user's intent and provides meaningful answers.

# Topic Adherence:
Evaluates whether the generated response stays aligned with the expected topic or domain.

Why it matters: Prevents responses from drifting into unrelated subjects and improves answer consistency.

# Rubrics Score:
Evaluates responses against predefined evaluation criteria or scoring rubrics.

Why it matters: Allows customized assessment based on business requirements, quality standards, or domain-specific expectations.

# Project Structure
```text
llm-evaluation-framework-ragas/

├── test_data/
│   ├── context_precision.json
│   ├── context_recall.json
│   ├── faithfulness.json
│   ├── response_relevancy_faithfulness.json
│   └── rubrics_score.json
│
├── tests/
│   ├── test_context_precision.py
│   ├── test_context_recall.py
│   ├── test_faithfulness.py
│   ├── test_response_relevancy_faithfulness.py
│   ├── test_topic_adherence.py
│   └── test_rubrics_score.py
│
├── utils.py
├── confest.py
├── README.md
└── screenshots/
```

# Technologies Used
Python
Pytest
RAGAS
OpenAI
JSON
Git
GitHub
