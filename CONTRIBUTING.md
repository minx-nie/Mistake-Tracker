# Contributing to Mistake Tracker

Thank you for your interest in contributing! 🎉

## 🚀 Getting Started

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Mistake-Tracker.git
   cd Mistake-Tracker
   ```
3. **Install** development dependencies:
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

## 📝 Development Workflow

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make your changes and ensure:
   - ✅ Tests pass: `pytest tests/ -v`
   - ✅ Linting passes: `ruff check .`
   - ✅ Types check: `mypy src/`

3. Commit with a descriptive message:
   ```bash
   git commit -m "feat: add your feature"
   ```

4. Push and create a Pull Request

## 📋 Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `test:` Tests
- `chore:` Maintenance

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=mistake_tracker
```

## 💡 Questions?

Open an [issue](https://github.com/ThanhNguyxn/Mistake-Tracker/issues)!
