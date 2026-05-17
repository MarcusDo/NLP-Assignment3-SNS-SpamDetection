import { Link } from "react-router-dom";

export default function Home() {
  return (
    <main>
      <section className="hero">
        <div className="hero-overlay">
          <h1>Detect Spam Before It Tricks You</h1>
          <p>
            AI-powered SMS spam detection using Natural Language Processing and
            machine learning models.
          </p>

          <div className="hero-buttons">
            <Link to="/feature" className="btn primary">
              Try Detector
            </Link>
            <Link to="/about" className="btn secondary">
              Learn More
            </Link>
          </div>
        </div>
      </section>

      <section className="features-preview">
        <div className="feature-card">
          <div className="feature-icon">🔍</div>
          <h3>SMS Analysis</h3>
          <p>Analyse message text and identify spam patterns instantly.</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">⚠️</div>
          <h3>Spam Risk Alert</h3>
          <p>Show whether a message is safe, suspicious, or high risk.</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">📊</div>
          <h3>Model Comparison</h3>
          <p>Compare Naive Bayes, Logistic Regression, and LSTM results.</p>
        </div>
      </section>
    </main>
  );
}