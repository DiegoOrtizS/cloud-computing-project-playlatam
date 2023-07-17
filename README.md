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

## Lambda function (serverless)
Test it locally
```shell
serverless invoke local --function extract_data_from_playlatam
```

Deploy the lambda function with serverless
```shell
serverless deploy
```


## Scraping

```shell
python src/main.py
```

## Cloudwatch (monitoreo)


## MongoDB (cloud storage)
Gráfico de métricas de Network, donde se pueden apreciar los bytes out, número de requests y bytes in. En este caso se ha intentado reducir al máximo el número de requests a MongoDB por uso de funciones como insert_many. Asimismo, de todos los bytes hay muy pocos que terminan ingresando a la base de datos porque pasa por un proceso de filtrado de los datos scrapeados, donde solo se insertan los relevantes para el estudio.
![Network metric mongodb atlas](network-bytes.png)

