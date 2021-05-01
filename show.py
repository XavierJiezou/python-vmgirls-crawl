import os
import matplotlib.pyplot as plt
import random
from PIL import Image
from collections import Counter

root = './vmgs'
imgs = []
temp = []
dirs = os.listdir(root)
random.shuffle(dirs)
for i in dirs:
    for j in os.listdir(f'{root}/{i}'):
        img_path = f'{root}/{i}/{j}'
        img = Image.open(img_path)
        img = img.resize((900, 600), Image.ANTIALIAS)
        w, h = img.size
        if w>h:
            imgs.append(img)
            temp.append(img.size)
            break
    if len(imgs)==81:
        break


plt.figure(figsize=(15, 10))
for i, img in enumerate(imgs):
    plt.subplot(9, 9, i+1)
    plt.imshow(img)
    plt.axis('off')
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
plt.savefig('test.jpg', dpi=300)