import { useState, useEffect, useRef } from "react";

const useWebSocket = (url) => {
    const ws = useRef(null);

    useEffect(() => {
        ws.current = new window.WebSocket(url);

        ws.current.onopen = () => {
            console.log("WebSocket connected");
        };

        ws.current.onmessage = (event) => {
            console.log("Received:", event.data);
        };

        ws.current.onclose = () => {
            console.log("WebSocket disconnected");
        };

        return () => {
            ws.current.close();
        };
    }, [url]);

    return ws;
};

const WhiteBoardCanvas = () => {
    const ws = useWebSocket("ws://127.0.0.1:8765");
    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [currentPos, setCurrentPos] = useState({x: 0, y:0});
    const [lastPos, setLastPos] = useState({x: 0, y: 0 }); // to save mouse position along the way
    const gridSize = 5 ; // use to snape pixel

    const saveCanvas = () => {
        const canvas = canvasRef.current;
        const dataUrl = canvas.toDataURL("image/png");
        fetch("http://localhost:8000/savecanvas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: dataUrl })
        });
    };

    const startDrawing = (e) => {
        setIsDrawing(true);
        // console.log(lastPos)
        draw(e)
    }

    const draw = (e) => {
        if (!isDrawing) return;
        console.log("Drawing");
        const rect = canvasRef.current.getBoundingClientRect();
        const currentPos ={
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        }

        // snap to grid
        const snappedX = Math.floor(currentPos.x / gridSize) * gridSize;
        const snappedY = Math.floor(currentPos.y / gridSize) * gridSize;

        const ctx = canvasRef.current.getContext("2d");
        ctx.fillRect(snappedX, snappedY, gridSize, gridSize);

        setLastPos(currentPos)
        saveCanvas();

    }

    const stopDrawing = () => {
        // console.log("strop Drawing");
        setIsDrawing(false);
    }

    


    return (
        <canvas 
            ref = {canvasRef}
            width={1000}
            height={700}
            style={{border: "1px solid black"}}
            onMouseDown={startDrawing}
            onMouseMove={draw}
            onMouseUp={stopDrawing}
            onMouseLeave={stopDrawing} 
        />
    )
}

export default WhiteBoardCanvas;