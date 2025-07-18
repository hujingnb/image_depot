"""
@author hujing
"""
from enum import Enum, auto


class DepotType(Enum):
    CatBox = auto()
    """
    图床
    
    url: https://catbox.moe/
    
    image: https://files.catbox.moe/pzchfp
    
    注意: 
        * 此图床国内无法访问
    """

    PomfSe = auto()
    """
    一类图床. 使用同一套框架运行, 上传接口一致. 
        * 不同人维护的不同服务.
        * 因此这里提供一个类型, 可配置上传连接 
        * 此服务可靠性应该是不高
    限制: 不同服务的限制不同
    
    配置: 
        * 可以不修改配置
        * 留出配置文件是为了防止所有服务都不能用了, 可以自定义上传接口
    
    可通过下方链接找到相似的站点,
        * 链接: https://pomf.se/
        * 上传参数: files[] (指定上传文件)
        * 响应: {"success": true, "files": [{"url": "xxx"}]} 
    
    注意: 
        * 默认配置的服务中存在会过期的图床, 使用时请确认
    
    url: https://pomf.se/
    
    image: https://s1.fileditch.ch/eUrajjLmzsKuXEDRzaBZ.jpg
    """

    Riyugo = auto()
    """
    限制: 
        1. 图片3天内有效
        2. 单文件最大5M
        3. 免费版, 页面22:00 ~ 07:00 关闭上传功能
    url: https://zixiaoyun.com/
    
    image: https://beta.glilmu.com/i/2022/12/04/p6eo39.png
    """

    ImgUrl = auto()
    """
    免费账户有上传限制:
        1. 每日限制上传15张图片
        2. 每月限制上传400张
    图片链接限制: 
        1. 浏览器直接打开图片时, 会重定向到图床网址
    url: https://www.imgurl.org/
    
    image: https://s3.uuu.ovh/imgs/2022/12/04/568047dc209095c7.jpg
    """

    SmMs = auto()
    """
    限制: 
        1. 免费账号限制存储空间(可注册多个账号)
        2. 图片链接空 referer 访问时, 会重定向到图床网址
        3. 每分钟上传限制20张
        4. 每日上传限制100张
    url: https://sm.ms/
    
    image: https://s2.loli.net/2022/12/04/XDt4H1zyMi6QvJ7.jpg
    """

    Imgbb = auto()
    """
    限制: 
        1. 图片链接空 referer 访问时, 会重定向到图床网址
    注意: 
        * 此图床国内无法访问
    url: https://imgbb.com/
    
    image: https://i.ibb.co/Qnjwwy4/source.jpg
    """

    Xywm = auto()
    """
    图床
        1. 注册用户存在限制, 可能登录后查看
            * 限制并发数量及上传数量
    
    url: https://pic.160320.xyz/
    
    image: https://p1.xywm.ltd/2022/12/04/638c4d21b9060.jpg
    """

    BoLuo = auto()
    """
    图床, 限制: 
        1. 每天限制上传50张, 每月上传1000张 (可自行付费扩容)
        2. 必须注册
    url: https://www.boluo.link/
    
    image: https://s1.boluo.link/imgs/2022/12/04/7bde14bb7169b7f2.jpg
    """

    Postimages = auto()
    """
    缺点: 
        1. 每次上传图片需要访问3次接口
        2. 图片链接空 referer 访问时, 会重定向到图床网址
    url: https://postimages.org/
    """

    Hakaimg = auto()
    """
    url: https://hakaimg.com/
    
    image: https://hakaimg.com/i/2022/12/04/pd0mkv.jpg
    """

    Tucang = auto()
    """
    图仓
    url: https://tucang.cc/
    
    image: https://img.tucang.cc/api/image/show/87917ba87bde14bb7169b7f225e430ac
    """

    HuaBan = auto()
    """
    花瓣网站的图片上传. 图片上传接口在图集上传处发现
    
    限制: 
        1. 需要先登录
        2. 图片做了 referer 判断, 空 referer 可访问
    url: https://huaban.com/
    
    image: https://gd-hbimg.huaban.com/670abb2c3e9db5ae69395775b5eb440730fdb4b43e39-viueHl
    """

    Ai58 = auto()
    """
    58同城客服, 在线上传图片
    
    url: https://ai.58.com
    
    image: https://pic3.58cdn.com.cn/nowater/webim/big/n_v2e0aa97ec21bb4f4581f365eff90a683c.jpg
    """

    Github = auto()
    """
    借用 github 仓库
    
    url: https://github.com
    
    image: https://cdn.jsdelivr.net/gh/hujingnb/img@test/content/img/f27ad12e-9bdb-4ab5-b2f7-91c0eff0ea55.jpg
    """

    PzAl = auto()
    """
    url: https://pz.al/
    
    image: https://f.pz.al/pzal/2023/11/19/37bd71a58ad86.jpg
    """

    Image23 = auto()
    """
    :deprecated
    限制: 
        1. 单文件最大5M
    url: https://23img.com/

    image: https://23img.com/i/2023/10/04/w7igrm.jpg
    """

    Dig268608 = auto()
    """
    :deprecated
    url: https://www.268608.com/

    image: https://www.268608.com/imgs/2022/12/04/7bde14bb7169b7f2.jpg
    """

    '''============================已不再支持的图床, 保留是为了旧版本升级不报错'''
    PngCm = auto()
    """
    :deprecated
    图床

    url: https://png.cm/

    image: https://i2.100024.xyz/2022/12/04/p5v5mj.webp
    """

    NiuPic = auto()
    """
    :deprecated
    牛客网

    url: https://www.niupic.com/

    image: https://i.niupic.com/images/2022/12/04/abCy.png
    """

    ImgAx = auto()
    """
    :deprecated
    
    url: https://img.ax/

    image: https://img.urlnode.com/file/ccd2064575362a738e943.jpg
    """
