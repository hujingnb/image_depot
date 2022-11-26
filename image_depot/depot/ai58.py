import base64
import json
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class Ai58(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Ai58

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        data = {
            'Pic-Size': '0*0',
            'Pic-Encoding': 'base64',
            'Pic-Path': '/nowater/webim/big/',
            'Pic-Data': base64.b64encode(content).decode('utf-8'),
        }
        headers = {
            'Origin': 'https://ai.58.com',
            'Referer': 'https://ai.58.com/pc/'
        }
        response = requests.post('https://upload.58cdn.com.cn/json', data=json.dumps(data), headers=headers)
        if response.status_code != 200:
            return self._set_error('upload fail')
        if not response.text:
            return self._set_error('content is empty')
        return f'https://pic3.58cdn.com.cn/nowater/webim/big/{response.text}'
