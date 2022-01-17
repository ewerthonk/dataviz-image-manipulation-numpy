#!/usr/bin/env python
# coding: utf-8

# # Manipulação de Imagem com NumPy

# ## Importando as bibliotecas necessárias

# In[1]:


from skimage import io
import numpy as np
import matplotlib.pyplot as plt

# Permitindo a visualização frontend de imagens e gráficos
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Carregando a imagem, armazendo seu formato e visualizando-a

# In[2]:


img = io.imread('imgs/shiba_inu.jpg')

# Visualizando o formato da imagem (640px x 640px x 3 matrizes[RGB])
height, width, rgb = img.shape

# Apresentando a imagem no frontend
plt.imshow(img)


# ## 1. Cortando a imagem no sentido vertical.

# In[3]:


# Criando uma cópia da imagem original (para preservá-la)
img_vcut = img[:, :(int(height/2)), :].copy()

# Apresentando a imagem no frontend
plt.imshow(img_vcut)


# ## 2. Cortando a imagem no sentido horizontal.

# In[4]:


# Criando uma cópia da imagem original (para preservá-la)
img_hcut = img[:(int(width/2)), :, :].copy()

# Apresentando a imagem no frontend
plt.imshow(img_hcut)


# ## 3. Apagando o nariz do cachorro 
# 
# Método usado: transformar os pixels no nariz em pixels de cor branca.

# ### Aumentando o detalhamento da imagem para definir os pixels a serem transformados com maior precisão

# In[5]:


img_noseless = img.copy()

# Criando a estrutura do gráfico e aumentando o tamanho de visualização da imagem
fig, ax1 = plt.subplots(figsize = (18,18))

# Apresentando a imagem no frontend
ax1.imshow(img_noseless)

# Aumentando o número de marcações nas linhas do gráfico
ax1.yaxis.set_ticks(np.arange(0, int(height), 20))
ax1.xaxis.set_ticks(np.arange(0, int(width), 20))

# Criando uma grade na visualização
ax1.grid(color='w', linestyle='--', linewidth=1)


# ### Determinando os pontos
# 
# Pela visualização, nota-se que os pontos ideais para transformar os pixels é no quadrado delimitado por:
# 
# |  x  |  y  |
# |:---:|:---:|
# | 330 | 280 |
# | 330 | 360 |
# | 420 | 360 |
# | 420 | 280 |

# In[6]:


# Guardando os pontos do quadrado
coordinates = ((330, 280), (330, 360), (420, 360), (420, 280))

# Guardando a ligação de linhas do quadrado
lines = ((330, 280), (330, 360), (420, 360), (420, 280), (330, 280))

# Replicando o gráfico anterior
fig, ax2 = plt.subplots(figsize = (18,18))

# Apresentando a imagem no frontend
ax2.imshow(img_noseless)

# # Aumentando o número de marcações nas linhas do gráfico
# ax2.yaxis.set_ticks(np.arange(0, int(height), 20))
# ax2.xaxis.set_ticks(np.arange(0, int(width), 20))

# # Criando uma grade na visualização
# ax2.grid(color='w', linestyle='--', linewidth=1)

# Adicionando os pontos mencionados na análise
for coordinate in coordinates:
    ax2.text(x=coordinate[0], 
             y=coordinate[1], 
             s=f'({coordinate[0]}, {coordinate[1]})',
             ha='center',
             va='center',
             color='w',
             size='x-large',
             weight='bold')
    
ax2.plot([coord[0] for coord in lines], [coord[1] for coord in lines], '-wo')


# ### Transformando os pixels do nariz para a cor branca

# In[7]:


# Separando os valores das coordenadas para o slicing da imagem
h_coord = set([coord[0] for coord in coordinates])
v_coord = set([coord[1] for coord in coordinates])

# Transformando as 3 matrizes RGB em branco
img_noseless[min(v_coord):max(v_coord), min(h_coord):max(h_coord), :] = 255

# Apresentando a imagem no frontend
plt.imshow(img_noseless)


# ## 4. Transformando a imagem para escala de cinza.
# 
# A fórmula para transforma para escala de cinza é:
# 
# $$0.299 * \text{red} + 0.587 * \text{green} + 0.114 * \text{blue}$$

# In[8]:


# Criando uma cópia da imagem original (para preservá-la)
img_gray = img.copy()

# Aplicando a fórmula de escala de cinza para a matriz da primeira camada de cor
img_gray[ :, :, 0] = ((img_gray[ :, :, 0]*0.299) +
                      (img_gray[ :, :, 1]*0.587) +
                      (img_gray[ :, :, 2]*0.114))

# Eliminando as demais camadas de cor
img_gray = img_gray[ :, :, 0]

# Apresentando a imagem no frontend
plt.imshow(img_gray, cmap="gray")

