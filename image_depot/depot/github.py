import base64
import json
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class Github(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Github

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        conf = self._config.github
        if not conf.username or \
                not conf.repo or \
                not conf.save_path or \
                not conf.token:
            return self._set_error('config is miss')
        # 获取文件名称
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        url = f"https://api.github.com/repos/{conf.username}/{conf.repo}/" \
              f"contents/{conf.save_path}/" \
              + file_name  # 用户名、库名、路径
        data = {
            "message": "upload file",
            "content": base64.b64encode(content).decode(),
            'branch': conf.branch
        }
        headers = {
            "Authorization": "token " + conf.token
        }
        response = requests.put(url=url, data=json.dumps(data), headers=headers)
        if response.status_code != 201 and response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        # 获取图片链接
        url = response.json().get('content', {}).get('download_url')
        if not url:
            return self._set_error(f'response error. {response.text}')
        # 返回结果
        if conf.use_jsdelivr:
            return f"https://cdn.jsdelivr.net/gh/{conf.username}/{conf.repo}@" \
                   f"{conf.branch}/{conf.save_path}/{file_name}"
        else:
            return url
