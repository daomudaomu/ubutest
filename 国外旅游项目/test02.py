name='a'
address='b'
web='c'
infor_address='d'
tel='e'
rate='f'

sql = 'insert into tour(name,address,web,inf_address,tel,rate)values("{}","{}","{}","{}","{}","{}")'.format(name,address,web,infor_address,tel,rate)
print(sql)