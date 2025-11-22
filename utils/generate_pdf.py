import pdfkit
from weasyprint import HTML

# Full HTML content (your joining letter)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Joining Request - Niva Ecotech</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.4;
      color: #333;
      background-color: #f8f9fa;
      padding: 30px;
    }

    .container {
      max-width: 800px;
      margin: auto;
      background-color: #fff;
      padding: 40px;
      border-radius: 10px;
      box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    h1 {
      text-align: center;
      color: #007BFF;
      margin-bottom: 30px;
      font-size: 28px;
    }

    h2 {
      color: #007BFF;
      margin-top: 20px;
      margin-bottom: 10px;
      font-size: 22px;
    }

    p {
      margin: 10px 0;
    }

    ul {
      margin: 10px 0 20px 20px;
    }

    .signature {
      margin-top: 40px;
    }

    .signature p {
      margin: 5px 0;
    }

    a {
      color: #007BFF;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .highlight {
      font-weight: bold;
      color: #000;
    }

  </style>
</head>
<body>
  <div class="container">
    <h1>Request for Joining – Niva Ecotech Pvt. Ltd.</h1>

    <p>Dear Sir / Madam,</p>

    <p>My name is <span class="highlight">Nishant Nanasaheb Jadhav</span>, currently in my 3rd year of B.Tech in Computer Science & Engineering. I am writing to express my sincere interest in joining <span class="highlight">Niva Ecotech Pvt. Ltd.</span>, given your organization’s leadership in solar park development, rooftop EPC, and operations & maintenance. You can know more about your services at <a href="https://www.nivaecotech.com" target="_blank">nivaecotech.com</a>.</p>

    <p>I have strong skills and keen interest in:</p>
    <ul>
      <li>Software development</li>
      <li>Data Science & Data Analytics</li>
      <li>Machine Learning / AI</li>
      <li>Web Development</li>
      <li>IoT and Automation</li>
    </ul>

    <p>Given these skills, I would like to join <span class="highlight">Niva Ecotech</span> in a role where I can contribute to your digital systems, solar monitoring solutions, and data-driven optimization strategies.</p>

    <h2>Proposed Role</h2>
    <p><span class="highlight">Software & Data Engineer – Solar Monitoring and AI Systems</span></p>

    
    <h2>Key Responsibilities (If appointed)</h2>
    <ul>
      <li>Analyzing solar panel data (voltage, current, temperature, efficiency) to derive insights.</li>
      <li>Building and maintaining web dashboards for real-time monitoring of solar systems.</li>
      <li>Implementing machine learning models for predictive maintenance, fault detection, and energy forecasting.</li>
      <li>Integrating IoT sensors for automated data collection and monitoring , testing to support continuous improvement.</li>
      <li>Developing backend services using Python, SQL, and REST APIs to handle solar performance data.</li>
      <li>Generating periodic (weekly / monthly) reports on system health and performance metrics.</li>
      <li>Prototyping AI-driven tools for anomaly detection, alert systems, and system optimization.</li>
    </ul>

    <h2>Why Me </h2>
    <p><span class="highlight">Why me:</span> My background in computer science, combined with a passion for AI, data, and web development, positions me well to add value to Niva’s technology initiatives.</p>
    
    <p>I kindly request you to consider issuing a formal joining / appointment letter for the proposed role and duration. I am ready to meet or discuss further at your convenience.</p>

    <p>Thank you for considering my application. I truly hope to join <span class="highlight">Niva Ecotech</span> and contribute to building a more sustainable future through technology.</p>

    <div class="signature">
      <p>Warm regards,</p>
      <p><span class="highlight">Nishant Nanasaheb Jadhav</span></p>
      <p>Phone: 9158752508</p>
      <p>Email: nnjadhav2004@gmail.com</p>
    </div>
  </div>
</body>
</html>
"""

# Output PDF file name
pdf_file = "joining_letter.pdf"

# Convert HTML to PDF
pdfkit.from_string(html_content, pdf_file)

print(f"PDF successfully generated: {pdf_file}")
