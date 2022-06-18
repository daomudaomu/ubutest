import requests
import json
from lxml import etree
import jsonpath
import pandas as pd
import pyecharts

F_url='https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
data={
'modules': 'statisGradeCityDetail,diseaseh5Shelf'
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

response=requests.post(url=F_url,data=data,headers=headers)
content=response.text
# print(content)
# with open('../sourese/疫情数据.json','w',encoding='utf-8')as fp:
#     fp.write(content)
obj=json.load(open('../sourese/疫情数据.json','r',encoding='utf-8'))
# json path获取数据
# 城市名
name=jsonpath.jsonpath(obj,'$..areaTree.0.children.*.name')
# 累计数
confirm=jsonpath.jsonpath(obj,'$..areaTree.0.children.*.total.confirm')
# 现有
nowConfirm=jsonpath.jsonpath(obj,'$..areaTree.0.children.*.total.nowConfirm')
# 今日新增
todayconfirm=jsonpath.jsonpath(obj,'$..areaTree.0.children.*.today.confirm')
# 死亡数
dead=jsonpath.jsonpath(obj,'$..areaTree.0.children.*.total.dead')
# 治愈
heal=jsonpath.jsonpath(obj,'$..areaTree.0.children.*.total.heal')

# for i in range(len(name)):
#     print('省或特区名字: '+name[i]+' '+'累计确诊: '+str(confirm[i])+' '+'现有确诊: '+str(nowConfirm[i])+' '+'今日新增：'+str(todayconfirm[i])+' '+'死亡数：'+str(dead[i])+' '+'治愈数: '+str(heal[i]))
#     print('\n')

# 数据处理：
# data_set=[]
# for i in range(len(name)):
#     data_dict={}
#     data_dict['省或城市']=name[i]
#     data_dict['累计确诊']=confirm[i]
#     data_dict['现有确诊']=nowConfirm[i]
#     data_dict['今日新增']=todayconfirm[i]
#     data_dict['死亡数']=dead[i]
#     data_dict['康复数']=heal[i]
#     data_set.append(data_dict)
# df=pd.DataFrame(data_set)
# df.to_csv('疫情数据.csv')

# 制作中国地图一样的确诊人数图

# from pyecharts import options as opts
# from pyecharts.charts import Map
# from pyecharts.faker import Faker
#
# c = (
#     Map()
#     .add("确诊人数", [list(z) for z in zip(name, confirm)], "china")
#     .set_global_opts(title_opts=opts.TitleOpts(title="今日中国疫情确诊人数统计"))
#     .render("中国地图显示疫情情况.html")
# )

# from pyecharts.charts import Bar
# from pyecharts.faker import Faker
# from pyecharts.globals import ThemeType
#
# from pyecharts import options as opts
# from pyecharts.charts import Bar
# from pyecharts.faker import Faker
#
# c = (
#     Bar()
#     .add_xaxis(name)
#     .add_yaxis("商家A", dead)
#     .add_yaxis("商家B", heal)
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
#         toolbox_opts=opts.ToolboxOpts(),
#         legend_opts=opts.LegendOpts(is_show=False),
#     )
#     .render("bar_toolbox.html")
# )

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add("", [list(z) for z in zip(name, confirm)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
)


