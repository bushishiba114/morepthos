import requests
from hashlib import md5
import math
import time
import os


secretKey = "HIOWEHGW23-56803" 
os.mkdir('l')
for i in range(9):
    p=time.time() 
    p=math.floor(p) 
    print(p)
    m = md5() 
    pp=str(p) 
    l=pp+secretKey
    l=l.encode(encoding="ASCII")
    m.update(bytes(l))
    print(m.hexdigest())
    token=m.hexdigest()
    params1={'timestamp':p,'token':token}
    print(params1)
    x = requests.get('https://box.fiime.cn/random/random.php',params={'timestamp':p,'token':token},stream=True)
    m=open('l//'+pp+".png",'wb')
    m.write(x.content)
    m.close()
    time.sleep(5)
