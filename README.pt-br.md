# Machine Learning - Dr. Diabetes - Python
Checkpoint #4 de Coding For security da FIAP
> - Objectivo: Desenvolver  um  programa  baseado  na  técnica  deaprendizagem  de máquina supervisionada.
> - Desafio: Como saber se tenho diabetes?

## Conteúdo
* [Informações Gerais](#general)
* [Parâmetros](#parâmetros)
* [Tecnologias](#tecnologias)
* [Configuração](#setup)

- - - - - - - - - - - - - - - - - - -

## Geral
Este programa visa fazer um pré-diagnóstico da diabetes com base nos valores de glicose do paciente recolhidos em três estados e situações diferentes. São elas: Estado casual, pós sobrecarga e jejum. 
Pode trazer 3 resultados diferentes.
* *Glicose normal*
* *Glicose diminuída*
* *Diabetes Mellitus*

## Parâmetros
* **Glicose normal**
    - Em jejum:
        - Inferior a 100mg/dL
    - Pós Sobrecarga: 
        - Inferior a 140mg/dL
    - Glicemia Casual:
        - Inferior de 200mg/dL
* **Glicose diminuída**
    - Em jejum:
        - Entre 100 e 126 mg/dL
    - Pós Sobrecarga: 
        - Entre 140 a 200mg/dL
    - Glicemia Casual:
        - Inferior de 200mg/dL
*Diabetes mellitus***
    - Em jejum:
        - Maior ou igual a 126mg/dL
    - Pós Sobrecarga:
        - Maior ou igual a 126mg/dL
    - Glicemia Casual:
        - Maior ou igual a 200mg/dL
*Critérios para avaliação***
    - Em jejum: Sem ingestão de alimentos há no minimo 8 horas
    - Pós Sobrecarga: 2 horas após 75 gramas de glicose
    - Glicemia Casual: Realizado em qualquer momento do dia
###### Fonte: [GlicOnline](https://gliconline.net/tenho-diabetes/)

## Tecnologias
Este projeto foi realizado em [Python 3.10](https://www.python.org) usando a biblioteca [scikit-learn](https://scikit-learn.org/stable/)

## Configuração
* 1 - Instalar [Python](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe)
* 2 - Instalar a biblioteca [scikit-learn](https://scikit-learn.org/stable/install.html#)
	- Abra o CMD
	- Digite `pip install -U scikit-learn` e execute-o
* 3 - Descarregue o `doctormachinelearning.py` e execute-o
