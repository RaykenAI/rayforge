from setuptools import setup, find_packages
import pathlib
root = pathlib.Path(__file__).parent
long_description = (root / "README.md").read_text(encoding="utf-8")
def load_requirements(filename="requirements.txt"):
    with open(filename) as f:
        return [line.strip() for line in f if line and not line.startswith("#")]

setup(
    name="rayforge",
    version="0.1.0",
    description="🧠 RayForge: Universal Python framework to download, run, and metricize AI models via HuggingFace, OpenAI, and Replicate.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RaykenAI",
    author_email="hylendust@gmail.com",
    url="https://github.com/rayken-ai/rayforge",  # Update if needed
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=load_requirements(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "rayforge=rayforge.cli.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Framework :: FastAPI",
    ],
    extras_require={
        "dev": ["pytest", "ruff", "python-dotenv"],
    },
    license="MIT",
    zip_safe=False,
)
