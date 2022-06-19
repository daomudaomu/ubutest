import requests
import urllib.request
from lxml import etree

xm_url='https://www.tripadvisor.com/Restaurant_Review-g45963-d5965897-Reviews-Delhi_Indian_Cuisine-Las_Vegas_Nevada.html'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
response=requests.get(url=xm_url,headers=headers)

content=response.text

tree=etree.HTML(content)
with open('test02.html','w',encoding='utf-8')as fp:
    fp.write(content)
infor_adress=tree.xpath('//div[@class="cSPba bKBJS Me"]/span[2]/a/span/text()')
tel=tree.xpath('//*[@id="component_51"]/div[1]/div/div[3]/div/div/div[4]/div/a/@href')
price=tree.xpath('//*[@id="component_51"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/text()')
custom=tree.xpath('//*[@id="component_51"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/text()')
food=tree.xpath('//*[@id="component_51"]/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/text()')
print(food)
print(custom)
print(price)
print(tel)
print(infor_adress)