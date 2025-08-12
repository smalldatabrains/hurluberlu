import { useState } from "react";

const WhiteBoardCanvas = () => {

    const startDrawing = () => {
        console.log("start Drawing")
    }

    const draw = () => {
        console.log("Drawing")
    }

    const stopDrawing = () => {
        console.log("strop Drawing")
    }

    return (
        <canvas 
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