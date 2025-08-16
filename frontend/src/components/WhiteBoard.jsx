import { useState, useRef } from "react";

const WhiteBoardCanvas = () => {

    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [currentPos, setCurrentPos] = useState({x: 0, y:0});
    const [lastPos, setLastPos] = useState({x: 0, y: 0 }); // to save mouse position along the way
    const gridSize = 5 ; // use to snape pixel

    const startDrawing = (e) => {
        setIsDrawing(true);
        console.log(lastPos)
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

    }

    const stopDrawing = () => {
        console.log("strop Drawing");
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