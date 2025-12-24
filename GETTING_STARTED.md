# RLHF PoC - Getting Started Guide

## Installation

1. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Run tests:**
   ```bash
   pytest tests/ -v
   ```

## Quick Examples

### 1. Train PPO Policy

```python
from src.algorithms.policy_gradient import PPOTrainer
import torch

trainer = PPOTrainer(input_dim=10, output_dim=4, hidden_dim=256)

# Generate dummy data
states = torch.randn(100, 10)
actions = torch.randint(0, 4, (100,))
rewards = torch.randn(100)
dones = torch.zeros(100)

# Train
losses = trainer.train_step(states, actions, rewards, dones, torch.randn(100))
print(f"Policy Loss: {losses['policy_loss']:.4f}")
```

### 2. Learn from Preferences

```python
from src.reward_modeling.preference_model import BradleyTerryModel

# Define preferences
preferences = [
    {"chosen": "response_A", "rejected": "response_B", "score": 1.0},
    {"chosen": "response_A", "rejected": "response_C", "score": 1.0},
]

# Fit model
model = BradleyTerryModel()
model.fit(preferences)

# Get rankings
ranking = model.get_ranking()
for response, ability in ranking:
    print(f"{response}: {ability:.4f}")
```

### 3. Check Safety

```python
from src.safety.safety_checker import SafetyChecker

checker = SafetyChecker()
result = checker.check_safety("This is a normal response")
print(f"Safe: {result['is_safe']}")
print(f"Score: {result['overall_safety_score']:.2f}")
```

### 4. Red-team Your Model

```python
from src.red_teaming.adversarial_generator import AdversaryGenerator

generator = AdversaryGenerator()
attacks = generator.generate_attacks("my_model", num_attacks=50)

print(f"Generated {len(attacks)} attacks")
for attack in attacks[:3]:
    print(f"- {attack.category}: {attack.prompt[:50]}...")
```

### 5. Constitutional Evaluation

```python
from src.constitutional_ai.constitution import Constitution, ConstitutionalEvaluator

constitution = Constitution()
evaluator = ConstitutionalEvaluator(constitution)

output = "I'll help you with that task"
result = evaluator.evaluate_detailed(output)

print(f"Overall Score: {result['overall_alignment_score']:.2f}")
for eval_result in result["principle_evaluations"]:
    print(f"- {eval_result['principle_name']}: {eval_result['alignment_score']:.2f}")
```

## Key Modules

### Algorithms (`src/algorithms/`)
- **PPOTrainer**: Proximal Policy Optimization
- **TRPOTrainer**: Trust Region Policy Optimization

### Reward Modeling (`src/reward_modeling/`)
- **PreferenceRewardModel**: Learn from pairwise preferences
- **BradleyTerryModel**: Classical ranking model
- **RankingModel**: Listwise ranking with neural networks

### Safety (`src/safety/`)
- **SafetyChecker**: Multi-layer safety evaluation
- **ToxicityDetector**: Detect harmful content
- **SafetyFilter**: Filter outputs by safety threshold
- **AlignmentGuard**: Check value alignment

### Red-teaming (`src/red_teaming/`)
- **AdversaryGenerator**: Generate diverse adversarial examples
- **PromptInjectionStrategy**: Injection attacks
- **SocialEngineeringStrategy**: Social engineering attacks
- **LogicExploitStrategy**: Logic-based attacks

### Constitutional AI (`src/constitutional_ai/`)
- **Constitution**: Define alignment principles
- **ConstitutionalEvaluator**: Evaluate against principles
- **SelfAlignmentSystem**: Iteratively improve outputs
- **CritiqueGenerator**: Generate principle-based critiques

## Next Steps

1. **Explore Notebooks**: Check `notebooks/` for detailed examples
2. **Run Tests**: `pytest tests/ -v`
3. **Customize**: Add your own principles, constraints, and attacks
4. **Integrate**: Use components in your own pipelines

## References

- **RLHF**: Christiano et al., "Deep Reinforcement Learning from Human Preferences"
- **PPO**: Schulman et al., "Proximal Policy Optimization Algorithms"
- **Constitutional AI**: Bai et al., "Constitutional AI: Harmlessness from AI Feedback"
