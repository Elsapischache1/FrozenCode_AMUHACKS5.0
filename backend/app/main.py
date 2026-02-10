from fastapi import FastAPI

app = FastAPI(title="Synapse Backend")

@app.get("/health")
def health():
    return {"status": "Backend running with Conda"}
