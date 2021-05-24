#下载视频.py

import requests
from bs4 import BeautifulSoup
import bs4
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}

# 获取网页文本
def getHTMLText(url, headers):
	try:
		r = requests.get(url,  timeout = 30, headers = headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
	return ""

url = "https://www.bilibili.com/"

txt = getHTMLText(url, headers)

soup = BeautifulSoup(txt, "html.parser")