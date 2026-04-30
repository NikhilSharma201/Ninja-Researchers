# Contributing to Ninja-Researchers

Thank you for your interest in contributing to Ninja-Researchers! This document provides guidelines and instructions for contributing to the project.

## 🎯 Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read and abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 🚀 How to Contribute

### 1. **Report Issues**

Found a bug? Have a feature request? Please create an issue:

1. Go to [Issues](https://github.com/yourusername/Ninja-Researchers/issues)
2. Check if issue already exists
3. Click "New Issue"
4. Provide:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment info (Python version, OS, etc.)
   - Relevant logs or screenshots

### 2. **Suggest Features**

Use GitHub Issues with the `enhancement` label:

- Describe the feature and why it's needed
- Provide use cases or examples
- Link to related issues or discussions

### 3. **Submit Pull Requests**

#### Step 1: Fork & Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Ninja-Researchers.git
cd Ninja-Researchers
git remote add upstream https://github.com/ORIGINAL_OWNER/Ninja-Researchers.git
```

#### Step 2: Create Feature Branch

```bash
# Create a new branch for your changes
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b bugfix/issue-description
```

#### Step 3: Make Your Changes

- Write clean, readable code
- Follow [Python Style Guide (PEP 8)](https://pep8.org/)
- Add comments for complex logic
- Update tests and documentation

#### Step 4: Test Your Changes

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Run tests
pytest tests/ -v --cov=agents --cov=utils

# Check code style
black --check .
```

#### Step 5: Commit & Push

```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "feat: add your feature description"
# or
git commit -m "fix: resolve issue with..."

# Push to your fork
git push origin feature/your-feature-name
```

#### Step 6: Create Pull Request

1. Go to the original repository
2. Click "New Pull Request"
3. Select your branch
4. Fill in PR template:
   - Description of changes
   - Related issues (closes #XXX)
   - Testing instructions
   - Screenshots (if applicable)

---

## 📝 Commit Message Guidelines

**Format:**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding/updating tests

**Examples:**

```
feat(retrieval): add semantic scholar integration
fix(database): resolve ChromaDB connection timeout
docs(readme): update installation instructions
test(agent): add unit tests for summarization agent
```

---

## 🏗️ Project Structure Guidelines

### Adding New Features

**Agents:**

```python
# agents/your_new_agent.py
from langchain.agents import Tool
from langchain_groq import ChatGroq

class YourNewAgent:
    def __init__(self, llm=None):
        self.llm = llm or ChatGroq(model_name="mixtral-8x7b-32768")

    def run(self, input_data):
        """Main agent logic"""
        pass
```

**Utilities:**

```python
# utils/your_new_utility.py
def utility_function():
    """Docstring describing function"""
    pass
```

**Tests:**

```python
# tests/test_your_new_feature.py
import pytest
from agents.your_new_agent import YourNewAgent

def test_agent_initialization():
    agent = YourNewAgent()
    assert agent is not None
```

---

## 🧪 Testing Requirements

- **Coverage**: Minimum 80% code coverage
- **Unit Tests**: All functions should have tests
- **Integration Tests**: Test agent interactions
- **Edge Cases**: Test error handling and edge cases

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agents.py -v

# Run with coverage
pytest --cov=agents --cov=utils --cov-report=html

# Run only failed tests
pytest --lf
```

---

## 📚 Documentation Guidelines

### Code Comments

```python
def complex_function(param1, param2):
    """
    One-line description.

    Longer description explaining what the function does,
    why it's useful, and any important details.

    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2

    Returns:
        dict: Description of return structure

    Raises:
        ValueError: When param1 is invalid

    Example:
        >>> result = complex_function("test", 42)
        >>> print(result)
    """
    pass
```

### Update Documentation

- **README.md**: For user-facing changes
- **docs/**: For detailed documentation
- **CHANGELOG.md**: For version history

---

## 🔍 Code Review Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] Tests pass locally (`pytest`)
- [ ] Code coverage maintained (>80%)
- [ ] Docstrings added for all functions
- [ ] No debug print statements left
- [ ] No credentials committed
- [ ] PR description is clear
- [ ] Related issues are linked
- [ ] CHANGELOG.md updated (if needed)

---

## 🐛 Bug Report Template

```markdown
## Description

Brief description of the bug.

## Steps to Reproduce

1. Step one
2. Step two
3. ...

## Expected Behavior

What should happen?

## Actual Behavior

What actually happened?

## Environment

- Python Version: 3.x.x
- OS: Windows/Linux/Mac
- Installed Packages: (output of pip list)

## Logs

<details>
<summary>Error logs</summary>
```

Paste error/log here

```

</details>

## Additional Info
Screenshots, relevant code snippets, etc.
```

---

## 🎨 Feature Request Template

```markdown
## Description

Clear description of the requested feature.

## Motivation

Why is this feature needed? What problem does it solve?

## Proposed Solution

Your suggested implementation (if any).

## Alternatives

Other solutions you've considered.

## Additional Context

Screenshots, mockups, or references.
```

---

## 📦 Development Dependencies

Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

**Included:**

- `pytest` - Testing framework
- `pytest-cov` - Coverage reports
- `black` - Code formatter
- `flake8` - Linting
- `mypy` - Type checking
- `sphinx` - Documentation generation

---

## 🤖 Continuous Integration

All PRs must pass:

- ✅ Tests (pytest)
- ✅ Linting (flake8)
- ✅ Code formatting (black)
- ✅ Type checking (mypy)
- ✅ Code coverage (>80%)

---

## 📊 Areas for Contribution

### High Priority

- [ ] Improve documentation
- [ ] Add more test coverage
- [ ] Optimize performance
- [ ] Add error handling

### Medium Priority

- [ ] New agent types
- [ ] Additional data sources
- [ ] Export format support
- [ ] Advanced filtering

### Nice to Have

- [ ] UI improvements
- [ ] Dark mode
- [ ] Export to more formats
- [ ] Performance optimizations

---

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Python Best Practices](https://pep8.org/)

---

## 💬 Questions?

- 📖 Check existing [Documentation](https://github.com/yourusername/Ninja-Researchers/wiki)
- 💭 Start a [Discussion](https://github.com/yourusername/Ninja-Researchers/discussions)
- 📧 Email: your.email@example.com
- 🐞 Report [Issues](https://github.com/yourusername/Ninja-Researchers/issues)

---

## ⭐ Recognition

Contributors will be:

- Listed in [CONTRIBUTORS.md](CONTRIBUTORS.md)
- Credited in release notes
- Highlighted on project page

---

## 📝 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

<div align="center">

**Thank you for contributing to Ninja-Researchers! 🙏**

</div>
