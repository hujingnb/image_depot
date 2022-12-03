"""
@author hujing
"""
import os
from typing import List, Optional
from .depot import Depot, DEPOT_MAP, DepotError
from .depot_type import DepotType


def image_depot(t: DepotType) -> Optional[Depot]:
    """
    根据 type 获取仓库对象
    :param t:
    :return:
    """
    if t in DEPOT_MAP:
        return DEPOT_MAP[t]()
    return None


def upload(content, type_list: List[DepotType] = None) -> (str, List[DepotError]):
    """
    按照指定的类型依次上传, 直到首次上传成功则返回
    若依次尝试后, 均失败, 则返回 None
    :param content:
    :param type_list: 若不指定, 则默认使用所有类型
    :return:
        str: 上传成功后的地址 <br>
        err: 若上传失败, 此数组保存所有失败原因
    """
    err = []
    if not type_list:
        type_list = DepotType
    for item in type_list:
        d = image_depot(item)
        if not d:
            continue
        ret = d.upload(content)
        if ret:
            return ret, err
        else:
            err.append(d.error())
    return None, err


def upload_file(file_path: str, type_list: List[DepotType] = None) -> (str, List[DepotError]):
    if not os.path.exists(file_path):
        return None, [DepotError(f'file {file_path} not exist')]
    with open(file_path, 'rb') as f:
        return upload(f.read(), type_list)
