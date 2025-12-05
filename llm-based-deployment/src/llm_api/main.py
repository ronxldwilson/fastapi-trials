from fastapi import FastAPI
from pydantic import BaseModel
from llm_api.model_loader import load_model

app = FastAPI()

class Prompt(BaseModel):
    prompt: str
    max_tokens: int = 128
    
@app.post("/generate")
def generate_text(data: Prompt):
    model = load_model()
    
    output = model(
        data.prompt,
        max_length = data.max_tokens,
        temperature=0.7,
        top_p=0.9
    )
    return {"response": output}