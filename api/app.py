from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

llm = ChatOllama(model="llama3.2")

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 year old child with 100 words"
)

essay_chain = prompt1 | llm
poem_chain = prompt2 | llm

class TopicRequest(BaseModel):
    topic: str
    
@app.get("/essay")
async def generate_essay_get():
    

    return {
        "answer": "hi"
    }
    


@app.post("/essay")
async def generate_essay(request: TopicRequest):
    response = await essay_chain.ainvoke({
        "topic": request.topic
    })

    return {
        "answer": response.content
    }
    
heritage_prompt = ChatPromptTemplate.from_template(
    "Write me a poem in 20 words about India's heritage."
)
heritage_chain=heritage_prompt|llm  
    
@app.get("/poem")
async def give_heritage_poem():
    response = await heritage_chain.ainvoke({
    })
    return {
        "heritage_poem": response.content
    }

@app.post("/poem")
async def generate_poem(request: TopicRequest):
    response = await poem_chain.ainvoke({
        "topic": request.topic
    })

    return {
        "answer": response.content
    }

@app.post("/chat")
async def chat(request: TopicRequest):
    response = await llm.ainvoke(request.topic)

    return {
        "answer": response.content
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)