# langchain-fastapi-integration

A library that integrates Langchain with FastAPI, enabling easy creation of LLM-powered APIs.

## Installation

```bash
pip install langchain-fastapi-integration
```

## Usage

Here's a simple example:

```python
from fastapi import FastAPI
from langchain import LLM

app = FastAPI()

llm = LLM(model_name="gpt-3")

@app.post("/generate")
async def generate_text(prompt: str):
    response = llm.generate(prompt)
    return {"generated_text": response.text}
```

## Features
- Seamless integration of Langchain with FastAPI
- Easy to use and integrate into existing projects
- Well-documented API

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.