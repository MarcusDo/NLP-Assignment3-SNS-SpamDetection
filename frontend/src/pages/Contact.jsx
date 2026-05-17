export default function Contact() {
  return (
    <main className="page-container">
      <section className="contact-card">
        <div className="contact-title">Contact Us</div>

        <div className="contact-grid">
          <div className="contact-box">
            <h3>📞 Phone Number</h3>
            <p>+61 420 770 868</p>
            <p>+84 782 299 868</p>
          </div>

          <div className="contact-box">
            <h3>✉️ Email</h3>
            <p>minhphuc.duong@student.uts.edu.au</p>
            <p>team.spamguard@student.uts.edu.au</p>
          </div>

          <div className="contact-box">
            <h3>📍 Location</h3>
            <p>15 Broadway</p>
            <p>Ultimo, NSW</p>
          </div>

          <div className="contact-box">
            <h3>🕘 Working Hours</h3>
            <p>Monday to Saturday</p>
            <p>09:00 AM – 06:00 PM</p>
          </div>
        </div>
      </section>
    </main>
  );
}