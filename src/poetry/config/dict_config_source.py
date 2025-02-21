from typing import Any
from typing import Dict

from .config_source import ConfigSource


class DictConfigSource(ConfigSource):
    def __init__(self) -> None:
        self._config: Dict[str, Any] = {}

    @property
    def config(self) -> Dict[str, Any]:
        return self._config

    def add_property(self, key: str, value: Any) -> None:
        keys = key.split(".")
        config = self._config

        for i, key in enumerate(keys):
            if key not in config and i < len(keys) - 1:
                config[key] = {}

            if i == len(keys) - 1:
                config[key] = value
                break

            config = config[key]

    def remove_property(self, key: str) -> None:
        keys = key.split(".")

        config = self._config
        for i, key in enumerate(keys):
            if key not in config:
                return

            if i == len(keys) - 1:
                del config[key]

                break

            config = config[key]
