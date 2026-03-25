# path-config

多路径配置文件加载器，支持 JSON、YAML、TOML 格式

## 安装

```bash
pip install path-config
```

## 支持格式

| 格式   | 扩展名             | 说明                    |
|------|-----------------|-----------------------|
| JSON | `.json`         | 标准 JSON 格式            |
| YAML | `.yaml`, `.yml` | YAML 格式               |
| TOML | `.toml`         | TOML 格式（Python 3.11+） |

## 使用

### 使用类（推荐）

```python
from pathlib import Path
from path_config import ConfigLoader

# 创建加载器
loader = ConfigLoader(env_var="MYAPP_CONFIG")

# 添加搜索路径（按优先级顺序）
loader.add_path(Path("config.yaml"))           # 当前目录
loader.add_xdg_path("myapp/config.yaml")       # XDG 配置目录
loader.add_cwd_path(".myapp.yaml")             # 当前目录

# 加载配置
config = loader.load(default={"debug": False})
```

### 便捷函数

```python
from path_config import load_config, xdg_config_path

# 简单用法
config = load_config([Path("config.yaml")])

# 使用环境变量
config = load_config(
    paths=[Path("config.yaml")],
    env_var="MYAPP_CONFIG",
    default={"debug": False},
)

# XDG 路径
xdg_path = xdg_config_path("myapp/config.yaml")
```

## XDG 配置路径

| 平台      | 路径                     |
|---------|------------------------|
| Linux   | `~/.config/{filename}` |
| macOS   | `~/.config/{filename}` |
| Windows | `%APPDATA%\{filename}` |

可通过环境变量覆盖：
- Linux/macOS: `XDG_CONFIG_HOME`
- Windows: `APPDATA`

## 搜索优先级

1. 环境变量指定的路径（`env_var`）
2. 通过 `add_path()` 添加的路径（按添加顺序）
3. 通过 `add_xdg_path()` 添加的路径
4. 通过 `add_cwd_path()` 添加的路径

## API

### ConfigLoader

```python
class ConfigLoader:
    def __init__(self, env_var: str | None = None, loaders: dict | None = None)
    def add_path(self, path: Path) -> ConfigLoader: ...
    def add_xdg_path(self, filename: str) -> ConfigLoader: ...
    def add_cwd_path(self, filename: str) -> ConfigLoader: ...
    def load(self, default: dict | None = None) -> dict | None: ...
```

### load_config(paths, env_var=None, default=None)

便捷函数

### xdg_config_path(filename: str) -> Path

获取 XDG 配置目录下文件路径
