# 🍿 IMDB-Buddy-AI (MCP Server)

[![MCP Version](https://img.shields.io/badge/MCP-1.0.0-blue)](https://modelcontextprotocol.io/)
[![Python Version](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**IMDB Buddy-AI** is a high-performance [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that bridges the gap between AI assistants and **The Movie Database (TMDB)**. 

By integrating this server, your AI assistant gains real-time "vision" into the cinematic world—moving beyond static training data to access live ratings, global releases, and detailed metadata.

---

## ✨ Features

- **🎯 Precision Filtering**: Find content by specific ratings (e.g., "7.5+ only") or popularity.
- **🌍 Global Reach**: Full support for ISO language codes (Hindi, Spanish, French, etc.).
- **📺 Dual Media Support**: Seamlessly switch between **Movies** and **TV/Web Series**.
- **🧠 Semantic Genre Mapping**: Maps natural language (e.g., "Action", "Sci-Fi") to internal API IDs automatically.
- **📄 Rich Metadata**: Delivers plot summaries, release years, and vote counts for grounded AI reasoning.

---

## 🚀 Installation & Setup

### 1. Prerequisites
- **Python 3.10+**
- **TMDB API Key**: [Get a free key here](https://www.themoviedb.org/settings/api).
- **Claude Desktop** (or any MCP-compatible client like Cursor or Windsurf).

### 2. Local Setup
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/IMDB Buddy-AI-AI.git](https://github.com/YOUR_USERNAME/IMDB Buddy-AI.git)
cd FlixSearch-AI

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt