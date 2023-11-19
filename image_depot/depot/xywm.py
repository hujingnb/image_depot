import base64
from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class Xywm(Depot):
    def __init__(self):
        super().__init__()
        self._token = None

    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Xywm

    def _upload(self, content) -> Optional[str]:
        conf = self._config.xywm
        if not conf.api_key:
            return self._set_error('api_key is empty')
        # 上传图片
        data = {
            'source': base64.b64encode(content).decode('utf-8'),
        }
        headers = {
            "Accept": "application/json",
            'X-API-Key': conf.api_key
        }
        response = requests.post("https://pic.xywm.ltd/api/1/upload", headers=headers, data=data)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}')
        data = response.json()
        if data.get('status_code') != 200:
            return self._set_error(f'upload fail. {response.text}')
        url = data.get('image', {}).get('image', {}).get('url')
        if not url:
            return self._set_error(f'response error. {response.text}')
        return url
