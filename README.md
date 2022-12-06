# 介绍

在上传图片的时候, 经常会用到图床功能.

此工具聚合了一些常用的图床, 以便于快速使用.

*注意: 因免费图床的稳定性无法保证, 因此请勿用其保存重要文件*

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
from image_depot import image_depot, DepotType, upload, upload_file, DepotConfig, set_global_config

# 部分图床需要添加配置才能使用
config = DepotConfig()
config.sm_ms.token = ''
# 全局配置
set_global_config(config)

# 选择图床对象
d = image_depot(DepotType.CatBox)
if d is None:  # 当前图床已失效
    pass
# 可以为每次上传使用不同的配置信息
# 此配置优先级高于 global_config
d.set_config(config)  

# 上传图片. 二进制内容
image_content = ''
image_url = d.upload(image_content)
if not image_url:  # 图片上传失败, 获取失败原因
    print(d.error())
# 上传图片, 使用本地文件路径
file_path = ''
image_url = d.upload_file(file_path)

# 依次尝试所有图床, 返回第一个成功的. 
url, err = upload(image_content)
upload_file(file_path)
```

