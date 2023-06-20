# cloud-computing-project-playlatam

## Conda environment
Create the conda environment with the environment.yml file

```shell
conda env create -f environment.yml
conda activate playlatam-pokemon-vgc
```

## Requirements
Install the requirements with pip

```shell
pip install -r src/requirements.txt
```

## Setup selenium on wsl

Follow this tutorial: https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/


## Pre-commit

After you have installed the requirements.txt with pip.
To generate the git hooks, you must run the following:

```shell
pre-commit install  # installs .git/hooks/pre-commit
pre-commit install --hook-type pre-push  # installs .git/hooks/pre-push
```

## Scraping

```shell
python main.py
```
