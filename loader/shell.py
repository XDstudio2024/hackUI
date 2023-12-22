import time
from tqdm import tqdm,tgrange
import random

# 11
osn = ['ubuntu','centos','debian','redhat','fedora','opensuse','archlinux','gentoo','slackware','suse','m']
port = ['22','80','21','25','21','3306','3389']
for i in tqdm(range(4),desc='正在尝试连接'):
    time.sleep(1)
for i in tqdm(range(10),desc='正在尝试扫描信息'):
    time.sleep(0.1)
print('系统名称',osn[random.randint(0,10)] )
print('端口',port[random.randint(0,5)] )

time.sleep(5)
for i in tqdm(range(100),desc='正在生成可用攻击程序'):
    time.sleep(0.01)
for i in tqdm(range(100),desc='正在获取root权限'):
    time.sleep(0.1)
print('root权限获取成功!')
time.sleep(2)