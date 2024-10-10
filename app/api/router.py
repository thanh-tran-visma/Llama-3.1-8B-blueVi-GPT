from fastapi import FastAPI
from .routes import chat_endpoint

app = FastAPI()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# The chat route
app.post("/chat")(chat_endpoint)
