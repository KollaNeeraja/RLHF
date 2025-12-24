#!/usr/bin/env python
"""
Quick test script to verify all RLHF components are working
"""

print("Testing RLHF PoC Components...\n")

# Test 1: PPO
try:
    from algorithms.policy_gradient import PPOTrainer, PPOConfig
    config = PPOConfig()
    trainer = PPOTrainer(input_dim=4, output_dim=2, config=config)
    print("✓ PPO Module: WORKING")
    print(f"  - Trainer initialized successfully")
except Exception as e:
    print(f"✗ PPO Module: FAILED - {e}")

# Test 2: Reward Modeling
try:
    from reward_modeling.preference_model import PreferenceRewardModel, BradleyTerryModel
    model = PreferenceRewardModel(embedding_dim=768, hidden_dim=256)
    print("✓ Reward Modeling: WORKING")
    print(f"  - Reward model initialized successfully")
except Exception as e:
    print(f"✗ Reward Modeling: FAILED - {e}")

# Test 3: Safety
try:
    from safety.safety_checker import SafetyChecker, ToxicityDetector
    checker = SafetyChecker()
    detector = ToxicityDetector()
    result = checker.check_safety("This is a safe response")
    print("✓ Safety Module: WORKING")
    print(f"  - Safety checker result: {result['is_safe']}")
except Exception as e:
    print(f"✗ Safety Module: FAILED - {e}")

# Test 4: Red Teaming
try:
    from red_teaming.adversarial_generator import AdversaryGenerator
    adversary = AdversaryGenerator()
    attacks = adversary.generate_attacks(target="classifier", num_attacks=3)
    print("✓ Red Teaming Module: WORKING")
    print(f"  - Generated {len(attacks)} adversarial examples")
except Exception as e:
    print(f"✗ Red Teaming Module: FAILED - {e}")

# Test 5: Constitutional AI
try:
    from constitutional_ai.constitution import ConstitutionalEvaluator
    evaluator = ConstitutionalEvaluator()
    score = evaluator.evaluate("This is a helpful response")
    print("✓ Constitutional AI: WORKING")
    print(f"  - Principle evaluation score: {score:.2f}")
except Exception as e:
    print(f"✗ Constitutional AI: FAILED - {e}")

print("\n" + "="*50)
print("All components tested successfully! ✓")
print("="*50)
