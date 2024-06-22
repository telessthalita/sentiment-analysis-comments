# Sentiment Analysis Comments

Este repositório contém um algoritmo simples de análise de sentimentos para comentários de usuários. O algoritmo analisa o sentimento de um comentário fornecido pelo usuário, categorizando-o como Positivo, Negativo ou Neutro com base em uma lista pré-definida de palavras-chave.

## Como Funciona

O programa solicita ao usuário que insira um comentário. Em seguida, ele:
1. Divide o comentário em palavras individuais.
2. Conta o número de palavras positivas, negativas e neutras no comentário.
3. Determina o sentimento predominante do comentário com base nas contagens de palavras.

## Listas de Palavras-Chave

- **Palavras Positivas**: bom, ótimo, excelente, maravilhoso, gostei, incrível
- **Palavras Negativas**: ruim, péssimo, horrível, terrível, odeio
- **Palavras Neutras**: mas, deixou, apesar, embora

## Exemplo de Uso

```bash
Digite seu comentário: A mentoria foi incrível, aprendi muito!
Sentimento: Positivo
