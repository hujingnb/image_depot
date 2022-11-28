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
    链接存在有效期
    
    url: https://riyugo.com/
    """
    NiuPic = auto()
    """
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
    Ai58 = auto()
    """
    58同城客服, 在线上传图片
    
    url: https://ai.58.com
    """
    Github = auto()
    """
    url: https://github.com
    """
