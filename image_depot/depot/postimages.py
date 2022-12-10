import json
import re
import time
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class Postimages(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Postimages

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        # 访问主页获取 token
        response = requests.get('https://postimages.org/')
        if response.status_code != 200:
            return self._set_error(f'response fail. code: {response.status_code}')
        re_search = re.search(r'"token","(\w+)"', response.text)
        if not re_search:
            return self._set_error('parse token fail')
        token = re_search.group(1)
        # 上传图片
        data = {
            'token': token,
            'upload_session': self._random_str(32),
            'numfiles': 1,
            'ui': json.dumps(['', '', '', True, '', '', time.strftime("%Y/%m/%d %H:%M:%S")]),
            'optsize': '',
            'session_upload': int(time.time() * 1000),
            'gallery': '',
            'expire': 0,
        }
        files = {
            'file': content,
        }
        response = requests.post('https://postimages.org/json/rr', data=data, files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        web_url = response.json().get('url')
        if not web_url:
            return self._set_error(f'parse error. {response.text}')
        # 获取图片链接
        response = requests.get(web_url)
        if response.status_code != 200:
            return self._set_error(f'got image url fail. code: {response.status_code}')
        re_search = re.search(r'meta\s*[\w="]+og:image[\s"\w=]+"([\w:/.]+)"', response.text)
        if not re_search:
            return self._set_error('parse image fail')
        return re_search.group(1)
