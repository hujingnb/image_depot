from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class CatBox(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.CatBox

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        data = {
            'reqtype': 'fileupload',
            'userhash': '',
        }
        files = {
            'fileToUpload': content,
        }
        response = requests.post('https://catbox.moe/user/api.php', data=data, files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        return response.text
