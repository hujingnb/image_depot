from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class NiuPic(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.NiuPic

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        files = {
            'file': content,
        }
        response = requests.post('https://www.niupic.com/api/upload', files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        data = response.json()
        if data.get('code') != 200 or not data.get('data'):
            return self._set_error(response.text)
        return data.get('data')
