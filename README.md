# 🎓 VTU Smart Study Agent

> **A Multi-Agent AI Study Assistant built using Google Agent Development Kit (ADK).**

## 📖 Overview

VTU Smart Study Agent is an AI-powered assistant that helps engineering students study smarter. It uses a **Multi-Agent Architecture**, where each agent is responsible for a specific task such as explaining concepts, generating quizzes, or creating study plans.

Built using **Google ADK** and **Gemini 2.5 Flash** as part of the **Google AI Agents Capstone Project**.

---

## ✨ Features

* 🤖 Multi-Agent Architecture
* 📚 Study Agent
* ❓ Quiz Agent
* 📅 Planner Agent
* 📄 PDF-based syllabus reading
* 🔌 MCP Integration
* ⚡ Gemini 2.5 Flash
* 🧩 Modular & scalable design

---

## 🏗️ Architecture

```text
                     Student
                        │
                        ▼
                VTU Manager Agent
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Study Agent       Quiz Agent      Planner Agent
      │                 │                 │
      └─────────────────┼─────────────────┘
                        ▼
                  PDF Reader Tool
                        ▼
                 VTU Syllabus PDFs
                        ▼
                 Gemini 2.5 Flash
```

---

## 🤖 Agents

### Manager Agent

Routes user requests to the appropriate specialized agent.

### Study Agent

Explains concepts and answers questions using VTU syllabus PDFs.

### Quiz Agent

Generates multiple-choice questions for revision.

### Planner Agent

Creates personalized study plans based on exam timelines.

---

## 🛠️ Tech Stack

* Python 3.10
* Google Agent Development Kit (ADK)
* Gemini 2.5 Flash
* FastMCP
* PyPDF
* python-dotenv

---

## 📁 Project Structure

```text
vtu-smart-study-agent/
│
├── study_agent/
│   ├── agent.py
│   ├── sub_agents/
│   ├── tools/
│   ├── mcp/
│   ├── memory/
│   └── data/
│
├── tests/
├── README.md
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

```bash
git clone <repository-url>
cd vtu-smart-study-agent

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
adk web
```

---

## 💬 Example Prompts

```text
Explain supervised learning.
```

```text
Generate 10 MCQs from Module 2.
```

```text
My exam is in 5 days. Create a study plan.
```

```text
Explain K-Means, generate 10 MCQs, and create a 3-day revision plan.
```

---

## 🎯 Concepts Demonstrated

* ✅ Multi-Agent Systems
* ✅ Google ADK
* ✅ Tool Calling
* ✅ MCP Integration
* ✅ Modular Agent Design
* ✅ Gemini API Integration

---

## 🚀 Future Improvements

* Persistent Memory
* RAG with Vector Database
* Previous Year Question Paper Analysis
* Voice Assistant
* Progress Tracking Dashboard
* Mobile Application

---

## 👨‍💻 Author

**Yesh**

AI & Machine Learning Engineering Student

🌐 Portfolio: **https://itsyesh.in**
