# **PYENV — COMPLETE NOTES (Beginner → Advanced)**

# 1. **What is pyenv?**

* A tool to **install**, **manage**, and **switch** between multiple Python versions.
* Allows per-project, per-shell, or global Python version selection.
* Works by **modifying PATH** and shimming Python executables.

# 2. **Why pyenv? (Key Benefits)**

* Easily install ANY Python version (3.7 → 3.12+).
* Isolate different projects with different Python interpreters.
* Avoid messing with system Python.
* Useful for:

  * Testing across versions
  * Using older frameworks requiring older Python
  * Managing multiple venvs tied to different Python versions

# 3. **How pyenv Works (Architecture)**

* Installs Python versions into `~/.pyenv/versions/`
* Adds a set of **shims** (tiny wrapper scripts) into PATH
* When you run `python`:

  1. pyenv checks **local** (.python-version file)
  2. Then **global**
  3. Then **shell override**
* Chooses the correct Python binary accordingly

# 4. **Installing pyenv**

## macOS

```bash
brew update
brew install pyenv
```

## Add to shell (IMPORTANT)

Add to `~/.zshrc`.

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"   # optional
```

Reload:

```bash
source ~/.zshrc
```

---

# 5. **Installing Python versions**

```bash
pyenv install --list           # show all versions
pyenv install 3.12.2
pyenv install 3.10.13
pyenv install 2.7.18           # legacy
```

Notes:

* pyenv compiles Python from source.
* Requires build dependencies (**VERY IMPORTANT**).
* On macOS: `brew install openssl readline zlib xz`
* On Ubuntu: install build essentials, dev headers.

# 6. **Versions Management**

### Check installed versions

```bash
pyenv versions
```

### Set global python version (system-wide default)

```bash
pyenv global 3.12.2
```

### Set python version for current directory/project

Creates a `.python-version` file:

```bash
pyenv local 3.10.13
```

### Set python version for current shell session

```bash
pyenv shell 3.11.6
```

# 7. **pyenv + venv**

Typical project flow:

```bash
pyenv local 3.11.6
python -m venv .venv
source .venv/bin/activate
```

Key point:

* The venv inherits whichever Python pyenv selected at that moment.

Verifying:

```bash
python --version
which python
```

# 8. **Uninstalling Versions**

```bash
pyenv uninstall 3.10.13
```

# 9. **Updating pyenv**

```bash
brew upgrade pyenv
```

# 10. **Best Practices**

* Always install Python versions via pyenv — never rely on system Python.
* Use **`.python-version` per project** so tools auto-detect Python version.
* Prefer `pyenv + venv` instead of `pyenv-virtualenv` for modern workflows.
* Combine pyenv with:

  * `poetry` (automatic use of pyenv versions)
  * `pip-tools`
  * Docker (match CI Python version)
* Never install Python packages into pyenv’s versions folder — always use venvs.

# 11. **Project Workflow Template**

```bash
# Step 1: project setup
mkdir myproject && cd myproject

# Step 2: choose Python version for project
pyenv install 3.12.2
pyenv local 3.12.2

# Step 3: create environment
python -m venv .venv
source .venv/bin/activate

# Step 4: develop
pip install <packages>
```