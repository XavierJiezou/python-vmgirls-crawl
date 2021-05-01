import os
from tqdm import tqdm
from PIL import Image
import concurrent.futures as cf


class DataProcessing(object):
    def __init__(self, srcdir, dstdir):
        self.srcdir = srcdir
        self.dstdir = dstdir
        os.makedirs(self.dstdir, exist_ok=True)

    def size(self, in_path, out_path, pbar):
        img = Image.open(in_path)
        w, h = img.size
        if w >= 128 and h >= 128:
            img = img.resize((128, 128), Image.ANTIALIAS)
            img.save(out_path, quality=95)
        else:
            pass
        pbar.update(1)

    def main(self):
        total = len(os.listdir(self.srcdir))
        with tqdm(total=total) as pbar:
            with cf.ThreadPoolExecutor() as tp:
                for item in os.listdir(self.srcdir):
                    in_path = f'{self.srcdir}/{item}'
                    out_path = f'{self.dstdir}/{item}'
                    tp.submit(self.size, in_path, out_path, pbar)


if __name__ == '__main__':
    DataProcessing('./vmgs-face', './vmgs-face-processing').main()
