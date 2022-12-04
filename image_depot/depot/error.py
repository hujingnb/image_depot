"""
定义仓库异常
@author hujing
"""


class DepotError:
    def __init__(self, err, tb):
        """
        :param err:
        :param tb: 堆栈信息
        """
        self._err = err
        self._traceback = tb

    def error(self):
        return self._err

    def traceback(self):
        return self._traceback

    def __str__(self):
        return self.error() + '\n' + \
            self.traceback()
