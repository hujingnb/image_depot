import os
import random
import traceback
import uuid
from abc import abstractmethod, ABC
from typing import Optional
import filetype
from image_depot import DepotType
from .depot_config import DepotConfig, get_global_config
from .error import DepotError


class Depot(ABC):
    _config: DepotConfig

    def __init__(self):
        self._err = None
        self._config = get_global_config()

    @classmethod
    @abstractmethod
    def depot_type(cls) -> DepotType:
        """
        当前类型
        :return:
        """
        pass

    def set_config(self, config: DepotConfig):
        """
        次函数用于自定义配置
        :return:
        """
        self._config = config

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        try:
            return self._upload(content)
        except Exception as e:
            tb = traceback.format_exc()
            return self._set_error(e, tb)

    @abstractmethod
    def _upload(self, content) -> Optional[str]:
        pass

    # 上传图片, 本地路径
    def upload_file(self, file_path) -> Optional[str]:
        if not os.path.exists(file_path):
            return self._set_error(f'file {file_path} not exist')
        with open(file_path, 'rb') as f:
            return self.upload(f.read())

    def error(self) -> Optional[DepotError]:
        """
        获取错误信息
        :return:
        """
        if self._err:
            return self._err
        return None

    def _set_error(self, err, tb: str = '') -> None:
        if not tb:  # 未指定堆栈信息, 获取调用方
            tb = traceback.extract_stack()[0:-1]
            tb = ''.join(traceback.format_list(tb))
        self._err = DepotError(str(err), tb)
        return None

    def _random_str(self, length: int, rand_str: str = None):
        """
        获取指定长度的随机字符串
        :param length:
        :param rand_str:
        :return:
        """
        if not rand_str:
            rand_str = '0123456789abcdefghijklmnopqrstuvwxyz'
        return ''.join(random.sample(list(rand_str) * length, length))

    def _random_file_name(self, content):
        """
        获取随机的文件名, 会自动识别文件后缀
        :param content:
        :return:
        """
        # 创建临时文件, 获取文件后缀
        tmp_file = '/tmp/' + str(uuid.uuid4())
        with open(tmp_file, 'wb') as f:
            f.write(content)
        suffix = filetype.guess_extension(tmp_file)
        os.remove(tmp_file)
        if not suffix:
            return self._set_error(f'parse mimetype error.')
        return str(uuid.uuid4()) + '.' + suffix
