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
    链接存在有效期 \n
    url: https://riyugo.com/
    """
    NiuPic = auto()
    """
    url: https://www.niupic.com/
    """
    SmMs = auto()
    """
    需要配置 \n
    免费存储空间限制, 可注册多个账号 \n
    图片链接空 referer 访问时, 会重定向到图床网址 \n
    url: https://sm.ms/
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
