from setuptools import setup, find_packages

setup(
    name="rlhf-poc",
    version="0.1.0",
    description="Proof of Concept for RLHF, Safety, and Human Feedback",
    author="RLHF Research Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "torch>=1.10.0",
        "transformers>=4.20.0",
        "tqdm>=4.62.0",
        "pydantic>=1.9.0",
        "pytest>=7.0.0",
        "jupyter>=1.0.0",
        "matplotlib>=3.5.0",
        "scikit-learn>=1.0.0",
        "tensorboard>=2.8.0",
        "wandb>=0.12.0",
        "peft>=0.3.0",
    ],
    extras_require={
        "dev": ["pytest-cov", "black", "flake8", "mypy"],
    },
)
