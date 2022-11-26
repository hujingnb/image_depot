import os
from abc import abstractmethod, ABC
from typing import Optional

import magic

from image_depot import DepotType
from .error import DepotError


class Depot(ABC):
    def __init__(self):
        self._err = None

    @classmethod
    @abstractmethod
    def depot_type(cls) -> DepotType:
        """
        当前类型
        :return:
        """
        pass

    # 上传图片, 二进制内容
    @abstractmethod
    def upload(self, content) -> Optional[str]:
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

    def _set_error(self, err) -> None:
        self._err = DepotError(err, back_num=1)
        return None

    @staticmethod
    def _get_mime_type(content):
        """
        识别文件的 mime type
        :param content:
        :return:
        """
        return magic.Magic(mime=True, uncompress=True).from_buffer(content)
