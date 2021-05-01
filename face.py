import os
import cv2
import dlib
import time
from tqdm import tqdm
import concurrent.futures as cf


class MakeFaceDataset():
    def __init__(self, srcdir, dstdir):
        self.srcdir = srcdir
        self.dstdir = dstdir
        os.makedirs(dstdir, exist_ok=True)

    def crop(self, subdir):
        for j in tqdm(os.listdir(f'{self.srcdir}/{subdir}'), desc=subdir):
            in_path = f'{self.srcdir}/{subdir}/{j}'
            out_path = f'{self.dstdir}/{subdir}_{j.split(".")[0]}'
            model_path = './cnn_human_face_detect.dat'
            cnn_face_detector = dlib.cnn_face_detection_model_v1(model_path)
            img = cv2.imread(in_path)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_hist = cv2.equalizeHist(img_gray)
            faces = cnn_face_detector(img_hist, 1)
            for index, face in enumerate(faces):
                x1 = face.rect.left()
                y1 = face.rect.top()
                x2 = face.rect.right()
                y2 = face.rect.bottom()
                cp = img[y1:y2, x1:x2]
                cv2.imwrite(f'{out_path}_{index+1}.jpg', cp)

    def main(self):
        with cf.ThreadPoolExecutor() as tp:
            for i in os.listdir(self.srcdir):
                tp.submit(self.crop, i)
        print('Face Detection Finished!')
                
                    
if __name__ == '__main__':
    MakeFaceDataset('./vmgs', './vmgs-face').main()
