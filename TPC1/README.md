# TPC1 - Somador On/Off

## AUTOR
### Artur Luís A95414 LEI

## OBJETIVO
O objetivo deste TPC era criar um programa em Python, sem usar expressões regulares, que processasse um texto e realizasse as seguintes operações:
1. Somar todas as sequências de dígitos encontradas no texto.
2. Desativar o comportamento de soma ao encontrar a string "off" (em qualquer combinação de maiúsculas e minúsculas).
3. Reativar o comportamento de soma ao encontrar a string "on" (em qualquer combinação de maiúsculas e minúsculas).
4. Sempre que o caráter "=" fosse encontrado, imprimir o valor atual da soma.
5. No final do texto, imprimir o valor total da soma.

## RESOLUÇÃO
- Foi implementado um programa em Python (`somador.py`) que:
  - Lê o texto de entrada linha a linha através do `stdin`.
  - Processa cada palavra para identificar números, comandos ("on", "off") e o caráter "=".
  - Soma os números encontrados quando o somador está ativo.
  - Imprime a soma atual sempre que o caráter "=" é encontrado.
  - Imprime a soma total no final do processamento.

## EXECUÇÃO
Para executar o programa, utilizo o seguinte comando no terminal:

```bash
python somador.py < input.txt


