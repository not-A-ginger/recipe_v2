from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Food-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A food recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    author_email="24aspears@nyos.org",
    packages=[SRC_REPO],
    
    python_requires=">=3.9",
    install_requires=LIST_OF_REQUIREMENTS
)