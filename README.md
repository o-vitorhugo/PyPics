# PyPics

Biblioteca simples para manipulação de imagens com Python.

## Descrição

PyPics permite aplicar filtros e transformações básicas em imagens de maneira fácil e rápida. Ideal para projetos de aprendizado ou automação simples de edição de imagens.

## Funcionalidades

* Converter imagens para preto e branco
* Rotacionar imagens
* Redimensionar imagens em quadrado
* Espelhar horizontalmente
* Aplicar blur simples

## Instalação

```bash
pip install pypics
```

## Como Usar (Quickstart)

```python
from pypics.funcoes import (
    preto_e_branco,
    rotacionar,
    redimensionar,
    espelhar_horizontal,
    blur_simples
)

# Coloque suas imagens em uma pasta dentro do projeto e teste as funções

# Exemplos de uso e descrição dos parâmetros:

# preto_e_branco(caminho_imagem_original, caminho_imagem_processada)
preto_e_branco('img_original.jpg', 'img_processada.jpg')

# rotacionar(caminho_imagem_original, caminho_imagem_processada, angulo_em_graus)
rotacionar('img_original.jpg', 'img_rot90.jpg', 90)

# redimensionar(caminho_imagem_original, caminho_imagem_processada, tamanho_em_pixel)
redimensionar('img_original.jpg', 'img_red.jpg', 300)

# espelhar_horizontal(caminho_imagem_original, caminho_imagem_processada)
espelhar_horizontal('img_original.jpg', 'img_esp.jpg')

# blur_simples(caminho_imagem_original, caminho_imagem_processada)
blur_simples('img_original.jpg', 'img_blur.jpg')
```

## Autor

Maria Isabel Henke e Vitor Hugo Reis de Jesus - [hugo.reisj@hotmail.com](mailto:hugo.reisj@hotmail.com)

## Link do Repositório

[https://github.com/o-vitorhugo/pypics](https://github.com/o-vitorhugo/pypics)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.