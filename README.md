# MrLlama 🦙

A premium, minimalist, and high-performance local AI interface for [Ollama](https://ollama.ai/). Designed with a focus on simplicity, privacy, and smooth user experience.

![MrLlama Interface](https://raw.githubusercontent.com/yourusername/mrllama/main/screenshot.png) *(Note: Replace with your actual screenshot after uploading to GitHub)*

## ✨ Features

- **Minimalist & Clean UI**: Built with pure Vanilla CSS for a lightweight and "Apple-style" distraction-free interface.
- **Privacy First**: Everything runs on your machine. No telemetry, no external tracking, no cloud dependencies.
- **Smart Markdown Rendering**: Full support for bold text, lists, tables, and more.
- **Syntax Highlighting**: Beautiful code blocks with "Copy to Clipboard" functionality.
- **Dynamic Dark Mode**: Seamlessly switches between light and dark themes (persisted in local storage).
- **Smooth Streaming**: Real-time word-by-word generation with a robust line-buffer system.
- **CORS-Free Proxy**: Includes a lightweight Python server that eliminates common browser connection issues.

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have [Ollama](https://ollama.ai/) installed and running on your machine.

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/mrllama.git
cd mrllama
```

### 3. Run the Application

The interface requires a small proxy server to bypass browser CORS (Cross-Origin Resource Sharing) restrictions.

```bash
python3 server.py 3333
```

### 4. Open in Browser

Navigate to:
`http://127.0.0.1:3333`

## 🛠 Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript, CSS3
- **Markdown**: [marked.js](https://marked.js.org/)
- **Code Highlighting**: [highlight.js](https://highlightjs.org/)
- **Backend (Proxy)**: Python 3 (Standard library only)

## 💡 Why a Proxy Server?

Most browsers block direct requests from a website to a local API (like Ollama) for security reasons (CORS). While you can configure Ollama with `OLLAMA_ORIGINS="*"`, this can be technical and sometimes fails depending on the browser. 

The included `server.py` acts as a unified bridge, serving both the web interface and the API from the same "origin," making it **plug-and-play** on any browser.

## 📄 License

MIT License - feel free to use and modify for your own local AI projects!
