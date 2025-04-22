# TPC2 - Análise de um dataset de obras musicais

## AUTOR
### Artur Luís A95414 LEI

## OBJETIVO
O objetivo deste TPC era criar um programa que processasse um ficheiro CSV contendo informações sobre obras musicais. O programa cria os seguintes resultados:
1. Lista ordenada alfabeticamente dos compositores musicais;
2.  Distribuição das obras por período: quantas obras catalogadas em cada período;
3.  Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

## RESOLUÇÃO
- Após analisar brevemente o dataset fornecido, implementei um programa em Python (`leitor.py`) que:
  - Lê o ficheiro CSV linha a linha, ignora o cabeçalho e processa os dados.
  - Extrai os campos relevantes: `nome`, `periodo` e `compositor`.
  - Gera uma lista ordenada de compositores, removendo duplicados.
  - Calcula a distribuição das obras por período, utilizando um dicionário para contar as ocorrências.
  - Cria um dicionário onde cada período está associado a uma lista de títulos de obras, ordenada alfabeticamente.

## EXECUÇÃO
Para executar o programa, utilizo o seguinte comando no terminal:

```bash
python leitor.py