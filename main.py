import os
import time
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import concurrent.futures as cf
from fake_useragent import UserAgent


class VmgirlsDownloader():
    def __init__(self, root):
        self.root = root
        os.makedirs(self.root, exist_ok=True)
        self.site = 'https://www.vmgirls.com/'
        self.sitemap = 'https://www.vmgirls.com/sitemap.html' # 从站点地图爬取文章列表
        self.headers = {'referer': self.site, 'user-agent': UserAgent().random}
        self.page()
        self.main()

    def page(self):
        resp = requests.get(self.sitemap, headers=self.headers)
        time.sleep(5)
        soup = BeautifulSoup(resp.content, 'lxml')
        temp = soup.select('h3 + ul li a') # 定位文章列表
        articles = []
        temp_dict = {}
        for item in temp:
            href = self.site+item.get('href')
            title = item.get('title')
            if temp_dict.get(title) == None:
                temp_dict[title] = 1
            else:
                temp_dict[title] += 1
                title += str(temp_dict[title]) # 重复文件夹的命名方式
            os.makedirs(os.path.join(self.root, title), exist_ok=True)
            articles.append([href, title])
        self.articles = articles

    def save(self, img_link, img_path):
        resp = requests.get(img_link, headers=self.headers)
        time.sleep(3)
        with open(img_path, 'wb') as f:
            f.write(resp.content)

    def down(self, article_link, article_title):
        resp = requests.get(article_link, headers=self.headers)
        time.sleep(5)
        soup = BeautifulSoup(resp.content, 'lxml')
        imgs = soup.select('div.nc-light-gallery img') # 定位文章里面的所有图片
        name = 1 
        for item in tqdm(imgs, desc=article_title):
            if 'https:' not in item.get('src'):
                img_link = 'https:'+item.get('src')
            else:
                img_link = 'https:'+item.get('srcset').split(' ')[0]
            img_path = f'{self.root}/{article_title}/{name}.{img_link.split(".")[-1]}'
            if not os.path.exists(img_path):
                self.save(img_link, img_path)
                name += 1
            else:
                continue

    def main(self):
        with cf.ThreadPoolExecutor() as tp:
            for article_link, article_title in self.articles:
                tp.submit(self.down, article_link, article_title)


if __name__ == '__main__':
    VmgirlsDownloader('./vmgs')
