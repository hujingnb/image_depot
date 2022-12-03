import random
import re
import time
import uuid
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class Hakaimg(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Hakaimg

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        data = {
            'uuid': 'o_' + self._random_str(27),
            'name': file_name,
        }
        files = {
            'file': content,
        }

        response = requests.post('https://hakaimg.com/file.php', data=data, files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. status: {response.status_code}')
        data = response.json()
        if not data:
            return self._set_error(f'content is error. {response.text}')
        # 上传失败
        if data.get('result') != 'success':
            return self._set_error(f'upload fail. {response.text}')
        # 上传成功, 但图片链接为空
        url = data.get('url')
        if not url:
            return self._set_error(f'success but not image. {response.text}')
        return url
