import base64
import json
import mimetypes
import uuid
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot

USERNAME = ''  # 用户名
REPO = ''  # 仓库名
SAVE_PATH = ''  # 保存路径
TOKEN = ''
USE_JSDELIVR = False  # 是否使用 jsdelivr 加速


def set_config(username: str, repo: str, save_path: str, token: str, use_jsdelivr: bool = True):
    """
    :param username: 仓库用户名
    :param repo: 仓库名称
    :param save_path: 文件保存路径. eg: content/img
    :param token: 获取地址: https://github.com/settings/tokens <br>
        创建 token 时, 权限选中 repo 的所有
    :param use_jsdelivr: 是否使用 jsdelivr 加速 <br>
        若为 True, 则返回 jsdelivr 图片链接, 否则返回 github 链接 <br>
        默认为 True
    :return:
    """
    global USERNAME, REPO, SAVE_PATH, TOKEN
    USERNAME = username
    REPO = repo
    SAVE_PATH = save_path
    TOKEN = token
    USE_JSDELIVR = use_jsdelivr


class Github(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Github

    # 上传图片, 二进制内容
    def upload(self, content) -> Optional[str]:
        if not USERNAME or not REPO or not SAVE_PATH or not TOKEN:
            return self._set_error('config is miss')
        # 获取文件名称
        suffix = mimetypes.guess_extension(self._get_mime_type(content))
        file_name = str(uuid.uuid4()) + suffix
        url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{SAVE_PATH}/" + file_name  # 用户名、库名、路径
        data = {
            "message": "upload file",
            "content": base64.b64encode(content).decode()
        }
        headers = {
            "Authorization": "token " + TOKEN
        }
        response = requests.put(url=url, data=json.dumps(data), headers=headers)
        if response.status_code != 201 and response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}')
        # 获取图片链接
        url = response.json().get('content', {}).get('download_url')
        if not url:
            return self._set_error(f'response error. {response.text}')
        # 返回结果
        if USE_JSDELIVR:
            return f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}/{SAVE_PATH}/{file_name}"
        else:
            return url