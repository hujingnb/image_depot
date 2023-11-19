from typing import Optional
from .base import Depot


class NoneType(Depot):
    @classmethod
    def depot_type(cls) -> None:
        return None

    def __init__(self, type):
        super().__init__()
        self._type = type

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        return self._set_error(f'{self._type} not support or is delete')