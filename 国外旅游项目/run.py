import requests
import urllib.request
from lxml import etree
import pymysql
datalist = []
def get_firsturl(url):
    xm_url = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    response = requests.get(url=xm_url, headers=headers)
    content = response.text
    tree = etree.HTML(content)

    with open('test01.html', 'w', encoding='utf-8') as fp:
        fp.write(content)

    xname = tree.xpath('//div[@class="OhCyu"]//a/text()')
    xadress = tree.xpath('//div[@class="bhDlF bPJHV eQXRG"]/span[1]/span/text()')
    rates = tree.xpath('//span[@class="bFlvo"]/*[name()="svg"]/@aria-label')
    urls = tree.xpath('//div[@class="OhCyu"]/span/a/@href')
    # 在列表urls中每个元素前加上https://www.tripadvisor.com，形成新的列表
    new_urls = []
    for url in urls:
        new_urls.append('https://www.tripadvisor.com' + url)

    # 获取列表中非数字，非符号的元素，生成新的列表
    xname_new = []
    for i in xname:
        if i.isdigit() or i == '. ':
            continue
        else:
            xname_new.append(i)

    for i in range(len(xname_new)):
        data = []
        name=xname_new[i]
        address=xadress[i]
        rate=rates[i]
        url=new_urls[i]
        data.append(name)
        data.append(address)
        data.append(rate)
        data.append(url)
        datalist.append(data)
    return datalist

def get_son_url(url,i):
    xm_url =url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    response = requests.get(url=xm_url, headers=headers)
    content = response.text
    tree = etree.HTML(content)

    infor_adress = tree.xpath('//div[@class="cSPba bKBJS Me"]/span[2]/a/span/text()')
    tels = tree.xpath('//div[@class="bKBJS Me"]/a/span/span[2]/text()')

    for j in range(len(infor_adress)):
        infaddress=infor_adress[j]
        tel=tels[j]

    datalist[i].append(infaddress)
    datalist[i].append(tel)

def save_mysql(datalist):
    init_db()  # 创建表
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306,
        charset='utf8',
        db='bosstest'
    )
    # 创建游标
    cursor = conn.cursor()
    i = 0
    for ex in datalist:
        i = i + 1
        # 工作名称
        name = ex[0]
        # 工作地点
        area = ex[1]
        # 公司名称
        company_name = ex[2]
        # 公司类型
        company_type = ex[3]
        # 薪资待遇
        money = ex[4]
        # 经验学历
        exp = ex[5]
        # 标签
        tags = ex[6]
        # 福利待遇
        boon = ex[7]
        try:
            sql = 'insert into `%s`(name,area,company_name,company_type,money,exp,tags,boon)values("{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                name, area, company_name, company_type, money, exp, tags, boon) % (KeyWord)
            cursor.execute(sql)
            conn.commit()
            print(f"正在保存第{i}条数据")
            # print(sql)
        except:
            print("数据有问题" + name)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    for k in range(1,11):
        if k==1:
            url='https://www.tripadvisor.com/RestaurantSearch?Action=FILTER&ajax=1&availSearchEnabled=false&sortOrder=relevance&geo=45963&itags=10591&zfp=10600'
        else:
            url='https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=false&sortOrder=popularity&geo=45963&itags=10591&o=a'+str(30*(k-1))
        get_firsturl(url)
        for i in range(len(datalist)):
            print(i)
            get_son_url(datalist[i][3], i)
        print(datalist)
        save_mysql()
        datalist.clear()
        print(datalist)
        if k==3:
            break




