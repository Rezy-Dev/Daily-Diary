# Daily Diary

**Daily Diary** is a web application written in Python using the ReportLab library. It is an intentionally vulnerable app created for educational purposes, particularly for cybersecurity training. The app contains a critical vulnerability related to user-controlled input in PDF generation, which can be exploited for malicious purposes.

This app was initially created by me for the WeShieldCyber CTF Event qualifiers, but I decided to make it public so that everyone can access it and learn from it.

---

## Features

| Feature            | Description                                           | Notes                              |
|--------------------|-------------------------------------------------------|------------------------------------|
| User Registration  | Allows users to register accounts.                   | Basic account creation.            |
| User Login         | Allows registered users to log in.                   | Session-based authentication.      |
| Diary Entry        | Users can create and save diary entries.             | Entries are rendered in pdf.       |
| PDF Generation     | Generates PDFs from user-submitted text.             | Exploitable vulnerability present. |

---

## Directory Structure

```plaintext
.
├── app.py              # Main application script.
├── docker-compose.yml  # Docker Compose file for containerized setup.
├── Dockerfile          # Dockerfile for building the app container.
├── flag.txt            # File containing a secret flag (for CTF challenges).
├── LICENSE             # MIT License.
├── README.md           # This document.
├── requirements.txt    # Python dependencies.
└── templates
   ├── diary.html       # Template for diary entry page.
   ├── home.html        # Template for home page.
   ├── layout.html      # Base layout template.
   ├── login.html       # Template for login page.
   └── register.html    # Template for registration page.
```

---

## Setup

### Prerequisites

- Docker Engine installed on your system.

---

### Deployment Using Docker

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Rezy-Dev/Daily-Diary.git
   cd Daily-Diary
   ```

2. **Build the Docker Image:**
   ```bash
   docker compose up -d
   ```
   > After this, the app should be **running locally.** i.e `port 3003`

---

## Access the Application

1. Open your browser and navigate to `http://localhost:3003` (or the specified port in your Docker configuration).
2. Start exploring the features of the app.

---

## Note on Vulnerability

Since you are exploring this app for educational purposes, it’s important to understand the potential risks of insecure code practices. For instance, this app uses the ReportLab library (version `3.5.0`) for PDF generation. Improper sanitization of user input in this process can lead to unintended consequences. Learn more about this type of vulnerability in the following article:

- [ReportLab Vulnerabilities in Web Applications](https://rezydev.xyz/research/)

---

## License

License? What is this, a driver's license? A drinking license? Do we even need one here???

Well, technically, yes. There is a [MIT License](https://github.com/Rezy-Dev/Daily-Diary/blob/main/LICENSE) (but don’t worry, it’s not as complicated as it sounds).
