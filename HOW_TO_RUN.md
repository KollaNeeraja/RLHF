# How to Run - RLHF PoC

Quick start guide for getting the RLHF Proof of Concept up and running.

## Prerequisites

- **Python 3.8+** installed
- **pip** package manager
- **Git** (optional, for cloning)

## Installation Steps

### 1. Navigate to Project Directory

```powershell
cd c:\Code_P1\rlhf-poc
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs:
- torch (1.10+)
- transformers (4.20+)
- numpy (1.21+)
- pytest (7.0+)
- jupyter (1.0+)

### 3. Install Package in Development Mode

```powershell
pip install -e .
```

This allows you to import the `src` modules from anywhere.

---

## Running Tests

Verify everything is working correctly by running the test suite:

```powershell
pytest tests/ -v
```

**Expected Output:**
- ✅ All 15 tests should pass
- Test execution time: ~5-10 seconds

### Run Specific Test Category

```powershell
# Test only PPO algorithm
pytest tests/test_components.py::TestPPO -v

# Test only reward modeling
pytest tests/test_components.py::TestRewardModel -v

# Test only safety
pytest tests/test_components.py::TestSafety -v

# Test only red teaming
pytest tests/test_components.py::TestRedTeaming -v

# Test only constitutional AI
pytest tests/test_components.py::TestConstitutionalAI -v
```

### Run with Coverage

```powershell
pytest tests/ -v --cov=src --cov-report=html
```

---

## Running Notebooks

### Start Jupyter Notebook Server

```powershell
jupyter notebook
```

This opens your browser at `http://localhost:8888`

### Run Notebooks in Order (Recommended)

1. **`notebooks/05_full_rlhf_pipeline.ipynb`** - Start here! Complete end-to-end pipeline
2. **`notebooks/01_ppo_training.ipynb`** - Deep dive into PPO algorithm
3. **`notebooks/02_reward_modeling.ipynb`** - Reward function learning from preferences
4. **`notebooks/03_red_teaming.ipynb`** - Adversarial attack generation and testing
5. **`notebooks/04_constitutional_ai.ipynb`** - Principle-based alignment

### Run Individual Notebook Cells

Within a notebook, use:
- **Shift+Enter** - Execute selected cell
- **Ctrl+Enter** - Execute cell and stay on it
- **Alt+Enter** - Execute cell and create new cell below

---

## Using the Components

### Quick Python Examples

#### 1. Train a PPO Policy

```python
from src.algorithms.policy_gradient import PPOTrainer, PPOConfig
import torch

# Create trainer
config = PPOConfig(learning_rate=3e-4, num_epochs=10)
trainer = PPOTrainer(state_dim=4, action_dim=2, config=config)

# Train on episodes (generate your own or use dummy data)
# ... training loop code ...

# Save checkpoint
trainer.save("ppo_checkpoint.pt")
```

#### 2. Learn Reward Model from Preferences

```python
from src.reward_modeling.preference_model import PreferenceRewardModel, Preference
import torch

# Create model
reward_model = PreferenceRewardModel(input_dim=4, hidden_dim=64)

# Create preferences (chosen > rejected)
preferences = [
    Preference(state=[1, 2, 3, 4], chosen_action=0, rejected_action=1, confidence=0.9),
    Preference(state=[2, 3, 4, 5], chosen_action=1, rejected_action=0, confidence=0.8),
]

# Train
reward_model.train_from_preferences(preferences, epochs=5)

# Predict
reward = reward_model.predict([1, 2, 3, 4], action=0)
```

#### 3. Check Safety

```python
from src.safety.safety_checker import SafetyChecker

checker = SafetyChecker()

# Check output
result = checker.check_safety("Hello, this is a safe response")
print(f"Safety score: {result.safety_score}")
print(f"Is safe: {result.is_safe}")
```

#### 4. Generate Adversarial Examples

```python
from src.red_teaming.adversarial_generator import AdversaryGenerator

adversary = AdversaryGenerator()

# Generate attacks
attacks = adversary.generate_attacks(num_attacks=5)
for attack in attacks:
    print(f"Attack: {attack.prompt}")
    print(f"Category: {attack.category}")
```

#### 5. Evaluate with Constitutional AI

```python
from src.constitutional_ai.constitution import ConstitutionalEvaluator

evaluator = ConstitutionalEvaluator()

# Evaluate output
output = "I will help you with that request"
evaluation = evaluator.evaluate_output(output)

print(f"Principles satisfied: {evaluation.passed_principles}")
print(f"Overall score: {evaluation.overall_score}")
```

---

## Project Structure Reference

```
rlhf-poc/
├── src/
│   ├── algorithms/               # PPO, TRPO implementations
│   ├── reward_modeling/          # Preference learning
│   ├── safety/                   # Safety checking & constraints
│   ├── red_teaming/              # Adversarial examples
│   ├── constitutional_ai/        # Principle-based alignment
│   └── utils/                    # Helper functions & metrics
├── tests/
│   └── test_components.py        # Unit tests (15+ tests)
├── notebooks/
│   ├── 01_ppo_training.ipynb
│   ├── 02_reward_modeling.ipynb
│   ├── 03_red_teaming.ipynb
│   ├── 04_constitutional_ai.ipynb
│   └── 05_full_rlhf_pipeline.ipynb
├── requirements.txt              # Python dependencies
├── setup.py                      # Package configuration
├── pytest.ini                    # Test configuration
├── README.md                     # Project overview
├── GETTING_STARTED.md            # Quick examples
├── HOW_TO_RUN.md                 # This file
└── ... (other documentation)
```

---

## Troubleshooting

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'src'`

**Solution**:
```powershell
pip install -e .
```

### PyTorch Installation Issues

**Problem**: `No module named 'torch'` or CUDA errors

**Solution** (CPU-only):
```powershell
pip install torch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### Jupyter Not Found

**Problem**: `jupyter: The term 'jupyter' is not recognized`

**Solution**:
```powershell
pip install jupyter ipykernel
```

### Test Failures

**Problem**: Some tests fail

**Solution**:
1. Verify all dependencies installed: `pip list`
2. Check Python version: `python --version` (should be 3.8+)
3. Re-install package: `pip install -e .`
4. Run tests again: `pytest tests/ -v`

---

## Advanced Usage

### Run with Debug Output

```powershell
# Verbose test output
pytest tests/ -v -s

# Show print statements during test execution
pytest tests/ --capture=no
```

### Generate Test Coverage Report

```powershell
pytest tests/ --cov=src --cov-report=html
# Opens: htmlcov/index.html
```

### Run Only Slow/Fast Tests

```powershell
# Run faster tests only (use -m "not slow" in pytest.ini)
pytest tests/ -m "not slow"
```

---

## Next Steps

1. **Read**: `GETTING_STARTED.md` for quick examples
2. **Run**: `pytest tests/ -v` to verify installation
3. **Explore**: `notebooks/05_full_rlhf_pipeline.ipynb` for complete pipeline
4. **Learn**: Read other notebooks for component details
5. **Extend**: See `DEVELOPMENT.md` for customization guide

---

## Getting Help

- **Component Reference**: `COMPONENT_REFERENCE.md`
- **Architecture Guide**: `ARCHITECTURE.md`
- **Development Guide**: `DEVELOPMENT.md`
- **Project Index**: `INDEX.md`

---

**Happy exploring! 🚀**
