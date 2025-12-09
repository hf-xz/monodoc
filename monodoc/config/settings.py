"""
Configuration settings for monodoc application.
"""

from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

APP_NAME = "monodoc"

DEFAULT_CONFIG_FILE = Path.home() / ".config" / APP_NAME / "config.toml"
DEFAULT_DATA_DIR = Path.home() / f".{APP_NAME}"


class DeferredTomlConfigSettingsSource(TomlConfigSettingsSource):
    """TOML config settings source that can reload config files later."""

    def __call__(self):
        """Reload config files based on current state."""
        super().__init__(
            settings_cls=self.settings_cls,
            toml_file=self.current_state.get("config_file", self.toml_file_path),
        )
        return super().__call__()


class Settings(BaseSettings):
    """
    Application configuration settings.
    Defaults can be overridden by CLI arguments, env vars, or config file.
    Priority order (highest to lowest):
    1. CLI arguments
    2. Environment variables
    3. Configuration file (TOML)
    4. Default values (this class)
    """

    # Constants
    app_name: str = APP_NAME

    # Settings with default values
    config_file: Path = DEFAULT_CONFIG_FILE
    data_dir: Path = DEFAULT_DATA_DIR
    debug: bool = False

    # Pydantic Settings Config
    model_config = SettingsConfigDict(
        extra="ignore",
        env_prefix="MONODOC_",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    # Customise settings sources to include deferred TOML config
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,  # initial settings source, CLI args come from here
        env_settings: PydanticBaseSettingsSource,  # environment variables source
        dotenv_settings: PydanticBaseSettingsSource,  # .env file source, will be ignored
        file_secret_settings: PydanticBaseSettingsSource,  # file secrets source
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            DeferredTomlConfigSettingsSource(settings_cls, DEFAULT_CONFIG_FILE),
            file_secret_settings,
        )
