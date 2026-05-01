# 🛠️ Detailed Installation Guide for Ninja-Researchers

This guide provides step-by-step instructions for installing and running Ninja-Researchers on different platforms.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Installation](#quick-installation)
3. [Platform-Specific Guide](#platform-specific-guide)
4. [Configuration](#configuration)
5. [Troubleshooting](#troubleshooting)
6. [Docker Setup](#docker-setup)
7. [Cloud Deployment](#cloud-deployment)

---

## ✅ Prerequisites

### System Requirements

- **RAM**: Minimum 4GB (8GB+ recommended)
- **Storage**: 2GB minimum for cache and papers
- **CPU**: Multi-core processor for better performance
- **Internet**: Required for API access

### Software Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version (for package management)
- **Git**: For cloning repository (optional)

### Optional Requirements

- **Docker**: For containerized deployment
- **CUDA**: For GPU acceleration (optional)
- **PostgreSQL**: For production database (optional)

---

## 🚀 Quick Installation

### 1. Clone Repository

```bash
# Using Git
git clone https://github.com/yourusername/Ninja-Researchers.git
cd Ninja-Researchers

# Or download ZIP
# https://github.com/yourusername/Ninja-Researchers/archive/refs/heads/main.zip
# Then extract and navigate to folder
```

### 2. Create Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Configuration

```bash
# Copy example to .env
cp .env.example .env

# Edit .env file with your API keys
# Windows:
notepad .env
# Linux/Mac:
nano .env
```

### 5. Run Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## 🖥️ Platform-Specific Guide

### Windows Installation

#### Step 1: Install Python

1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. **Important**: Check "Add Python to PATH"
4. Click "Install Now"

Verify installation:

```cmd
python --version
pip --version
```

#### Step 2: Clone Repository

Option A: Using Git

```cmd
git clone https://github.com/yourusername/Ninja-Researchers.git
cd Ninja-Researchers
```

Option B: Using PowerShell

```powershell
# If Git is not installed, use direct download
cd Downloads
# Download from GitHub
# Extract ZIP folder
cd Ninja-Researchers-main
```

#### Step 3: Create Virtual Environment

```cmd
# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate

# Verify activation (should show (venv) prefix)
```

#### Step 4: Install Dependencies

```cmd
# Upgrade pip (important for Windows)
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installation
python -c "import langchain, chromadb, streamlit; print('✅ All dependencies OK')"
```

#### Step 5: Configure Environment

```cmd
# Copy .env.example to .env
copy .env.example .env

# Open in notepad
notepad .env

# Edit with your API keys:
# - GROQ_API_KEY (get from https://console.groq.com)
# - OPENAI_API_KEY (optional)
```

#### Step 6: Initialize Database

```cmd
# Create directories
mkdir data\cache
mkdir data\papers
mkdir data\reports

# Initialize ChromaDB
python utils/database.py --init
```

#### Step 7: Run Application

```cmd
# Run Streamlit app
streamlit run app.py

# Browser should open automatically
# If not, visit: http://localhost:8501
```

---

### Linux Installation

#### Ubuntu/Debian

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3 python3-pip python3-venv git

# Verify installation
python3 --version
pip3 --version

# Clone repository
git clone https://github.com/yourusername/Ninja-Researchers.git
cd Ninja-Researchers

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy and edit configuration
cp .env.example .env
nano .env

# Create data directories
mkdir -p data/{cache,papers,reports}

# Run application
streamlit run app.py
```

#### Fedora/RedHat

```bash
# Install dependencies
sudo dnf install -y python3 python3-pip python3-venv git

# Follow same steps as Ubuntu above
```

#### Arch Linux

```bash
# Install dependencies
sudo pacman -S python python-pip git

# Follow same steps as Ubuntu above
```

---

### macOS Installation

#### Using Homebrew (Recommended)

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.10

# Verify installation
python3 --version
pip3 --version

# Clone repository
git clone https://github.com/yourusername/Ninja-Researchers.git
cd Ninja-Researchers

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy configuration
cp .env.example .env
nano .env

# Create directories
mkdir -p data/{cache,papers,reports}

# Run application
streamlit run app.py
```

#### Using MacPorts

```bash
# Install Python via MacPorts
sudo port install python310

# Follow similar steps as Homebrew approach
```

---

## ⚙️ Configuration

### Environment Variables

Create `.env` file from `.env.example`:

```env
# Required
GROQ_API_KEY=your_groq_api_key

# Optional but recommended
OPENAI_API_KEY=your_openai_api_key

# Database
VECTOR_DB_TYPE=chromadb
DB_PATH=./data/chroma_db/

# Models
EMBEDDING_MODEL=all-MiniLM-L6-v2
MAX_PAPERS=50

# Logging
LOG_LEVEL=INFO
DEBUG_MODE=false
```

### API Keys Setup

#### Getting Groq API Key (Free, Recommended)

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up with email/GitHub
3. Navigate to API Keys
4. Generate new API key
5. Copy to `.env` file

#### Getting OpenAI API Key

1. Visit [platform.openai.com](https://platform.openai.com/api-keys)
2. Sign up/Login
3. Go to API Keys section
4. Create new secret key
5. Copy to `.env` file

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. Python Not Found

**Error**: `python: command not found`

**Solution**:

- Verify Python installation: `python --version`
- On Linux/Mac, try `python3` instead of `python`
- Add Python to PATH (Windows):
  - Settings → System → Environment Variables
  - Add Python installation directory to PATH

#### 2. Virtual Environment Activation Failed

**Error**: `activate: command not found` or `Access Denied`

**Solution**:

```bash
# Windows - Use full path
.\venv\Scripts\activate

# Linux/Mac - Use source
source venv/bin/activate

# Verify activation (should show (venv) prefix)
```

#### 3. pip Permission Denied

**Error**: `Permission denied: pip`

**Solution**:

```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use sudo (not recommended)
sudo pip install -r requirements.txt
```

#### 4. Module Not Found

**Error**: `ModuleNotFoundError: No module named 'langchain'`

**Solution**:

```bash
# Verify virtual environment is activated
which python  # Should show venv path

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

#### 5. API Key Not Working

**Error**: `AuthenticationError` or `API key invalid`

**Solution**:

- Verify `.env` file exists in project root
- Check API key is correct (no spaces/trailing chars)
- Test API key directly:

```python
from langchain_groq import ChatGroq
llm = ChatGroq(api_key="your_key")
print(llm.invoke("test"))
```

#### 6. Port Already in Use

**Error**: `Port 8501 is already in use`

**Solution**:

```bash
# Run on different port
streamlit run app.py --server.port 8502

# Or kill process using port
# Windows:
netstat -ano | findstr :8501
taskkill /PID [PID] /F

# Linux/Mac:
lsof -i :8501
kill -9 [PID]
```

#### 7. ChromaDB Connection Error

**Error**: `Failed to connect to ChromaDB`

**Solution**:

```bash
# Create data directory
mkdir -p data/chroma_db

# Initialize database
python utils/database.py --init

# Check permissions
ls -la data/chroma_db/
```

#### 8. Memory Issues

**Error**: `MemoryError` or `Out of memory`

**Solution**:

- Reduce MAX_PAPERS in `.env`
- Disable GPU acceleration if enabled
- Clear cache: `rm -rf data/cache/*`

---

## 🐳 Docker Setup

### Prerequisites

- Install [Docker](https://docs.docker.com/install/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

### Quick Docker Start

```bash
# Build image
docker build -t ninja-researchers .

# Run container
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_key \
  -v $(pwd)/data:/app/data \
  ninja-researchers

# Or with docker-compose
docker-compose up
```

### Docker Compose File

```yaml
version: "3.8"

services:
  ninja-researchers:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - VECTOR_DB_TYPE=chromadb
      - DB_PATH=/app/data/chroma_db
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

---

## ☁️ Cloud Deployment

### AWS Deployment

```bash
# Create EC2 instance
# Then SSH into instance and follow Linux instructions above

# Or use AWS ECS with Docker container
```

### Azure Deployment

```bash
# Using Azure Container Instances
az container create \
  --resource-group myResourceGroup \
  --name ninja-researchers \
  --image ninja-researchers:latest \
  --environment-variables \
    GROQ_API_KEY=your_key \
  --ports 8501
```

### Google Cloud Deployment

```bash
# Using Cloud Run
gcloud run deploy ninja-researchers \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars GROQ_API_KEY=your_key
```

---

## ✅ Verification

After installation, verify everything works:

```python
# test_installation.py
import sys
print("Python:", sys.version)

try:
    import langchain
    print("✅ LangChain installed")
except ImportError:
    print("❌ LangChain not installed")

try:
    import chromadb
    print("✅ ChromaDB installed")
except ImportError:
    print("❌ ChromaDB not installed")

try:
    import streamlit
    print("✅ Streamlit installed")
except ImportError:
    print("❌ Streamlit not installed")

try:
    import sentence_transformers
    print("✅ Sentence Transformers installed")
except ImportError:
    print("❌ Sentence Transformers not installed")

print("\n🎉 Installation verification complete!")
```

Run with:

```bash
python test_installation.py
```

---

## 📞 Need Help?

- 📖 [Documentation](https://github.com/yourusername/Ninja-Researchers/wiki)
- 🐛 [Report Issues](https://github.com/yourusername/Ninja-Researchers/issues)
- 💬 [Discussions](https://github.com/yourusername/Ninja-Researchers/discussions)
- 📧 Email: your.email@example.com

---

<div align="center">

**Installation Guide Complete! 🎉**

[Back to README](README.md)

</div>
