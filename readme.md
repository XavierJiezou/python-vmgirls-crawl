# Introduction
Crawl images based on `Python` from the website [vmgrils.com](https://www.vmgirls.com/).
# Install
The following modules must be installed for images crawling.
```bash
pip install requests
pip install BeautifulSoup4
pip install fake_useragent
pip install tqdm
```
The following modules must be installed for faces detection.
```bash
pip install opencv-python
pip install dlib
pip install tqdm
```
# Usage
Crawl almost all images of the website [vmgrils.com](https://www.vmgirls.com/).
```bash
python main.py
```
Randomly choice 81 images from the crawled images and view.
```bash
python show.py
```
Detect and extract faces from the images crawled to make a dataset for deep learning training.
```bash
python face.py
```
# Result
## Single-image-preview
![single-image-preview.jpg](single-image-preview.jpg)
## Multi-image-preview
![Multi-image-preview.jpg](Multi-image-preview.jpg)
## Data of craweling
| Item |Details|
|:--:|:--:|
| Website | [https://www.vmgirls.com/](https://www.vmgirls.com/) |
| Sitemap | [https://www.vmgirls.com/sitemap.html](https://www.vmgirls.com/sitemap.html) |
| Date of crawling | 2021年4月28日 |
| Total number of images | 17601 |
| Total number of faces | 13960 |
| Types of images | png, jpg, jpeg |
| Link of repository | [https://github.com/XavierJiezou/python-vmgirls-crawl/](https://github.com/XavierJiezou/python-vmgirls-crawl/) |
# Cite
> [https://github.com/psf/requests](https://github.com/psf/requests)
> [https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)
> [https://github.com/hellysmile/fake-useragent](https://github.com/hellysmile/fake-useragent)
> [https://github.com/tqdm/tqdm](https://github.com/tqdm/tqdm)