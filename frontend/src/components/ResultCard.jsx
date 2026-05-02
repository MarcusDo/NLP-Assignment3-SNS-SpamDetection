export default function ResultCard({ result }) {
  if (!result) return null;

  const isSpam = result.label === "spam";
  const confidencePercent = (result.confidence * 100).toFixed(2);

  return (
    <div className="card">
      <h2>Analysis Result</h2>

       <p className="result-note">
  {isSpam
    ? "This message contains patterns commonly found in spam texts."
    : "This message appears similar to normal SMS messages in the training data."}
</p>

      <div className="result-row">
        Prediction:{" "}
        <span className={`result-badge ${isSpam ? "result-spam" : "result-ham"}`}>
          {result.label.toUpperCase()}
        </span>
      </div>

     {result.keywords && (
  <div style={{ marginTop: "20px", textAlign: "center" }}>
    <p><strong>Key indicators:</strong></p>
    <div>
      {result.keywords.map((word, i) => (
        <span key={i} className="keyword">{word}</span>
      ))}
    </div>
  </div>
)}

      <div className="result-row">
        Confidence: <strong>{confidencePercent}%</strong>
      </div>

      <div className="confidence-bar">
        <div
          className={`confidence-fill ${
            isSpam ? "confidence-spam" : "confidence-ham"
          }`}
          style={{ width: `${confidencePercent}%` }}
        />
      </div>
    </div>
  );
}