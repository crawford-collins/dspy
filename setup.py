from setuptools import setup

setup(
    name="dspy-crawford",
    version="2.4.0",
    packages=["dspy"],
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
)