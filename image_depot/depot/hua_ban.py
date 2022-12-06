from typing import Optional
from image_depot import DepotType
from .base import Depot
import requests


class HuaBan(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.HuaBan

    def _upload(self, content) -> Optional[str]:
        cookie = self._config.hua_ban.cookie
        if not cookie:
            return self._set_error('cookie is empty')
        files = {
            'file': content,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36',
            'Cookie': cookie,
        }
        response = requests.post('https://api.huaban.com/upload', files=files, headers=headers)
        if response.status_code != 200:
            return self._set_error(f'request fail. code: {response.status_code}')
        data = response.json()
        if not data:
            return self._set_error(f'parse response error. {response.text}')
        # 拼接图片链接
        bucket = data.get('bucket')
        key = data.get('key')
        if not bucket or not key:
            return self._set_error(f'upload fail. {response.text}')
        return f'https://{bucket}.huaban.com/{key}'
