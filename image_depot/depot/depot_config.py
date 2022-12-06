"""
@author hujing
"""
from typing import Union


class ConfigBase:
    def __getattr__(self, name):
        """
        当属性未定义时会调用此方法, 直接返回 None, 防止报错
        :param name:
        :return:
        """
        return None

    def copy(self) -> 'ConfigBase':
        """
        当前类型深度克隆
        :return:
        """
        ret = self.__class__()
        for field in dir(self):
            if field.startswith('_'):
                continue
            value = getattr(self, field)
            if isinstance(value, ConfigBase):
                value = value.copy()
            setattr(ret, field, value)
        return ret


class DepotConfig(ConfigBase):
    class Smms(ConfigBase):
        """
        token 获取地址: https://sm.ms/home/apitoken \n
        """
        token: str

    sm_ms = Smms()

    class Github(ConfigBase):
        username: str  # 用户名
        repo: str  # 仓库名称
        token: str
        """
        获取地址: https://github.com/settings/tokens <br>
        创建 token 时, 权限选中 repo 的所有
        """
        save_path: str = ''  # 文件保存路径. eg: content/img
        use_jsdelivr: bool = True
        """
        是否使用 jsdelivr 加速 <br>
        若为 True, 则返回 jsdelivr 图片链接, 否则返回 github 链接 <br>
        默认为 True
        """
        branch: str = 'master'  # 指定分支名称, 分支必须存在. 默认'master'

    github = Github()

    class ImgUrl(ConfigBase):
        token: str  # 获取地址: https://www.imgurl.org/vip/manage/mytoken
        uid: str  # 与 token 一起获取

    img_url = ImgUrl()

    class HuaBan(ConfigBase):
        cookie: str
        """
        登录网站 https://huaban.com 后
        将请求 header 中的 cookie 取出
        """

    hua_ban = HuaBan()

    class Xywm(ConfigBase):
        email: str
        password: str

    xywm = Xywm()

    class PomfSe(ConfigBase):
        upload_url_list = [  # 修改此配置, 请确认您对需要的链接了解
            # https://fileditch.com/
            'https://up1.fileditch.com/upload.php',
            'https://qu.ax/upload.php',
            'https://midi.moe/upload.php',
            'https://cockfile.com/upload.php',
            'https://imouto.kawaii.su/api/upload',
            'https://safe.waifuhunter.club/api/upload',
            'https://take-me-to.space/api/upload',
            'https://files.htp.sh/api/upload',
            'https://pomf.lain.la/upload.php',
            'https://smutty.horse/upload.php',
            'https://stuff.poxydoxy.com/upload.php',
            # 48小时候自动过期
            'https://uguu.se/upload.php',
            # 24小时过期
            'https://cockfile.com/upload.php',
        ]

    pomf_se = PomfSe()

    class Tucang(ConfigBase):
        # 配置的获取请参考: http://doc.tucang.cc/project-1/doc-7/
        token: str
        folder_id: str = 0

    tucang = Tucang()


_global_config = DepotConfig()


def get_config_by_dict(data: dict) -> Union[DepotConfig, ConfigBase]:
    """
    使用字典初始化配置
    外部配置可使用 yaml/json/xml 等不限, 自行转换为字典即可
    :param data:
    :return:
    """
    ret = DepotConfig()

    def set_config_by_dict(obj: ConfigBase, tmp_data: dict):
        for field in tmp_data:
            if not hasattr(obj, field):
                continue
            value = getattr(obj, field)
            if isinstance(value, ConfigBase):
                set_config_by_dict(value, tmp_data.get(field))
            else:
                setattr(obj, field, tmp_data.get(field))

    set_config_by_dict(ret, data)
    return ret


def set_global_config(config: DepotConfig):
    global _global_config
    _global_config = config


def get_global_config() -> DepotConfig:
    return _global_config
