# Interpolação de Imagens

## Desenvolvido por [Hernandes Macedo](https://github.com/hernandesmacedo) & [Heitor Galdino](https://github.com/h80r)
  &nbsp;
### [Vídeo de apresentação do projeto](https://youtu.be/25KToe8ukXk)
  &nbsp;

## Descrição
* Nesse projeto há a implementação de algoritmos de Interpolação por vizinho mais próximo e da Interpolação Bilinear, ambos para redução e ampliação de imagens.

## Definições
* <u>Interpolação por vizinho mais próximo</u> é uma técnica que utiliza a remoção de pixels de uma imagem para que suas dimensões sejam reduzidas, e também reproduz pixels para que suas dimensões sejam ampliadas. Essa técnica é conhecida por produzir imagens pixeladas.
* <u>Interpolação Bilinear</u> é uma técnica que utiliza a média de pixels para remover ou criar novos pixels, fazendo com que as dimensões de uma imagem sejam reduzidas ou ampliadas. Essa técnica é conhecida por produzir imagens mais suaves/borradas.

## Exemplos

  ### *Imagem 1* ampliada atráves da Interpolação por vizinho mais próximo
  ![Exemplo de Interpolação por vizinho mais próximo](https://lh3.googleusercontent.com/pw/ACtC-3cf5x748GzGxsk2AoKv2iBzFkGbOCNQaQt89o84sYzK9HO7Q2kJH7VVOfuDX6uyW2Y9KzcHKlodA4Ll4m52uKqavS6TfXnr4Updy2Hs0wEIMrwP2qF3IM5f47Qo_kZkPvGnx4Z6T8wHnLLKRJ1krQns=w1280-h640-no?authuser=0)
  ### *Imagem 1* ampliada atráves da Interpolação Bilinear
  ![Exemplo de Interpolação Bilinear](https://lh3.googleusercontent.com/pw/ACtC-3c0M1GY_mAp8zpKP9TL5bESUj0ywZKc3ziQTRwIPkHkp-ea-GOU7VniT6YYI3JPyh-NPme9ds2DnfZuj4AyZozEW_dXsd6Cy7JlFkZIzA0gIVAahEMg6q6W3UlCrXfzUlH878vYJILV9I-04ZCv4v_0=w1280-h640-no?authuser=0)

  ### *Imagem 2* ampliada atráves da Interpolação por vizinho mais próximo
  ![Exemplo de Interpolação por vizinho mais próximo](https://lh3.googleusercontent.com/pw/ACtC-3cJK9otkcgjnuDRAqTJlOF7QneqvZNyoQa3Fqe13EZwLiA4KfUgJD-phsTnxPuWcUt-shqqttfpeZAb4NRSa7O04UiStQzNrIobh9U2rNzV7EqZJIoYkmyChY_oOt8k6BEBj1TS6EiO6DVi57drylXJ=w1280-h640-no?authuser=0)
  ### *Imagem 2* ampliada atráves da Interpolação Bilinear
  ![Exemplo de Interpolação Bilinear](https://lh3.googleusercontent.com/pw/ACtC-3epDhecVweh-2Ldfr1NTgW0AK1SAl2LBkIVbocuWlMV2f8mY367gSgzHGP9Ne92zTLpTKZhCgwSXc-VlnFmOK60BkvS87H41HtATDYo507k9NheEGFYPfeE-0NTM-PM0ZxmNnpe7Iulg87JsrNv9Bfg=w1280-h640-no?authuser=0)

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