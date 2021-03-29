"""
@author:Wang Xinsheng
@File:main.py
@description:...
@time:2021-03-29 14:22
"""
import requests
from bs4 import BeautifulSoup
import tqdm

url = 'https://crustal.usgs.gov/speclab/QueryAll07a.php?page=2'
base_url = 'https://crustal.usgs.gov'
def download_file(url):
    # 下载文件
    response = requests.get(url, stream=True)
    with open( './'+url.split('/')[-1], 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
if __name__ == '__main__':
    for i in range(1,248):
        print("正在下载第{}页".format(i))
        url = 'https://crustal.usgs.gov/speclab/QueryAll07a.php?page={}'.format(i)
        repsonse = requests.get(url)
        content_soup = BeautifulSoup(repsonse.text,'html.parser',from_encoding='utf-8')
        # data-column-name="ZIP_File"
        download_links = content_soup.find_all('td',attrs={'data-column-name':'ZIP_File'})
        for download_link in download_links:
            link = download_link.find('a').get('href')
            link = base_url+link
            download_file(link)
            print(link)
    # print(len(download_links))