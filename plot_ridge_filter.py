"""
==================
Operadores de Cume
==================

Os filtros de crista podem ser usados para detectar estruturas 
semelhantes a cristas, como neurites, tubos, vasos, rugas ou rios.

Diferentes filtros de cumeeira podem ser adequados para detectar 
diferentes estruturas, por exemplo, dependendo do contraste ou 
nível de ruído.

A presente classe de filtros de cumeeira baseia-se nos autovalores 
da matriz Hessiana de intensidades de imagem para detectar 
estruturas de cumeeira onde a intensidade muda perpendicularmente, 
mas não ao longo da estrutura.

Observe que, devido aos efeitos de borda, os resultados dos filtros 
Meijering e Frangi são cortados em 4 pixels em cada borda para obter 
uma renderização adequada.
"""

#from skimage import data
#from skimage import color
from skimage.filters import meijering, sato, frangi, hessian
import matplotlib.pyplot as plt
import cv2 as cv 

image = cv.imread('sangue3.webp',0)

def identity(image, **kwargs):
    """Return the original image, ignoring any kwargs."""
    return image

# image = color.rgb2gray(data.retina())[300:700, 700:900]
cmap = plt.cm.gray

kwargs = {'sigmas': [1], 'mode': 'reflect'}

fig, axes = plt.subplots(2, 5)
for i, black_ridges in enumerate([1, 0]):
    for j, func in enumerate([identity, meijering, sato, frangi, hessian]):
        kwargs['black_ridges'] = black_ridges
        result = func(image, **kwargs)
        axes[i, j].imshow(result, cmap=cmap, aspect='auto')
        if i == 0:
            axes[i, j].set_title(['Imagem\nOrifinal', 'Meijering\nneuriteness',
                                  'Sato\ntubeness', 'Frangi\nvesselness',
                                  'Hessian\nvesselness'][j])
        if j == 0:
            axes[i, j].set_ylabel('black_ridges = ' + str(bool(black_ridges)))
        axes[i, j].set_xticks([])
        axes[i, j].set_yticks([])

plt.tight_layout()
plt.show()
