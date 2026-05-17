export default function About() {
  return (
    <main className="page-container">
      <section className="content-card">
        <h1>About SpamGuard AI</h1>

        <h2>Our Mission</h2>
        <p>
          SpamGuard AI is designed to help users identify dangerous SMS messages
          before they interact with them. The system aims to reduce phishing,
          scams, fraud, and unwanted spam communication.
        </p>

        <h2>How It Works</h2>
        <p>
          The app analyses SMS text using Natural Language Processing. Messages
          are cleaned, processed, and classified using machine learning models
          such as Naive Bayes, Logistic Regression, and LSTM.
        </p>

        <h2>Our Vision</h2>
        <p>
          Our vision is to make mobile communication safer by giving users a
          simple tool that can detect suspicious messages early and provide clear
          safety recommendations.
        </p>
      </section>
    </main>
  );
}