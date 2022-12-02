import re
import time
import uuid
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class SmMs(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.BoLuo

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        files = {
            'file': (file_name, content),
        }
        response = requests.post('https://www.boluo.link/upload/ftp', files=files)
        print(response.status_code)
        print(response.text)
        if response.status_code != 200:
            return self._set_error(f'upload fail. status: {response.status_code}')
        data = response.json()
        if not data:
            return self._set_error(f'content is error. {response.text}')
        # 上传失败
        if data.get('code') != 200:
            return self._set_error(f'upload fail. {response.text}')
        url = data.get('url')
        if not url:
            return self._set_error(f'success but not image. {response.text}')
        return url
