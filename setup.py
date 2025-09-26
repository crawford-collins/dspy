from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dspy-crawford",
    version="2.4.0",
    author="Crawford Collins",
    author_email="crawford.collins@example.com",
    description="DSPy fork: The framework for programming—not prompting—foundation models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crawford-collins/dspy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "backoff>=2.2.1",
        "joblib>=1.3.2",
        "openai>=1.12.0",
        "pandas",
        "regex",
        "requests",
        "tqdm",
        "ujson",
    ],
    extras_require={
        "dev": ["pytest", "black", "isort", "flake8"],
        "optional": ["anthropic", "cohere", "together", "fastembed", "qdrant-client"],
    },
)