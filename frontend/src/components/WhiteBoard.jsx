import { useState, useRef } from "react";

const WhiteBoardCanvas = () => {

    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [lastPos, setLastPos] = useState({x: 0, y: 0 }) // to save mouse position along the way

    const startDrawing = (e) => {
        setIsDrawing(true);
        const rect = canvasRef.current.getBoundingClientRect();
        setLastPos({
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        })
        console.log(lastPos)
    }

    const draw = () => {
        console.log("Drawing");

    }

    const stopDrawing = () => {
        console.log("strop Drawing");
        setIsDrawing(false);
    }

    return (
        <canvas 
            ref = {canvasRef}
            width={800} 
            height={400}
            style={{border: "1px solid black"}}
            onMouseDown={startDrawing}
            onMouseMove={draw}
            onMouseUp={stopDrawing}
            onMouseLeave={stopDrawing} 
        />
    )
}

export default WhiteBoardCanvas;