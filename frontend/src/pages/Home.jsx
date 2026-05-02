import { useState } from "react";
import MessageInput from "../components/MessageInput";
import ResultCard from "../components/ResultCard";
import { predictSpam } from "../services/api";

export default function Home() {
  const [result, setResult] = useState(null);

  const handleSubmit = async (text) => {
    try {
      const res = await predictSpam(text);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error calling API");
    }
  };

  return (
    <div className="container">
     <h1>📩 SMS Spam Detector</h1>
    <p className="subtitle">
     Enter an SMS message and let the machine learning model classify it as spam or ham.
    </p>
    
      <MessageInput onSubmit={handleSubmit} />
      <ResultCard result={result} />
    </div>
  );
}