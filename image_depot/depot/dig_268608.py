from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class Dig268608(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Dig268608

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        files = {
            "file": (file_name, content)
        }
        response = requests.post('https://www.268608.com/upload/localhost', files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        data = response.json()
        url = data.get('url')
        if data.get('code') != 200 or not url:
            return self._set_error(f'response error. {response.text}')
        return url
