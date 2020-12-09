#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.utils.data import download_file
from matplotlib.colors import LogNorm

arquivo = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
arq = fits.open(arquivo)
imagem = arq[0].data
arq.close()

print('Imagem em escala aritmética:')
plt.imshow(imagem, cmap='gray')
plt.colorbar()
plt.show()

# In[4]:


print('Imagem em escala logarítmica:')

plt.imshow(imagem, cmap='gray', norm=LogNorm())

#Definindo números que apareceram na barra logarítimica
cbar = plt.colorbar(ticks=[5e3, 1e4 , 1.5e4 ,2e4])

#"Legenda" de cada número que aparece ali em cima. Tente mudar 5.000 por "cinco mil", por exemplo.
cbar.ax.set_yticklabels(['5.000', '10.000','15.000','20.000'])
plt.show()

