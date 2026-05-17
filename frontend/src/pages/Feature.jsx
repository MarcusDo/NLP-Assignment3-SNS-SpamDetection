import { useState } from "react";

export default function Feature() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);

  function checkMessage() {
    if (!message.trim()) {
      alert("Please enter an SMS message first.");
      return;
    }

    const lowerMessage = message.toLowerCase();

    const spamWords = [
      "free",
      "win",
      "winner",
      "claim",
      "urgent",
      "click",
      "prize",
      "cash",
      "reward",
      "limited",
      "offer",
      "congratulations",
    ];

    const foundWords = spamWords.filter((word) => lowerMessage.includes(word));

    const isSpam = foundWords.length >= 2;

    const mockResult = {
      finalPrediction: isSpam ? "Spam" : "Safe",
      confidence: isSpam ? 97 : 91,
      riskLevel: isSpam ? "High" : "Low",
      recommendation: isSpam
        ? "Do not click any links, reply, or share personal information."
        : "This message looks safe, but always check the sender carefully.",
      suspiciousWords: foundWords,
      models: [
        {
          name: "Naive Bayes",
          prediction: isSpam ? "Spam" : "Safe",
          confidence: isSpam ? 94 : 88,
        },
        {
          name: "Logistic Regression",
          prediction: isSpam ? "Spam" : "Safe",
          confidence: isSpam ? 96 : 91,
        },
        {
          name: "LSTM",
          prediction: isSpam ? "Spam" : "Safe",
          confidence: isSpam ? 98 : 93,
        },
      ],
    };

    setResult(mockResult);
  }

  return (
    <main className="page-container">
      <section className="detector-card">
        <h1>SMS Spam Detection</h1>
        <p className="subtitle">
          Paste an SMS message below to check whether it is spam or safe.
        </p>

        <textarea
          className="sms-input"
          placeholder="Example: Congratulations! You won a free prize. Click here to claim now."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button className="check-btn" onClick={checkMessage}>
          Check Message
        </button>

        {result && (
          <section className="result-section">
            <div
              className={
                result.finalPrediction === "Spam"
                  ? "result-card spam"
                  : "result-card safe"
              }
            >
              <h2>
                Result: <span>{result.finalPrediction}</span>
              </h2>
              <p>Confidence: {result.confidence}%</p>
              <p>Risk Level: {result.riskLevel}</p>
              <p>{result.recommendation}</p>
            </div>

            <div className="explanation-card">
              <h2>Explanation</h2>
              {result.suspiciousWords.length > 0 ? (
                <p>
                  Suspicious words found:{" "}
                  <strong>{result.suspiciousWords.join(", ")}</strong>
                </p>
              ) : (
                <p>No obvious spam keywords were found in this message.</p>
              )}
            </div>

            <div className="model-card">
              <h2>Model Comparison</h2>

              <table>
                <thead>
                  <tr>
                    <th>Model</th>
                    <th>Prediction</th>
                    <th>Confidence</th>
                  </tr>
                </thead>

                <tbody>
                  {result.models.map((model) => (
                    <tr key={model.name}>
                      <td>{model.name}</td>
                      <td>{model.prediction}</td>
                      <td>{model.confidence}%</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}
      </section>
    </main>
  );
}