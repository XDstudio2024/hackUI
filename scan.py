import time
from tqdm import tqdm
user = input('输入搜索网段(1~255)')
for i in tqdm(range(100),desc="正在扫描..."):
    time.sleep(0.01)
for i in range(1,256):
    print('扫描到ip','192.168.'+user+'.'+str(i))
    time.sleep(0.1)
print('扫描完成(此网段已满)')
