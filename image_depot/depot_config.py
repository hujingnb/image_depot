"""
@author hujing
"""
from .depot.sm_ms import set_config as sm_ms_set_config
from .depot.github import set_config as github_set_config


class DepotConfig:
    SmMs = sm_ms_set_config
    Github = github_set_config
