# Interpolação de Imagens

## Esse projeto foi desenvolvido por Hernandes Macedo & Heitor Galdino (@h80r)
  &nbsp;
## Objetivo
* Implementação da interpolação por vizinho mais próximo e da interpolação bilinear para redução e ampliação de imagens.

## Definições
* **Interpolação por vizinho mais próximo** é uma técnica que utiliza a remoção de pixels de uma imagem para que suas dimensões sejam reduzidas, e também reproduz pixels para que suas dimensões sejam ampliadas. Essa técnica é conhecida por produzir imagens pixeladas.
* **Interpolação Bilinear** é uma técnica que utiliza a média de pixels para remover ou criar novos pixels, fazendo com que as dimensões de uma imagem sejam reduzidas ou ampliadas. Essa técnica é conhecida por produzir imagens menos pixeladas/mais suaves.

## Desenvolvimento
* [x] Interpolação por vizinho mais próximo:
  * [x] Redução
  * [x] Ampliação
* [x] Interpolação bilinear:
  * [x] Redução
  * [x] Ampliação

## Uso
* Para o funcionamento deste projeto é necessário que as bibliotecas NumPy e OpenCV estejam instaladas. Instale-as utilizando os comandos:
  * `pip3 install NumPy`
  * `pip3 install opencv-python`
* Há sugestões de imagens para utilização na pasta `sample`.
* As novas imagens interpoladas pelo programa são salvas na pasta `export`.

## Tecnologias utilizadas
* Python 3.9.3
  * OpenCV 4.5.2.52
  * NumPy 1.20.2

## Documentação
* [OpenCV Docs](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
* [NumPy Docs](https://numpy.org/doc/)