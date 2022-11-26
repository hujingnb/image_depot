import os
from .base import Depot
from .error import DepotError

# 整理所有的类型 map, 方便获取的时候加速
DEPOT_MAP = {}

"""
将当前目录下的所有文件导入
目的是在使用的时候无需关注具体有哪些子类
添加子类文件后即可创建新的仓库, 无需修改其他额外内容
"""
for file in os.listdir(os.path.dirname(__file__)):
    # 解析, 将文件名后缀去掉
    name = os.path.basename(file).split('.')[0]
    exec(f'from .{name} import *')

for item in Depot.__subclasses__():
    DEPOT_MAP[item.depot_type()] = item

