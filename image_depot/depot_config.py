"""
@author hujing
"""
from .depot.sm_ms import set_config as sm_ms_set_config
from .depot.github import set_config as github_set_config
from .depot.img_url import set_config as img_url_set_config
from .depot.hua_ban import set_config as hua_ban_set_config
from .depot.xywm import set_config as xywm_set_config
from .depot.pomf_se import set_config as pomf_se_set_config


def _default_set_config(*arg1, **arg2):
    """
    此函数无实际意义. 为了向后兼容
    若未来某个图床失效了, 需要将其实现删除
    此时, 为了保证调用方升级后不保存, set_config 函数需要保留
    可以使用此函数进行替代
    :param arg1:
    :param arg2:
    :return:
    """
    pass


class DepotConfig:
    SmMs = sm_ms_set_config
    Github = github_set_config
    ImgUrl = img_url_set_config
    HuaBan = hua_ban_set_config
    Xywm = xywm_set_config
    PomfSe = pomf_se_set_config
