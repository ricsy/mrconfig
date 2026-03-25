"""多路径配置文件加载器

支持 JSON、YAML、TOML 格式，兼容 Linux、macOS、Windows。
"""

__version__ = "0.1.0"

from .loader import ConfigLoader
from .loaders import JsonLoader, Loader, TomlLoader, YamlLoader
from .utils import load_config, xdg_config_path

__all__ = [
    "ConfigLoader",
    "JsonLoader",
    "Loader",
    "TomlLoader",
    "YamlLoader",
    "load_config",
    "xdg_config_path",
]
