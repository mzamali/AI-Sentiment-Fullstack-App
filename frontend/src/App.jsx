import { useState } from "react";
import './App.css'
import axios from "axios"

function App() {
  const[inputText ,setInputText] = useState('')
  const [result, setResult] = useState(null)

  const handleAnalyze= async () => {
    if(!inputText) return
    try{
      const response= await axios.get(`http://127.0.0.1:8000/analyze?text=${inputText}`)
      setResult(response.data)
      console.log("Response from Python:", response.data);

    }catch (error){

    console.error("Connection failed:", error);
    alert("Is your Python server running?");
    }
  }
  return(
    <div className="App">
      <h1>AI Sentiment Dashboard</h1>
      <p>Status: Ready to connect to Python</p>
      <input type="text"  placeholder="Type how you feel..." value={inputText} onChange={(e) => setInputText(e.target.value)}/>
      <button onClick={handleAnalyze}>
        Test input

      </button>
      {result && (
        <div className={`result-card ${result.mood}`}>
        <h2>The AI thinks you are: {result.mood}</h2>
        <p>Confidence Score: {result.score.toFixed(2)}</p>
      </div>
      )}
    </div>
  )
}

export default App