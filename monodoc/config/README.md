# Config

Monodoc use [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
for config setup.

## Config Definations

Monodoc's config settings class is defined at `monodoc.config.settings`.

It's initializing and getting function are defined at `monodoc.config.__init__`.

## Config Sources

Monodoc accepts following config source (ordered by priority):

- CLI Arguments (`--debug`, etc.)
- Environment Variables (`MONODOC_DEBUG=true`)
- Config File (default path `~/.config/monodoc/config.toml`)
- Default Configs

We use `settings_customise_sources` of `pydantic_settings.BaseSettings`
to achieve this.

## CLI Arguments

ClI arguments is defined at `monodoc.cli.main:main()`,
this is the top-level callback function of monodoc.

We define CLI arguments as this function's params with default
value `None`. This is important, by defaulting `None`, arguments
not set by CLI will be ignored when initializing settings.
So that other low-priority config source can take effect.
