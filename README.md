# 介绍

在上传图片的时候, 经常会用到图床功能.

此工具聚合了一些常用的图床, 以便于快速使用. 免费图床大部分都不支持定义文件名称

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

当前支持的所有上传方式可通过`DepotType`查看

# 其他

如果你有其他优秀的图床推荐, 欢迎提交`isuse`或`PR`
