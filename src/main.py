from fastapi import FastAPI
from langchain import LLM

app = FastAPI()

llm = LLM(model_name="gpt-3")

@app.post("/generate")
async def generate_text(prompt: str):
    try:
        response = llm.generate(prompt)
        return {"generated_text": response.text}
    except Exception as e:
        return {"error": str(e)}