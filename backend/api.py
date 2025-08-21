from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import base64
import asyncio
import websockets


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],      # Allow all headers
)



#websocket connection
ws_connection = None
async def connect_websocket():
    global ws_connection
    uri = "ws://127.0.0.1:8765"
    ws_connection = await websockets.connect(uri)


@app.on_event("startup")
async def root():
    await connect_websocket()
    return {"message": "Hello World"}

@app.post("/send")
async def send_message():
    image='I am here'
    if ws_connection :
        await ws_connection.send(image)
        return {"image sent"}
    return {"Not connected"}

@app.post("/savecanvas")
async def save_canvas(request: Request):
    data = await request.json()
    image_data = data["image"].split(",")[1]  # Remove data:image/png;base64,
    if ws_connection :
        await ws_connection.send(image_data)
        with open("saved_canvas.png", "wb") as f:
            f.write(base64.b64decode(image_data))
        return {"status": "saved and shared"}
    return {"Not connected"}