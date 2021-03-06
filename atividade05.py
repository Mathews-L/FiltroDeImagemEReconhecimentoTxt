# -*- coding: utf-8 -*-
"""Atividade05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XuYrcBG_HgbnIXHmwK3v8RZT9XZOi7bx

**MATEUS LUCAS FRANCO - 202010520**
"""

! sudo apt install tesseract-ocr 
! pip install pytesseract
! sudo apt-get install tesseract-ocr-por


import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import imagem

import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt
import scipy

#	  Desenvolva um código que lhe permita abrir uma imagem RGB ou BGR de sua preferência, 
#   utilizando a interface python do OpenCV. Logo depois, converta a imagem para escala de cinza e
#   exiba as duas imagens lado a lado na tela. Documente as funções utilizadas no código.

urls = ["img.jpg"]

for url in urls:
  image = cv.imread(url)                              #Leitura da imagem
  transf_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #Comando utilizado para transformar a imagem em cinza
  gray = cv.cvtColor(transf_gray,cv.COLOR_GRAY2BGR)

  final_photo = np.hstack((image, gray))

  cv2_imshow(final_photo)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') #Criando o detector de faces


faces = face_cascade.detectMultiScale(image,scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv.CASCADE_SCALE_IMAGE) #Execução do detector de faces


for (x,y,w,h) in faces:
     cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2) #"Desenhando" o retangulo vermelho na face detectada

cv2_imshow(image)

! sudo apt-get install tesseract-ocr-por

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import imagem

urls2 = ["image.jpg"]


for url in urls2:
  image = cv.imread(url) 
  cv2_imshow(image)

mensagem = pytesseract.image_to_string(image, lang='por') #Depois de ler e imprimir a imagem, será usado o pytesseract para extrair a mensagem da foto
print(mensagem)