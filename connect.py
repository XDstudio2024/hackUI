import os
import sys
print('hackUI connect v1')
# v1原有功能
print('请输入你的服务器地址')
ip = input('ip:')
print(ip,'连接成功')
print('连接成功后会自动使用工具进行攻击，获取root权限')
os.system('python loader\shell.py')
sys.exit(0)