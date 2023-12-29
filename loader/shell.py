import time
from tqdm import tqdm,tgrange
import random

# v1原有功能(2023/12/23)
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
for i in tqdm(range(100),desc='正在获取root权限',colour="red"):
    time.sleep(0.1)
print('root权限获取成功!')
time.sleep(2)
# v2
print('-------------------------------------------------')
print('可用命令列表')
print('config:查看当前系统信息')
print('exit:退出')
print('restore:恢复目标系统')
print('-------------------------------------------------')

while True:
    cmd = input('>')
    if cmd == 'exit':
        break
    elif cmd == 'config':
        print('正在生成配置文件...')
        time.sleep(2)
        print('ip','none')
        print('port','none')
        print('os','none')
        print('root','shell')
    elif cmd == 'restore':
        for i in tqdm(range(100),desc='正在下载Ubuntu'):
            time.sleep(0.01)
        for i in tqdm(range(100),desc='正在还原GRUB'):
            time.sleep(0.01)
        for i in tqdm(range(100),desc='正在生成可用的配置文件'):
            time.sleep(0.01)
        for i in tqdm(range(100),desc='正在应用配置文件',colour = 'red'):
            time.sleep(0.1)
        for i in tqdm(range(10),desc='正在尝试连接',colour = 'green'):
            time.sleep(0.1)
        print('系统已还原!')
# 此功能已归档