# AI Tool-Calling Chatbot (FastAPI + MongoDB + Docker)

This project is a **production‑ready AI chatbot backend** built using **FastAPI**, **MongoDB**, **Docker**, and **OpenAI Tool Calling**.
It intelligently understands user intent and automatically fetches **Sales** or **Admin** data from MongoDB without requiring the user to explicitly mention commands.

---

## 🚀 Features

* 🔹 FastAPI backend (high‑performance, async)
* 🔹 OpenAI **Tool Calling** (intent detection + structured arguments)
* 🔹 MongoDB for persistent storage
* 🔹 Chat history stored per session
* 🔹 Docker & Docker‑Compose based setup (one command run)
* 🔹 Clean project structure (agents, tools, services, db)
* 🔹 Works without repeated prompt instructions

---

## 🧠 How It Works (High‑Level Flow)

1. User sends a message to `/chat`
2. LLM decides **which tool is required** (sales/admin)
3. Backend executes MongoDB query
4. Data is sent back to LLM
5. Final natural‑language response is returned
6. Chat history is saved in MongoDB

---

## 📂 Project Structure

```
ai-tool-calling-chatbot/
│
├── app/
│   ├── main.py                 # FastAPI entry point
│   │
│   ├── chatbot/
│   │   ├── agent.py            # Tool calling + orchestration logic
│   │   ├── tools.py            # Tool schemas (OpenAI format)
│   │   └── prompts.py          # System prompt
│   │
│   ├── services/
│   │   └── openai_service.py   # OpenAI API wrapper
│   │
│   ├── db/
│   │   └── mongo.py            # MongoDB connection + collections
│   │
│   └── data/                   # JSON seed data (sales/admin)
│
├── docker/
│   └── mongo-init/
│       └── init.js             # MongoDB initialization script
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## 🐳 Docker Setup (Recommended)

### 1️⃣ Prerequisites

* Docker
* Docker Compose

---

### 2️⃣ Environment Variables (`.env`)

```
OPENAI_API_KEY=your_openai_key_here
MONGO_URI=mongodb://mongo:27017/company_db
```

---

### 3️⃣ Build & Run Containers

```bash
docker compose up --build
```

Services started:

* FastAPI → `http://localhost:8000`
* MongoDB → `mongodb://localhost:27017`

---

## 🔌 API Endpoints

### 🔹 Chat API

**POST** `/chat`

```json
{
  "message": "Get sales data for customer 101",
  "session_id": "session_123"
}
```

---

### 🔹 Chat History API

**GET** `/history/{session_id}`

```http
GET /history/session_123
```

Returns full conversation for that session.

---

## 🗄️ MongoDB Collections

| Collection     | Purpose                      |
| -------------- | ---------------------------- |
| `sales`        | Sales/customer data          |
| `admin`        | Admin credentials & metadata |
| `chat_history` | Conversation logs            |

---

## 🧪 Example Prompt Behavior

| User Input       | System Action        |
| ---------------- | -------------------- |
| "Get sales data" | Asks for customer ID |
| "Customer 101"   | Fetches sales data   |
| "Get admin data" | Fetches admin info   |

No hard‑coded commands required.

---

## 🛡️ Best Practices Used

* Tool calling instead of prompt hacking
* Clear separation of concerns
* DB‑level persistence for chats
* Dockerized for portability

---

## 💼 Interview‑Ready Explanation

> "This system uses OpenAI function calling to dynamically select backend tools, fetch structured data from MongoDB, and maintain conversation state across sessions using persistent storage."

---

## 📌 Future Enhancements

* Pagination for chat history
* Authentication (JWT)
* Role‑based admin access
* Streaming responses

---

## 👨‍💻 Author

**Saksham Tyagi**

If this project helped you, consider starring the repo!
