# 介绍

在上传图片的时候, 经常会用到图床功能.

此工具聚合了一些常用的图床, 以便于快速使用. 免费图床大部分都不支持定义文件名称

# 说明

因为使用各种免费服务, 稳定性无法保证

若各位在使用过程中碰到问题, 欢迎下列任选一种方式补充: 

1. 提交`isuse`说明问题
2. 将问题写到`DepotType`的对应文档上

如果你有其他优秀的图床推荐, 欢迎提交`isuse`或`PR`

当前支持的所有图床, 可查看文件[DepotType](./image_depot/depot_type.py)

# 使用

安装: 

```shell
pip install image-depot
```

```python
from image_depot import image_depot, DepotType

# 选择图床对象
d = image_depot(DepotType.CatBox)

# 上传图片. 二进制内容
image_content = ''
image_url = d.upload(image_content)
if not image_url:  # 图片上传失败, 获取失败原因
    print(d.error())
# 上传图片, 使用本地文件路径
file_path = ''
image_url = d.upload_file(file_path)
```

