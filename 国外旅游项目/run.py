import requests
import urllib.request
from lxml import etree

xm_url='https://www.tripadvisor.com/RestaurantSearch?Action=FILTER&ajax=1&availSearchEnabled=false&sortOrder=relevance&geo=45963&itags=10591&zfp=10600'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
response=requests.get(url=xm_url,headers=headers)

content=response.text

tree=etree.HTML(content)
with open('test01.html','w',encoding='utf-8')as fp:
    fp.write(content)
xname=tree.xpath('//div[@class="OhCyu"]//a/text()')
xadress=tree.xpath('//div[@class="bhDlF bPJHV eQXRG"]/span[1]/span/text()')
rate=tree.xpath('//span[@class="bFlvo"]/*[name()="svg"]/@aria-label')
urls=tree.xpath('//div[@class="OhCyu"]/span/a/@href')
#在列表urls中每个元素前加上https://www.tripadvisor.com，形成新的列表
new_urls=[]
for url in urls:
    new_urls.append('https://www.tripadvisor.com'+url)
print(new_urls)
#获取列表中非数字，非符号的元素，生成新的列表
xname_new=[]
for i in xname:
    if i.isdigit() or i=='. ':
        continue
    else:
        xname_new.append(i)
print(xname_new)
print(xadress)
print(rate)
print(len(xname_new),len(xadress),len(rate),len(new_urls))








# xmimgurl=tree.xpath('//img[@class="c-img-img"]/@src')
# for i in range(len(xmname)):
#     urllib.request.urlretrieve(xmimgurl[i],'../sourse/项目图片/'+xmname[i]+'.jpg')