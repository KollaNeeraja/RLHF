# RLHF PoC - Component Reference

## Core Modules (3,000+ lines of code)

### 1. Algorithms Module (`src/algorithms/policy_gradient.py`)

**Classes:**
- `PPOConfig` - Configuration dataclass for PPO
- `PolicyNetwork` - Neural network for policy (actor)
- `ValueNetwork` - Neural network for value function (critic)
- `PPOTrainer` - Main PPO training class
- `TRPOTrainer` - Trust region policy optimization trainer

**Key Methods:**
- `PPOTrainer.compute_gae()` - Generalized Advantage Estimation
- `PPOTrainer.train_step()` - Single training iteration
- `PPOTrainer.save()` / `load()` - Model checkpointing
- `TRPOTrainer.compute_kl_divergence()` - KL divergence computation

**Features:**
- ✓ GAE for variance reduction
- ✓ Entropy regularization
- ✓ Gradient clipping
- ✓ Multi-epoch mini-batch updates
- ✓ Configurable hyperparameters

---

### 2. Reward Modeling Module (`src/reward_modeling/preference_model.py`)

**Classes:**
- `RewardModel` - Neural network reward scorer
- `Preference` - Preference data structure
- `PreferenceDataset` - PyTorch dataset for preferences
- `PreferenceRewardModel` - Learn reward from preferences
- `BradleyTerryModel` - Classical probabilistic ranking
- `RankingModel` - Neural listwise ranking

**Key Methods:**
- `PreferenceRewardModel.preference_loss()` - Bradley-Terry loss
- `PreferenceRewardModel.train()` - Training loop with validation
- `BradleyTerryModel.fit()` - EM-based fitting
- `BradleyTerryModel.predict()` - Preference probability
- `BradleyTerryModel.get_ranking()` - Get ranked list
- `RankingModel.listwise_loss()` - NDCG-based loss

**Features:**
- ✓ Preference pair training
- ✓ Confidence weighting
- ✓ Train/validation splitting
- ✓ Multiple model architectures
- ✓ Ranking and scoring

---

### 3. Safety Module (`src/safety/safety_checker.py`)

**Classes:**
- `SafetyLevel` - Enum for violation levels
- `SafetyViolation` - Violation data structure
- `ToxicityDetector` - Pattern-based toxicity detection
- `SafetyConstraint` - Base constraint class
- `LengthConstraint` - Output length checking
- `FactualConsistencyConstraint` - Factual checking
- `SafetyChecker` - Multi-layer safety evaluation
- `SafetyFilter` - Filter outputs by safety
- `AlignmentGuard` - Value alignment checking
- `SafetyMonitor` - Track safety during training

**Key Methods:**
- `ToxicityDetector.detect_toxicity()` - Detect harmful patterns
- `SafetyChecker.check_safety()` - Comprehensive evaluation
- `SafetyFilter.filter()` - Filter outputs
- `AlignmentGuard.check_alignment()` - Check alignment
- `SafetyMonitor.get_safety_stats()` - Statistics

**Features:**
- ✓ Multi-category toxicity detection
- ✓ Custom constraint support
- ✓ Confidence scoring
- ✓ Safety filtering
- ✓ Training-time monitoring

---

### 4. Red-teaming Module (`src/red_teaming/adversarial_generator.py`)

**Classes:**
- `AdversarialExample` - Adversarial prompt data structure
- `JailbreakTemplate` - Template for generating attacks
- `RedTeamingStrategy` - Base strategy class
- `PromptInjectionStrategy` - Prompt injection attacks
- `SocialEngineeringStrategy` - Social engineering
- `LogicExploitStrategy` - Logic-based attacks
- `AdversaryGenerator` - Main generator
- `AdversarialScoreCard` - Robustness evaluation

**Key Methods:**
- `PromptInjectionStrategy.generate_attacks()` - Generate injections
- `SocialEngineeringStrategy.generate_attacks()` - Generate social attacks
- `LogicExploitStrategy.generate_attacks()` - Generate logic attacks
- `AdversaryGenerator.generate_attacks()` - Unified generation
- `AdversaryGenerator.test_model()` - Test against attacks
- `AdversarialScoreCard.get_summary()` - Robustness summary

**Features:**
- ✓ 3 attack strategy families
- ✓ 10+ attack templates
- ✓ Configurable attack count
- ✓ Model vulnerability testing
- ✓ Robustness scoring

---

### 5. Constitutional AI Module (`src/constitutional_ai/constitution.py`)

**Classes:**
- `Principle` - Constitutional principle
- `Constitution` - Set of principles
- `PrincipleEvaluator` - Evaluate against principles
- `CritiqueGenerator` - Generate critiques
- `SelfAlignmentSystem` - Iterative alignment
- `ConstitutionalEvaluator` - Main interface

**Key Methods:**
- `Constitution.add_principle()` - Add custom principle
- `PrincipleEvaluator.evaluate_principle()` - Single principle eval
- `PrincipleEvaluator.evaluate_all()` - All principles
- `CritiqueGenerator.generate_critique()` - Generate feedback
- `SelfAlignmentSystem.align_output()` - Iterative improvement
- `ConstitutionalEvaluator.evaluate()` - Quick scoring
- `ConstitutionalEvaluator.improve()` - Improve outputs

