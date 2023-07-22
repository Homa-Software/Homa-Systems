# Contributing guidelines

## Enviroment setup

### asdf - version manager

Asdf is used to manage the versions of the tools used in this project. It manages the versions of the following tools:

- Python
- Node.js
- pnpm

Install [asdf](https://asdf-vm.com/guide/getting-started.html#_1-install-dependencies) and the following plugins:

```bash
asdf plugin add python
asdf plugin add nodejs
asdf plugin add pnpm
```

> **Warning**
>
> Asdf can conflict with tools like `nvm` and `pyenv`.
> This will cause problem when invoking binaries that would be provided by asdf shims like `node` and `python`.
> To prevent calling incorrect binaries ensure that the asdf shims are prepended to the beginning of your `PATH` variable. For example:
>
> ```bash
> export PATH="$HOME/.asdf/shims:$PATH"
> ```
>
> This can be added to your `~/.bashrc` or `~/.zshrc` file.
> Use the `which` command to verify that the correct binary is being called.

Asdf will automatically install the correct version of the tool when you enter the project directory.
This is done by reading the `.tool-versions` file in the project root.
To inspect the current versions of the tools run `asdf current` in the project root.
