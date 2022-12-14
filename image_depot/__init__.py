"""
图床

使用方式:
  1. 指定仓库上传文件
    d = image_depot(DepotType.CatBox) # 获取仓库对象
    if d is None:  # 当前图床已失效
        pass
    url = d.upload(image_content) #  上传二进制内容
    url = d.upload_file(file_path) # 上传文件
    if not url:  # 图片上传失败, 获取失败原因
        print(d.error())
  2. 依次尝试所有仓库, 返回首个上传成功的链接
    url, err = upload(image_content)
    url, err = upload_file(file_path)

配置:
  部分仓库需要进行配置才能使用, 例如配置 sm.ms 图床
    config = DepotConfig()
    config.sm_ms.token = ''
    # 全局配置
    set_global_config(config)
    # 单次上传配置
    d = image_depot(DepotType.CatBox)
    d.set_config(config)

"""
from .depot_type import DepotType
from .image_depot import image_depot, upload, upload_file
from .depot import DepotConfig, set_global_config, get_config_by_dict

