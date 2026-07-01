from fastapi import FastAPI

app = FastAPI(
    title="OptiRoute AI",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "OptiRoute AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }