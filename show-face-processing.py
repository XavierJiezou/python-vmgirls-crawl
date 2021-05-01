import os
import random
import matplotlib.pyplot as plt


class ShowFaceProcessing(object):
    def __init__(self, root):
        self.root = root

    def show(self, imgs):
        plt.figure(figsize=(10, 10))
        for ind, img in enumerate(imgs):
            plt.subplot(10, 10, ind+1)
            plt.imshow(plt.imread(img))
            plt.axis('off')
            plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.savefig('face-processing.jpg', dpi=128)

    def main(self):
        imgs = [f'{self.root}/{name}' for name in os.listdir(self.root)]
        imgs = random.sample(imgs, k=100)
        self.show(imgs)


if __name__ == '__main__':
    ShowFaceProcessing('./vmgs-face-processing').main()
