import os
import uuid
from abc import abstractmethod, ABC
from typing import Optional
import filetype
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
        if not suffix:
            return self._set_error(f'parse mimetype error.')
        os.remove(tmp_file)
        return str(uuid.uuid4()) + '.' + suffix
