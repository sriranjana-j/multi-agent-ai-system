# 🤖 Multi-Agent AI System (Production-Ready)

🚀 A cloud-deployed, intelligent multi-agent AI system built using **Google ADK**, capable of managing tasks, notes, schedules, and knowledge retrieval through coordinated agent workflows.

---

## 🌐 Live Demo

👉 https://multi-agent-ai-684072970800.asia-south1.run.app

> ⚡ Try:
>
> * "Add a task to complete assignment"
> * "Schedule a meeting tomorrow"
> * "Save note about AI project"
> * "What is artificial intelligence?"

---

## 🧠 Key Features

* 🧠 **Multi-Agent Architecture**

  * Coordinator + sub-agents working together
* 🔁 **Multi-Step Workflow Execution**

  * Handles complex user requests intelligently
* 🛠️ **Tool Integration (MCP Style)**

  * Task manager, notes system, calendar, Wikipedia
* 💾 **Structured Data Storage**

  * SQLite-based task & notes storage
* 🌍 **Knowledge Retrieval**

  * Real-time answers using Wikipedia tool
* ☁️ **Cloud Deployment**

  * Fully deployed on Google Cloud Run
* 🧾 **Clean Response Formatting**

  * User-friendly, structured outputs

---

## 🏗️ Architecture Overview

```
User Input
    ↓
Root Agent (Entry Point)
    ↓
Sequential Workflow
    ├── Research Agent (Decision Maker)
    │     ├── Task Tool
    │     ├── Notes Tool
    │     ├── Calendar Tool
    │     └── Wikipedia Tool
    ↓
Response Formatter Agent
    ↓
Final Output to User
```

---

## ⚙️ Tech Stack

| Category   | Technology          |
| ---------- | ------------------- |
| Language   | Python              |
| Framework  | Google ADK          |
| Tools      | LangChain Community |
| Database   | SQLite              |
| Deployment | Google Cloud Run    |
| AI Model   | Gemini (Vertex AI)  |

---

## 📂 Project Structure

```
multi-agent-system/
├── agent.py          # Core multi-agent logic
├── database.py       # SQLite operations
├── run.py            # Local execution
├── requirements.txt  # Dependencies
├── __init__.py
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sriranjana-j/multi-agent-ai-system.git
cd multi-agent-ai-system
```

---

### 2️⃣ Setup Environment

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

---

### 3️⃣ Run Locally

```bash
python run.py
```

---

## ☁️ Deployment (Cloud Run)

This project is deployed using Google ADK CLI:

```bash
uvx --from google-adk==1.14.0 adk deploy cloud_run
```

---

## 🧪 Example Use Cases

### ✅ Task Management

```
Add a task to complete assignment
```

### 📅 Scheduling

```
Schedule meeting tomorrow at 5pm
```

### 📝 Notes

```
Save note about AI project ideas
```

### 🌍 Knowledge Queries

```
What do lions eat?
```

### 🔥 Multi-Step Workflow

```
Schedule meeting and remind me to prepare slides
```

---

## 🧠 How It Works

* The **Root Agent** receives user input
* It passes control to a **Sequential Workflow**
* The **Research Agent** decides which tools to use
* Multiple tools can be triggered dynamically
* The **Formatter Agent** generates clean output

👉 This demonstrates **real-world AI orchestration**

---

## ⚠️ Limitations

* SQLite storage is temporary (Cloud Run `/tmp`)
* Calendar is simulated (not real API yet)
* No persistent memory across sessions

---

## 🚀 Future Enhancements

* 🔥 Firestore (persistent database)
* 📅 Google Calendar API integration
* 🧠 Long-term memory
* 📄 Document / PDF processing
* 🎙️ Voice interaction
* 🌐 Custom frontend UI

---

## 👨‍💻 Author

**J Sri Ranjana**

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share it

---

## 📌 Why This Project Matters

This project demonstrates:

* Real-world **multi-agent AI systems**
* Cloud-native deployment
* Tool orchestration (MCP-style design)
* Practical AI system architecture

👉 This is **industry-level project work**, not just a demo.
