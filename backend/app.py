from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import base64


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],      # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/savecanvas")
async def save_canvas(request: Request):
    data = await request.json()
    image_data = data["image"].split(",")[1]  # Remove data:image/png;base64,
    with open("saved_canvas.png", "wb") as f:
        f.write(base64.b64decode(image_data))
    return {"status": "saved"}