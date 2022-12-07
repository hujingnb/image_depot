from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class NiuPic(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.NiuPic

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        files = {
            'file': (file_name, content),
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36',
            'origin': 'https://www.niupic.com',
            'referer': 'https://www.niupic.com/',
        }
        response = requests.post('https://www.niupic.com/api/upload', files=files, headers=headers)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        data = response.json()
        if data.get('code') != 200 or not data.get('data'):
            return self._set_error(response.text)
        return data.get('data')
