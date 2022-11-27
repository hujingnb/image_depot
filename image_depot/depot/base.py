import mimetypes
import os
import uuid
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

    def _get_mime_type(self, content):
        """
        识别文件的 mime type
        :param content:
        :return:
        """
        return magic.Magic(mime=True, uncompress=True).from_buffer(content)

    def _random_file_name(self, content):
        """
        获取随机的文件名, 会自动识别文件后缀
        :param content:
        :return:
        """
        mime_type = self._get_mime_type(content)
        # todo 系统的 mimetypes 识别度并不高, 很多类型都无法正常识别.
        #  后面若找到更好的, 替换掉. 若实际使用中喷到问题了, 自己维护转换 map
        suffix = mimetypes.guess_extension(mime_type)
        if not suffix:
            return self._set_error(f'parse mimetype error. mime_type: {mime_type}, suffix: {suffix}')
        if suffix == '.jpe':  # image/jpeg 类型会返回此后缀
            suffix = '.jpg'
        return str(uuid.uuid4()) + suffix
