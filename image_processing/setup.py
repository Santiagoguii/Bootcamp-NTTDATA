from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pacote_imagem_simples_python",
    version="0.0.1",
    author="Guilherme Santiago",
    author_email="guilhermepsantiago04@gmail.com",
    description="Projeto processamento de imagens com python - Bootcamp. NTT DATA",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Santiagoguii/Bootcamp-NTTDATA",
    packages=find_packages(),
    install_requires=requirements,
)