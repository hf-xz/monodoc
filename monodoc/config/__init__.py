"""
Initialization and access for application settings.
"""

from .settings import Settings

__all__ = ["Settings", "get_settings", "init_settings"]

_settings_instance: Settings | None = None


def get_settings(**kwargs) -> Settings:
    global _settings_instance

    # if no instance exists, create one
    if _settings_instance is None:
        # exclude None values from kwargs
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        # create a new Settings instance
        _settings_instance = Settings(**filtered_kwargs)
        return _settings_instance

    # if instance exists, ensure no kwargs are passed
    if kwargs:
        raise ValueError("Settings have already been initialized; cannot pass kwargs again.")

    return _settings_instance


def init_settings(**kwargs) -> Settings:
    return get_settings(**kwargs)
