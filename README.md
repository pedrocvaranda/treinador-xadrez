# Treinador de Xadrez – Gambito da Rainha

> **Sobre o autor:** Desenvolvido por [Pedro Varanda](github.com/pedrocvaranda), 
> autor de *Varandian Optics* 

## Descrição do Projeto

Este projeto é um **treinador de xadrez em Python**, focado no **Gambito da Rainha**, desenvolvido para aprendizado e prática de abertura clássica de forma **interativa e didática**.

O projeto oferece dois modos de jogo:

1. **Modo Treinador (Gambito da Rainha)**  
   - Ensina o Gambito da Rainha passo a passo.  
   - Fornece explicações sobre os princípios de cada lance.  

2. **Modo Livre Inteligente**  
   - Permite jogar qualquer abertura.  
   - Avalia seus lances e aponta **fraquezas estratégicas** ou peças mal posicionadas.  
   - Dá dicas detalhadas apenas quando o usuário solicita (`hint`).  

O projeto é **100% terminal**, simples de usar e não requer conhecimentos prévios em programação ou instalação de pacotes complexos.

---

## Pré-requisitos

- Python 3.7 ou superior  
- Biblioteca **`python-chess`**

Para instalar a biblioteca necessária, execute:

```bash
pip install chess
```
---

## Como Baixar o Projeto

1. Clone este repositório ou baixe o arquivo `.py` diretamente:
```bash
   git clone https://github.com/pedrocvaranda/treinador-xadrez.git
```
2. Acesse a pasta do projeto:
```bash
   cd treinador-xadrez
```
3.	Certifique-se de que o Python está instalado:
```bash
  	python --version
```
---

## Como Executar

1. Execute o arquivo principal
2. Você verá o menu inicial
3. Escolha o modo desejado digitando `1` ou `2`.

4. Durante o jogo, você pode:  
   - Digitar lances em **SAN** (ex: `d4`, `c4`, `Nf3`, `O-O`).  
   - Digitar `hint` para receber dicas explicativas.  
   - Digitar `quit` para sair do jogo.  

5. Após cada lance, o **tabuleiro será mostrado atualizado**, com explicações ou alertas estratégicos, dependendo do modo escolhido.

---

## Exemplo de Uso
Bem-vindo ao Treinador de Xadrez
Modo Treinador: foco no Gambito da Rainha

Como jogar:
- Digite lances em SAN, ex: d4, c4, Nf3, O-O
- Digite 'hint' para dicas explicativas
- Digite 'quit' para sair

Tabuleiro atual:

r n b q k b n r

p p p p p p p p

0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

0 0 0 P 0 0 0 0

0 0 0 0 0 0 0 0

P P P 0 P P P P

R N B Q K B N R


Seu lance: d4

Você jogou: d4

Explicação: Você está controlando o centro do tabuleiro, ótimo para dominar o jogo.

Tabuleiro após seu lance:
...

---

## Observações

- Este projeto é **didático**: não é um motor de xadrez profissional, mas sim uma ferramenta de aprendizado.  
- Recomendado para iniciantes e jogadores intermediários que queiram aprender o Gambito da Rainha ou melhorar percepção estratégica.  
- Funciona **diretamente no terminal**, sem interface gráfica.  

---
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
