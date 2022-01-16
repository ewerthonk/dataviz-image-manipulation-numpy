# Manipulação de Imagem com NumPy | Aula 03 | Data Science Degree

#### Repositório: desafio-imagem-numpy

### Autor
---
Ewerthon José Kutz.

### Conceitos utilizados
---
- Arrays e Matrizes multidimensionais.
- Representação computacional de imagens.
- Representação computacional de cores (RGB).
- Manipulação de imagens com a biblioteca Numpy.
- Manipulação de imagens com a biblioteca scikit-image.
- Visualização deimagens com a biblioteca Matplotlib.

Complexidade: Iniciante.

### Descrição
---
O desafio é abrir um arquivo de imagem de um cachorro Shiba inu (sim, o do Dogecoin) e efetuar **quatro** operações nessa imagem:

1. Cortar a imagem no sentido vertical.
2. Cortar a imagem no sentido horizontal.
3. Apagar o nariz do cachorro (tecnicamente, transformar os pixels no nariz em pixels de cor branca).
4. Transformar a imagem para escala de cinza.

#### A imagem
![shiba_inu.jpg](imgs/shiba_inu.jpg)

##### Curiosidade

A raça de cachorros Shiba inu é de origem japonesa (e uma das mais antigas por lá). Essa raça ficou especialmente conhecida após tornar-se um *meme* de reação muito popular em 2013, dando origem e inspiração à criptomoeda **DOGECOIN**.

A criptomoeda e alguns tweets do Elon Musk fizeram a raça ser facilmente reconhecida em qualquer lugar do mundo.

#### Dogecoin
![dogecoin.jpg](imgs/dogecoin.png)

#### Tweets
![tweet1.jpg](imgs/tweet1.jpg)

![tweet2.jpg](imgs/tweet2.jpg)

#### Contexto

Toda imagem colorida, do ponto de vista computacional, nada mais é do que um conjunto de três matrizes: <span style="color:red">Vermelha</span>, Verde e Azul (RGB de red, green e blue)), onde cada uma dessas matriz traz a intensidade da respectiva cor para cada um dos pixels.
![image.png](imgs/img5.jpg)

Os valores vão de 0 a 255, onde 0 representa a ausência dessa cor e 255 a intensidade mais forte. Se tivermos um píxel puramente vermelho ele será representado pelos seguintes valores em cada matriz:

- R = 255
- G = 0
- B = 0

Na imagem acima, cada célula da matriz representa um píxel. Uma imagem é formada por vários pixels.

Já uma imagem preta e branca ou também chamada de escala de cinza apresenta apenas uma matriz com valores entre 0 e 255 ou entre 0 e 1, onde quanto mais perto de 0, mais escuro é o píxel e quanto mais distante, mais claro.
