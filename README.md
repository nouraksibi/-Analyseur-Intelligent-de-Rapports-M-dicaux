#  Medical Report Analyzer

An intelligent **Multi-Agent Medical Report Analyzer** that automatically extracts information from medical PDF reports and generates a probable diagnosis using **CrewAI**, **Google Gemini**, and **Streamlit**.

---

##  Overview

Medical Report Analyzer is an AI-powered application designed to analyze medical reports in PDF format.

The system extracts relevant medical information such as patient details, symptoms, laboratory results, and clinical observations before generating a probable diagnosis, risk level, and medical recommendations through a collaborative multi-agent architecture.

> **Note:** This project is intended for educational and research purposes only and does **not** replace professional medical advice. :contentReference[oaicite:0]{index=0}

---

##  Features

-  Upload medical reports in PDF format
-  Automatic medical information extraction
-  AI-assisted diagnosis
- Risk level estimation
-  Medical recommendations
-  Multi-Agent architecture with CrewAI
-  Google Gemini integration
-  Interactive Streamlit interface

---

##  Multi-Agent Architecture

###  Medical Data Extractor

Responsible for:

- Patient information extraction
- Symptoms detection
- Laboratory results extraction
- Clinical observations

###  Medical Diagnostician

Responsible for:

- Medical reasoning
- Probable diagnosis
- Risk assessment
- Personalized recommendations

The system follows a **sequential workflow**, where each agent performs a specialized task before passing its output to the next agent. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

---

##  Technologies

### Backend

- Python
- CrewAI
- Google Gemini
- PyPDF2
- PyYAML
- python-dotenv

### Interface

- Streamlit

---

##  Project Structure

```
Medical-Report-Analyzer/
│
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Medical-Report-Analyzer.git

cd Medical-Report-Analyzer
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit
pip install crewai
pip install "crewai[google-genai]"
pip install google-generativeai
pip install PyPDF2
pip install pyyaml
pip install python-dotenv
```

:contentReference[oaicite:3]{index=3}

---

##  Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

##  Run the Application

```bash
streamlit run main.py
```

Then open

```
http://localhost:8501
```

---

##  Workflow

1. Upload a medical report (PDF).
2. Extract text from the PDF.
3. Medical Data Extractor processes the document.
4. Medical Diagnostician analyzes the extracted information.
5. Generate:
   - Structured medical summary
   - Probable diagnosis
   - Risk level
   - Medical recommendations

---

##  Main Libraries

- CrewAI
- Google Gemini
- Streamlit
- PyPDF2
- PyYAML
- python-dotenv

---


##  Academic Project

Developed at:

**Higher Institute of Computer Science of Kef**

**University of Jendouba**

## 📄 License

This project is developed for **academic and research purposes**.
