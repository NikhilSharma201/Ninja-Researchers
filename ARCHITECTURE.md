# 🏗️ Architecture Documentation

Comprehensive guide to Ninja-Researchers system architecture, design patterns, and component interactions.

---

## 📑 Table of Contents

1. [System Overview](#system-overview)
2. [Component Architecture](#component-architecture)
3. [Data Flow](#data-flow)
4. [Agent Design](#agent-design)
5. [Database Layer](#database-layer)
6. [API Integrations](#api-integrations)
7. [Performance Considerations](#performance-considerations)
8. [Security Architecture](#security-architecture)

---

## 🎯 System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        APPLICATION LAYER                    │
│                    (Streamlit Web Interface)                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                      │
│                   (LangChain Agent Controller)              │
└──────┬──────────────────┬──────────────────┬────────────────┘
       │                  │                  │
       ▼                  ▼                  ▼
┌────────────┐    ┌────────────┐    ┌──────────────┐
│ Retrieval  │    │Summarization│    │  Reasoning  │
│   Agent    │    │   Agent    │    │   Agent     │
└────┬───────┘    └────┬───────┘    └──────┬───────┘
     │                 │                   │
     ▼                 ▼                   ▼
┌─────────────────────────────────────────────────────┐
│            PROCESSING LAYER                        │
│  (Data Extraction, Embedding, Analysis)           │
└──────┬──────────────────┬───────────────┬──────────┘
       │                  │               │
       ▼                  ▼               ▼
┌────────────┐    ┌────────────┐    ┌──────────────┐
│   External │    │  Vector DB │    │  Local Cache│
│    APIs    │    │ (ChromaDB) │    │  (Memory)   │
└────────────┘    └────────────┘    └──────────────┘
```

---

## 🔧 Component Architecture

### 1. Streamlit Interface Layer

**Purpose**: User-facing web interface

**Components**:

```python
app.py
├── Search Interface
├── Results Display
├── Configuration Panel
├── Report Builder
└── Export Options
```

**Key Features**:

- Single-page application
- Real-time query processing
- Interactive data visualization
- Report generation UI

**Technology**: Streamlit 1.28+

---

### 2. Agent Orchestration Layer

**Purpose**: Coordinate multiple specialized agents

**Architecture**:

```python
agents/
├── orchestrator.py          # Main controller
├── agent1.py               # Retrieval Agent
├── agent2.py               # Summarization Agent
├── agent3.py               # Reasoning Agent
└── devil_advocate.py       # Adversarial Agent
```

**Design Pattern**: **Chain of Responsibility**

- Each agent handles specific tasks
- Results pass to next agent
- Orchestrator manages flow

**Agent Structure**:

```python
class SpecializedAgent:
    def __init__(self, llm=None, tools=None):
        self.llm = llm
        self.tools = tools

    def run(self, input_data):
        # Process input
        # Use tools
        # Return output
        pass
```

---

### 3. Processing Layer

**Purpose**: Extract, transform, and enhance data

**Components**:

#### 3.1 Retrieval Module

```
Query → Query Enhancement → API Requests → Result Aggregation
         ↓                    ↓
    Synonym Expansion    Multi-source Search
                              ↓
                        Deduplication
```

#### 3.2 Embedding Module

```
Text Data → Tokenization → Embedding Model → Vectors
                              ↓
                        Normalization → Vector Store
```

#### 3.3 Analysis Module

```
Summaries → Claim Extraction → Relationship Analysis
                ↓                    ↓
           Confidence Scoring   Gap Detection
                                    ↓
                           Contradiction Detection
```

---

### 4. Data Layer

**Technology Stack**:

- **Primary**: ChromaDB (vector store)
- **Secondary**: FAISS (optional, for scale)
- **Metadata**: JSON files / SQLite

**Data Model**:

```python
class PaperDocument:
    id: str                 # Unique identifier
    title: str
    authors: List[str]
    abstract: str
    full_text: str
    url: str
    source: str             # arxiv, pubmed, semantic_scholar
    embedding: List[float]  # Vector representation
    metadata: Dict
    retrieved_at: datetime
    cached: bool
```

---

## 📊 Data Flow

### Query Processing Pipeline

```
1. USER INPUT
   ↓
   "Machine Learning in Healthcare"

2. INPUT VALIDATION
   ├─ Syntax check
   ├─ Language detection
   └─ Tokenization

3. QUERY ENHANCEMENT
   ├─ Synonym expansion
   ├─ Related term inclusion
   └─ Semantic enrichment

4. CACHE CHECK
   ├─ Vector embedding of enhanced query
   ├─ ChromaDB semantic search
   └─ If cache hit → Skip API calls

5. MULTI-SOURCE RETRIEVAL
   ├─ arXiv API call
   ├─ PubMed API call
   ├─ Semantic Scholar API call
   └─ Parallel execution

6. RESULT AGGREGATION
   ├─ Deduplication
   ├─ Relevance scoring
   ├─ Result ranking
   └─ Top N selection

7. TEXT EXTRACTION
   ├─ PDF parsing
   ├─ Metadata extraction
   ├─ Text normalization
   └─ Quality filtering

8. EMBEDDING GENERATION
   ├─ Batch processing
   ├─ Sentence Transformers
   ├─ Vector normalization
   └─ Store in ChromaDB

9. SUMMARIZATION
   ├─ Key claim extraction
   ├─ Methodology identification
   ├─ Result extraction
   └─ Confidence scoring

10. ANALYSIS & REASONING
    ├─ Cross-reference analysis
    ├─ Contradiction detection
    ├─ Gap identification
    └─ Relationship mapping

11. DEVIL'S ADVOCATE
    ├─ Assumption challenge
    ├─ Alternative interpretation
    ├─ Bias identification
    └─ Counter-evidence suggestion

12. REPORT GENERATION
    ├─ Structure assembly
    ├─ Citation formatting
    ├─ Visualization creation
    └─ Export formatting

13. OUTPUT
    ├─ Markdown report
    ├─ PDF export
    ├─ JSON data
    └─ Visualizations
```

---

## 🤖 Agent Design Patterns

### Agent 1: Retrieval Agent

**Responsibility**: Find relevant academic papers

**Tools**:

- arXiv API
- PubMed API
- Semantic Scholar API
- Web scraping

**Algorithm**:

```
1. Parse user query
2. Expand query with synonyms
3. Execute parallel API calls
4. Aggregate results
5. Remove duplicates
6. Score by relevance
7. Return top papers
```

**LLM Prompt**:

```
You are an expert research paper finder.
Given a research topic, find the most relevant
academic papers from multiple sources.
Rank by relevance and recency.
```

### Agent 2: Summarization Agent

**Responsibility**: Extract key information from papers

**Process**:

```
1. Extract abstract
2. Parse full text
3. Identify key claims
4. Extract methodology
5. Extract findings
6. Assign confidence scores
7. Format as structured data
```

**Output Format**:

```json
{
  "paper_id": "arxiv:2023.12345",
  "key_claims": [
    {
      "claim": "...",
      "confidence": "high",
      "evidence": "..."
    }
  ],
  "methodology": "...",
  "findings": "...",
  "limitations": "..."
}
```

### Agent 3: Reasoning Agent

**Responsibility**: Cross-reference and analyze papers

**Analysis Types**:

- **Contradiction Detection**: Find conflicting claims
- **Confidence Scoring**: Assign reliability metrics
- **Gap Analysis**: Identify research opportunities
- **Relationship Mapping**: Connect concepts

**Algorithms**:

```
# Contradiction Detection
1. Extract claims from all papers
2. Vectorize claims (embeddings)
3. Compute similarity scores
4. Flag contradictions (low similarity + opposite meaning)
5. Assign confidence levels

# Gap Analysis
1. Identify research areas
2. Check coverage across time
3. Count papers per area
4. Identify sparse areas
5. Suggest unexplored directions
```

### Agent 4: Devil's Advocate Agent

**Responsibility**: Challenge and validate findings

**Functions**:

- Question assumptions
- Propose alternatives
- Identify biases
- Suggest counter-evidence

**Questions Asked**:

```
- What if the opposite were true?
- What evidence contradicts this?
- What assumptions are unstated?
- What's the worst-case interpretation?
- What methodological flaws exist?
```

---

## 💾 Database Layer

### ChromaDB Architecture

```
┌─────────────────────────────────────┐
│       Persistent Storage            │
│  (data/chroma_db/collections/)     │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│     ChromaDB Collections            │
│  ├─ papers                          │
│  ├─ summaries                       │
│  └─ embeddings                      │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│     Metadata Storage                │
│  ├─ Document IDs                    │
│  ├─ Metadata (source, date, etc)    │
│  ├─ Embedding vectors               │
│  └─ Distance indices                │
└─────────────────────────────────────┘
```

### Query Optimization

**Indexing Strategy**:

```
Primary Index: Source + Year + Title (compound)
Full-Text Index: Abstract + Keywords
Vector Index: Embedding vectors (HNSW algorithm)
```

**Query Execution**:

```
SELECT * FROM papers
WHERE vector_similarity(query_embedding, paper_embedding) > 0.7
ORDER BY relevance_score DESC
LIMIT 50
```

---

## 🔌 API Integrations

### Retrieval APIs

#### arXiv API

```
Endpoint: https://arxiv.org/api/query
Method: GET
Params: search_query, max_results, sort_by
Rate Limit: 3 req/sec (implicit)
```

#### PubMed API

```
Endpoint: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi
Method: GET
Params: term, retmax, sort
Rate Limit: 3 req/sec
```

#### Semantic Scholar API

```
Endpoint: https://api.semanticscholar.org/v1/paper/search
Method: GET
Params: query, limit, offset
Rate Limit: 100 req/5min
```

### LLM APIs

#### Groq (Recommended)

```
Endpoint: https://api.groq.com/openai/v1/chat/completions
Model: mixtral-8x7b-32768
Speed: Very fast
Cost: Free tier available
```

#### OpenAI (Alternative)

```
Endpoint: https://api.openai.com/v1/chat/completions
Model: gpt-4, gpt-3.5-turbo
Speed: Standard
Cost: Paid, usage-based
```

---

## ⚡ Performance Considerations

### Optimization Strategies

#### 1. Caching

**Three-Level Cache**:

```
L1: In-Memory Cache        (session-level, fast)
L2: ChromaDB Vector Cache  (persistent, medium)
L3: API Response Cache     (last 24h, slow)
```

**Cache Hit Time**: < 50ms
**Cache Miss Time**: 8-12s (cold) → 200ms (warm)

#### 2. Batch Processing

```python
# Efficient embedding generation
embeddings = model.encode(texts, batch_size=32)  # vs batch_size=1

# Parallel API calls
async def fetch_from_apis():
    responses = await asyncio.gather(
        fetch_arxiv(),
        fetch_pubmed(),
        fetch_semantic_scholar()
    )
```

#### 3. Lazy Loading

```python
# Load only when needed
class PaperDocument:
    def __init__(self, metadata):
        self._full_text = None  # Not loaded yet

    @property
    def full_text(self):
        if self._full_text is None:
            self._load_full_text()
        return self._full_text
```

### Performance Metrics

| Operation | Cold Start | Cached  | Target |
| --------- | ---------- | ------- | ------ |
| Search    | 8-12s      | 200ms   | ✅     |
| Embedding | 5-8s       | instant | ✅     |
| Analysis  | 10-15s     | 2-3s    | ⚠️     |
| Report    | 15-20s     | 3-5s    | ✅     |

---

## 🔒 Security Architecture

### API Security

```
Request Flow:
Client → (.env) → API Key → API Endpoint → Response

Security:
- API keys stored locally only
- Environment variables (never commit)
- HTTPS for all API calls
- Request rate limiting
- Error masking (no exposes)
```

### Data Security

```
Principles:
- No external data transmission
- Local caching only
- User data isolation
- Input validation
- Output sanitization
```

### Error Handling

```python
class SecureErrorHandler:
    def handle_error(self, error):
        # Log internally
        log_error(error)

        # Return user-safe message
        if isinstance(error, APIError):
            return "Search temporarily unavailable"
        elif isinstance(error, ValidationError):
            return "Invalid input format"
        else:
            return "System error occurred"
```

---

## 🔄 Deployment Architecture

### Local Deployment

```
Machine → venv → pip install → .env → streamlit run
```

### Docker Deployment

```
Dockerfile → Docker Image → Container → Port 8501
```

### Cloud Deployment

```
GitHub → Docker Registry → Cloud Platform (AWS/Azure/GCP)
```

---

## 📈 Scalability Paths

### Current (Single Machine)

- Max ~1000 papers/session
- ~500 cached embeddings
- Single user

### Medium Scale (Docker/Compose)

- Multiple containers
- Load balancing
- Shared cache (Redis)
- ~5 concurrent users

### Enterprise Scale (Kubernetes)

- Auto-scaling
- Distributed database
- API gateway
- Monitoring & logging
- ~100+ concurrent users

---

## 🧪 Testing Architecture

```
Unit Tests (agents/)
    ↓
Integration Tests (workflows/)
    ↓
API Tests (external services/)
    ↓
Performance Tests (benchmarks/)
    ↓
E2E Tests (frontend/)
```

---

## 📚 Design Principles

1. **Separation of Concerns**
   - Each agent has single responsibility
   - Layers decouple cleanly
   - APIs well-defined

2. **Extensibility**
   - Easy to add new agents
   - Plugin architecture for APIs
   - Custom export formats

3. **Maintainability**
   - Clear code structure
   - Comprehensive logging
   - Good documentation

4. **Performance**
   - Caching at multiple levels
   - Async operations
   - Batch processing

5. **Security**
   - Local-first architecture
   - No data transmission
   - API key protection

---

<div align="center">

**Architecture Documentation Complete**

[Back to Main Documentation](README.md)

</div>
