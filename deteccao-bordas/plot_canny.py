"""
=============================
Detector de Borda Inteligente
=============================

O filtro Canny é um detector de borda de vários estágios. 
Utiliza um filtro baseado na derivada de uma Gaussiana para 
calcular a intensidade dos gradientes. A Gaussiana reduz o 
efeito do ruído presente na imagem. Em seguida, as bordas 
potenciais são reduzidas a curvas de 1 pixel, removendo 
pixels não máximos do gradiente de magnitude. Finalmente, 
os pixels de borda são mantidos ou removidos usando o 
limiar de histerese no gradiente de magnitude.

O Canny tem três parâmetros ajustáveis: a largura da 
Gaussiana (quanto mais ruidosa a imagem, maior a largura) 
e o limiar baixo e alto para o limiar de histerese.

"""
import matplotlib.pyplot as plt
from skimage import feature
import cv2 as cv 
# import numpy as np
# from scipy import ndimage as ndi
# from skimage.util import random_noise
# from skimage.io import imread

image = cv.imread('plant.jpg',0)

# Generate noisy image of a square
# image = np.zeros((128, 245), dtype=float)
# image[32:-32, 64:-64] = 1
# image = ndi.rotate(image, 60, mode='constant')
# image = ndi.gaussian_filter(image, 4)
# image = random_noise(image, mode='speckle', mean=0.1)

# Compute the Canny filter for two values of sigma

edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=2)
edges3 = feature.canny(image, sigma=3)

# display results
fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(8, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Imagem Tons de Cinza', fontsize=16)

ax[1].imshow(edges1, cmap='gray')
ax[1].set_title(r'Detecção de Bordas, $\sigma=1$', fontsize=16)

ax[2].imshow(edges2, cmap='gray')
ax[2].set_title(r'Detecção de Bordas, $\sigma=2$', fontsize=16)

ax[3].imshow(edges3, cmap='gray')
ax[3].set_title(r'Detecção de Bordas, $\sigma=3$', fontsize=16)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
