"""
@author hujing
"""
from enum import Enum, auto


class DepotType(Enum):
    CatBox = auto()
    """
    图床
    
    url: https://catbox.moe/
    """
    PngCm = auto()
    """
    图床
    
    url: https://png.cm/
    """
    Riyugo = auto()
    """
    限制: 
        1. 图片3天内有效
    url: https://riyugo.com/
    """
    NiuPic = auto()
    """
    牛客网
    
    url: https://www.niupic.com/
    """
    ImgUrl = auto()
    """
    免费账户有上传限制:
        1. 每日限制上传15张图片
        2. 每月限制上传400张
    图片链接限制: 
        1. 浏览器直接打开图片时, 会重定向到图床网址
    url: https://www.imgurl.org/
    """
    SmMs = auto()
    """
    限制: 
        1. 免费账号限制存储空间(可注册多个账号)
        2. 图片链接空 referer 访问时, 会重定向到图床网址
    url: https://sm.ms/
    """
    Imgbb = auto()
    """
    限制: 
        1. 图片链接空 referer 访问时, 会重定向到图床网址
    url: https://imgbb.com/
    """
    Xywm = auto()
    """
    图床
        1. 注册用户存在限制, 可能登录后查看
            * 限制并发数量及上传数量
    
    url: https://pic.xywm.ltd/
    """
    BoLuo = auto()
    """
    图床, 限制: 
        1. 每天限制上传10张
    url: https://www.boluo.link/
    """
    ImgAx = auto()
    """
    url: https://img.ax/
    """
    HuaBan = auto()
    """
    花瓣网站的图片上传. 图片上传接口在图集上传处发现
    
    限制: 
        1. 需要先登录
        2. 图片做了 referer 判断, 空 referer 可访问
    url: https://huaban.com/
    """
    Ai58 = auto()
    """
    58同城客服, 在线上传图片
    
    url: https://ai.58.com
    """
    Github = auto()
    """
    借用 github 仓库
    
    url: https://github.com
    """
