import os
import random
from PIL import Image
import matplotlib.pyplot as plt


class ShowData(object):
    def __init__(self, root):
        self.root = root

    def show(self, imgs):
        plt.figure(figsize=(15, 10))
        for ind, img in enumerate(imgs):
            plt.subplot(9, 9, ind+1)
            plt.imshow(img)
            plt.axis('off')
            plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
            plt.margins(0, 0)
        plt.savefig('multi-images-preview.jpg.jpg', dpi=300)

    def main(self):
        imgs = []
        dirs = os.listdir(self.root)
        random.shuffle(dirs)
        for i in dirs:
            for j in os.listdir(f'{self.root}/{i}'):
                img_path = f'{self.root}/{i}/{j}'
                img = Image.open(img_path)
                img = img.resize((900, 600), Image.ANTIALIAS)
                w, h = img.size
                if w > h:
                    imgs.append(img)
                    break
            if len(imgs) == 81:
                break
        self.show(imgs)


if __name__=='__main__':
    ShowData('./vmgs').main()
