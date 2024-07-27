import requests
from hashlib import md5
import math
import time

p=time.time() #获取时间戳

secretKey = "HIOWEHGW23-56803" 设置密钥
p=math.floor(p) #对时间戳进行处理
print(p)
m = md5() #创建MD5对象
pp=str(p) 
l=pp+secretKey
l=l.encode(encoding="ASCII")
m.update(bytes(l))
print(m.hexdigest())
token=m.hexdigest()
params1={'timestamp':p,'token':token}
print(params1)
x = requests.get('https://box.fiime.cn/random/random.php',params={'timestamp':p,'token':token},stream=True)
m=open(pp+".png",'wb')
m.write(x.content)
m.close()
