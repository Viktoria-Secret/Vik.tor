<<<<<<< HEAD
# Vik.tor Project - Captive Portal + AI Assistant for Ship Network Access

## 🚀 Mission
"Vik.tor" is a hybrid system designed to manage internet access on a commercial ship via a Captive Portal and integrate an AI assistant to help crew members troubleshoot onboard equipment using PDF documentation and GPT models. The system is built to be **offline-first**, with seamless switching between online (Starlink) and offline (cached logic).

---

## 📁 Project Structure
```
vik.tor/
├── backend/            # FastAPI logic for PIN handling and device authorization
├── frontend/           # Next.js-based UI for PIN entry, job selection, and portal interface
├── .env                # Environment config (API keys, URLs)
├── docker-compose.yml  # Docker orchestration for backend, frontend, n8n
├── .cursor/mcp.json    # MCP configuration for LLMs in Cursor (Claude, GPT o3, etc.)
└── README.md           # This file
```

---

## 🤖 Features
- **Captive Portal**: Auth page via PIN, with support for:
  - Temporary (time-based) PINs
  - Persistent PINs by crew rank
  - 3 device limit per PIN (MAC binding)
  - Pause/resume access (green/red indicator)
- **Admin Panel (future)**: Voucher generation, session logs, user management
- **AI Assistant**: Embedded Chat UI (WIP)
  - Upload PDF manuals (scanned or text)
  - Ask in plain English/Ukrainian/Russian
  - See highlighted answer and matching PDF excerpts
- **LLM Integration (MCP)**:
  - Claude 3.5 (Sonnet) / GPT o3 via Cursor Agent
  - Full tool invocation via MCP

---

## ⚖️ Stack
| Part       | Tech                    |
|------------|-------------------------|
| Backend    | Python + FastAPI        |
| Frontend   | Next.js + Tailwind      |
| Proxy/Auth | MikroTik + Captive Portal|
| AI Layer   | Cursor + Claude o3      |
| Workflow   | n8n (Docker container)  |
| Deployment | Docker + Vercel (future)|

---

## 🛠️ Setup Instructions (Local Dev)

### 1. Clone the repo
```bash
git clone https://github.com/your-username/vik.tor.git
cd vik.tor
```

### 2. Configure environment
Create `.env` file:
```
VIKTOR_API_KEY=your_secret_key
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Create MCP config for Cursor
Make `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "openai-o3": {
      "uri": "https://mcp.openai.com",
      "apiKey": "sk-...",
      "model": "o3"
    }
  }
}
```

### 4. Run Docker services
```bash
docker compose up --build -d
```
This will launch:
- FastAPI backend (port 8000)
- Next.js frontend (port 3000)
- n8n workflow engine (port 5678)

### 5. Open in browser
- Frontend: [http://localhost:3000](http://localhost:3000)
- API: [http://localhost:8000/docs](http://localhost:8000/docs)
- n8n: [http://localhost:5678](http://localhost:5678)

---

## 🧹 Use Cases
- Ship crew connect via Wi-Fi and are redirected to `vik.tor` portal.
- Enter rank → receive PIN (if valid)
- PIN used to unlock access for up to 3 devices (MAC bound)
- User can pause/resume time-based access (10h, 100h, etc.)
- In offline mode, AI gives cached suggestions (future feature)
- In online mode, AI uses LLM (Claude o3 / GPT-4o) to answer PDF-based queries

---

## 🦄 MCP Integration (Cursor)
- Cursor > Settings > MCP
- Add `.cursor/mcp.json`
- Restart Cursor
- Confirm that "openai-o3" is listed

Model should now be able to:
- Write/modify code in context
- Use local tools (planned)
- Respond to commands via chat + CLI

---

## 🌐 Planned Extensions
- Telegram Bot for PINs + control
- PayPal/Stripe/Google Pay PIN payment
- Auto/manual PDF tagging system
- GPT-powered log analysis (MikroTik)
- Integration with Starlink API

---

## 🚪 Security Notes
- Never expose `.env` or `mcp.json` in GitHub
- Use rate limiting in backend
- Add JWT or MAC+Token auth for device validation (future)

---

## ✨ Credits
- Built by Electro-technical Officer onboard container vessel
- Assisted by Cursor, Claude, and ChatGPT
- Inspired by the pain of limited internet at sea

---

> ✅ This README is your **anchor**. Keep it updated as we evolve.
> Ping your AI agent in Cursor and refer to this for full context.

---

=======
# Marine AI (Rudder Prototype)

Steps:
1. Add your API key to `.env.local`
2. Run `npm install`
3. Run `npm run dev`
>>>>>>> ee6a18651e63c26854fb9614e896cd62de921e6b