**Features:**
- ✓ 5 default principles
- ✓ Custom principle support
- ✓ Multi-principle evaluation
- ✓ Automated critique
- ✓ Iterative self-alignment

---

### 6. Utilities Module (`src/utils/helpers.py`)

**Functions:**
- `create_dummy_embeddings()` - Create test embeddings
- `batch_tensors()` - Batch creation
- `compute_entropy()` - Entropy computation
- `compute_kl_divergence()` - KL divergence
- `normalize()` - Normalization
- `running_mean()` - Running average
- `compute_returns()` - Discounted returns
- `save_checkpoint()` - Checkpoint saving
- `load_checkpoint()` - Checkpoint loading

**Classes:**
- `MetricsTracker` - Track training metrics
- `EvaluationMetrics` - Compute evaluation metrics

**Features:**
- ✓ Math utilities
- ✓ Metric tracking
- ✓ Checkpoint management
- ✓ Data utilities

---

## Test Suite (`tests/test_components.py`)

**Test Classes:**
- `TestPPO` - 3 PPO tests
- `TestRewardModel` - 3 reward model tests
- `TestSafety` - 3 safety tests
- `TestRedTeaming` - 2 red-teaming tests
- `TestConstitutionalAI` - 4 constitutional AI tests

**Total:** 15 unit tests covering all major components

---

## Jupyter Notebooks (5 interactive examples)

### 1. `01_ppo_training.ipynb` (6 sections, ~200 lines)
- PPO trainer initialization
- Episode generation
- Training loop
- Loss visualization
- Model inference

### 2. `02_reward_modeling.ipynb` (7 sections, ~200 lines)
- Preference data creation
- Bradley-Terry model training
- Neural reward model training
- Ranking comparison
- Score visualization

### 3. `03_red_teaming.ipynb` (7 sections, ~200 lines)
- Adversarial generation
- Attack categories
- Model testing
- Vulnerability analysis
- Robustness scorecard

### 4. `04_constitutional_ai.ipynb` (8 sections, ~250 lines)
- Principle definition
- Principle evaluation
- Alignment visualization
- Self-alignment
- Custom principles

### 5. `05_full_rlhf_pipeline.ipynb` (9 sections, ~250 lines)
- Complete pipeline
- Preference collection
- Reward modeling
- RL training
- Safety monitoring
- Red-teaming
- Constitutional alignment
- Results visualization

---

## Documentation Files

1. **README.md** (400+ lines)
   - Project overview
   - Installation instructions
   - Quick start examples
   - Component descriptions
   - Reference papers

2. **GETTING_STARTED.md** (200+ lines)
   - Installation steps
   - Code examples for each component
   - Module descriptions
   - Next steps

3. **DEVELOPMENT.md** (300+ lines)
   - Architecture overview
   - Development workflow
   - Component extension guide
   - Performance optimization
   - Debugging tips

4. **PROJECT_SUMMARY.md** (250+ lines)
   - What was created
   - Quick start
   - Learning path
   - Next steps

5. **LICENSE.md** (50+ lines)
   - Usage rights
   - Citation format
   - References
   - Contributing guidelines

---

## Configuration Files

1. **requirements.txt**
   - 13 main dependencies
   - Optional: wandb, tensorboard

2. **setup.py**
   - Package configuration
   - Dependency specifications
   - Development extras

3. **pytest.ini**
   - Test configuration
   - Test discovery patterns
   - Output options

4. **.gitignore**
   - Python artifacts
   - Virtual environments
   - IDE files
   - Models and data
   - Logs

---

## Component Count Summary

| Category | Count |
|----------|-------|
| **Classes** | 30+ |
| **Functions** | 100+ |
| **Test Cases** | 15 |
| **Notebooks** | 5 |
| **Documentation Files** | 5 |
| **Total Code Lines** | 3,000+ |
| **Total Doc Lines** | 1,500+ |

---

## Key Integration Points

### Pipeline Flow
```
Human Preferences
    ↓
Reward Model (Bradley-Terry or Neural)
    ↓
RL Training (PPO/TRPO)
    ↓
Safety Checking
    ↓
Constitutional Alignment
    ↓
Red-teaming Validation
    ↓
Final Aligned Model
```

### Component Dependencies
```
algorithms/ ← reward_modeling/ ← safety/
    ↓
utils/ ← red_teaming/
    ↓
constitutional_ai/
```

---

## Extension Points

### Adding New Components
1. Create new module in `src/`
2. Implement required interfaces
3. Add tests in `tests/`
4. Document in README or DEVELOPMENT.md

### Customization Examples
- Custom safety constraints
- Custom attack strategies
- Custom principles
- Custom reward models

---

**Total Project Size**: ~5,000 lines (code + docs)  
**Estimated Study Time**: 10-20 hours  
**Estimated Implementation Time**: 40-80 hours (if building from scratch)  

This is a production-quality proof of concept ready for learning, extension, and integration!
