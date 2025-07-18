from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class SmMs(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.SmMs

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        conf = self._config.sm_ms
        if not conf.token:
            return self._set_error('token is empty')
        data = {
            'format': 'json',
        }
        headers = {
            'Authorization': conf.token,
        }
        files = {
            'smfile': content,
        }

        response = requests.post('https://sm.ms/api/v2/upload', data=data, files=files, headers=headers, timeout=30)
        if response.status_code != 200:
            return self._set_error(f'upload fail. status: {response.status_code}')
        data = response.json()
        if not data:
            return self._set_error(f'content is error. {response.text}')
        # 上传失败
        if not data.get('success'):
            # 上传图片重复, 会将图片链接返回来
            if data.get('code') == 'image_repeated' and data.get('images'):
                return data.get('images')
            return self._set_error(f'upload fail. {response.text}')
        # 上传成功, 但图片链接为空
        url = data.get('data', {}).get('url')
        if not url:
            return self._set_error(f'success but not image. {response.text}')
        return url
