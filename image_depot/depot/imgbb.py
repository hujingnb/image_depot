import re
import time
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class Imgbb(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Imgbb

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        session = requests.session()
        # 访问首页, 获取token
        response = session.get('https://imgbb.com/')
        if response.status_code != 200:
            return self._set_error(f'request fail. code: {response.status_code}')
        re_search = re.search(r'auth_token\s*=\s*"([\S\d]+)"', response.text)
        if not re_search:
            return self._set_error('parse token fail')
        token = re_search.group(1)

        data = {
            'type': 'file',
            'action': 'upload',
            'timestamp': int(time.time() * 1000),
            'token': token,
        }
        files = {
            'source': content,
        }
        response = session.post('https://zh-cn.imgbb.com/json', data=data, files=files)
        if response.status_code != 200:
            return self._set_error(f'request fail. code: {response.status_code}')
        #  检查返回数据
        data = response.json()
        status_code = data.get('status_code')
        if status_code != 200:
            return self._set_error(f'server return error. {response.text}')
        url = data.get('image', {}).get('url')
        if not url:
            return self._set_error(f'parse url fail. {response.text}')
        return url
