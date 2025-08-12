import { useState, useRef } from "react";

const WhiteBoardCanvas = () => {

    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [currentPos, setCurrentPos] = useState({x: 0, y:0});
    const [lastPos, setLastPos] = useState({x: 0, y: 0 }); // to save mouse position along the way
    

    const startDrawing = (e) => {
        setIsDrawing(true);
        const rect = canvasRef.current.getBoundingClientRect();
        setLastPos({
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        })
        console.log(lastPos)
    }

    const draw = (e) => {
        if (!isDrawing) return;
        console.log("Drawing");
        const rect = canvasRef.current.getBoundingClientRect();
        setCurrentPos({
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        })

        const ctx = canvasRef.current.getContext("2d");
        ctx.beginPath();
        ctx.moveTo(lastPos.x, lastPos.y);
        ctx.lineTo(currentPos.x, currentPos.y);
        ctx.stroke();

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