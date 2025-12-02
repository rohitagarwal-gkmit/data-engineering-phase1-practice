# 1 — What is a Python virtual environment?

* **Definition (short):** a *virtual environment* is an isolated Python runtime and package area. It gives each project its own `python` interpreter and `site-packages` directory so dependencies don't conflict across projects.
* **Why it matters:** different projects can require different versions of libraries (e.g., Django 2.x vs Django 5.x). venv prevents "dependency hell" by isolating them.
* **Core idea:** inside a venv you get:

  * A `python` binary (a copy or shim to the system interpreter)
  * A `bin/` (Unix) or `Scripts\` (Windows) with `activate` scripts
  * A private `site-packages` for installed packages

# 2 — Creating and using a venv (practical basics)

These are exact commands you’ll use daily.

**Create a venv**

```bash
python3 -m venv .venv
```

Notes:

* `.venv` is a common name; `env`, `venv`, or a project-specific name is fine. `.venv` keeps it hidden in many file browsers.
* `python` or `python3` or `py` — use whichever points to the Python interpreter you want.

**Activate**

```bash
source .venv/bin/activate
```

After activation your shell prompt typically changes to show `(.venv)`.

**Deactivate**

```bash
deactivate
```

**Install packages**

```bash
pip install -U pip
```

**List installed**

```bash
pip list
pip freeze        # good for requirements files
```

**Save/restore dependencies**

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

# 3 — What `venv` actually does (internals)

* `python -m venv DIR` creates a directory with:

  * `pyvenv.cfg` — records which base interpreter is used.
  * `bin/` (Unix) or `Scripts\` (Windows) — contains `python`, `pip`, and `activate` wrappers.
  * `lib/pythonX.Y/site-packages` — packages live here.
* Activation modifies your shell environment (PATH, maybe prompt). You can still call an env’s interpreter directly: `./.venv/bin/python script.py`.
* The virtual environment is not a full copy of Python standard library — it references the system copy for standard libs, but isolates installed packages.

# 4 — Common flags & options

```bash
python -m venv --help
```

Useful ones:

* `--clear` — remove environment contents (useful to recreate).
* `--upgrade` — upgrade existing env with new stdlib links iff needed.
* `--system-site-packages` — allow access to global site-packages (rare; breaks isolation).

# 5 — Best practices (project structure & git)

* Put your venv directory **outside** version control (or add `.venv/` to `.gitignore`).
* Use `requirements.txt` or `pyproject.toml` / `poetry.lock` for reproducibility.
* Common layout:

```
myproject/
  .venv/            # optional: local venv (gitignored)
  src/
  tests/
  pyproject.toml or setup.cfg or requirements.txt
  README.md
```

* Prefer `pip install --upgrade pip setuptools wheel` inside venv before adding packages.

# 6 — Reproducible dependencies

* `pip freeze > requirements.txt` gives exact versions (including transitive deps).
* For better repeatability across platforms, consider using a lockfile tool:

  * `pip-tools` (`pip-compile`, `pip-sync`)
  * `poetry` or `pipenv` (higher-level tools that produce lock files)
* Use constraints files when pinning only top-level libs is desired.

# 7 — Differences: venv vs virtualenv vs conda vs pipenv vs poetry

* **venv**: built-in, simple, uses system Python.
* **virtualenv**: older third-party tool; works where `venv` might not; provides some extras (faster on some platforms).
* **conda**: separate ecosystem; manages Python and binary packages; used in data science.
* **pipenv / poetry**: higher-level dependency managers with lock files and extra features (virtual env management built-in).
* Recommendation:

  * Use `venv` for straightforward projects and learning.
  * Use `poetry` or `pip-tools` for application dependency management (if you want lockfiles and nicer workflows).
  * Use `conda` when you need heavy compiled binaries and cross-language dependencies.

# 8 — Advanced topics & workflows

## a) Running scripts w/out activation

You can run the venv Python directly:

```bash
.venv/bin/python -m mymodule
.venv/bin/pip install somepkg
```

This is useful in CI scripts and Dockerfiles.

## b) Using venv in CI/CD

* Create and activate the venv in CI steps or call the interpreter directly.
  Example (bash in CI):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Better: skip activation and call `.venv/bin/python -m pytest`.

## c) Editable installs (dev workflow)

If you’re developing a package:

```bash
pip install -e .
```

This installs your package in "editable" mode so changes to your `src/` show up without reinstalling.

With `pyproject.toml` (PEP 517/518) ensure you use a build backend (`setuptools`, `flit`, `poetry` etc.)

## d) Wheels & binary dependencies

* Build wheels for faster installs and reproducibility:

```bash
pip wheel --wheel-dir=wheels -r requirements.txt
pip install --no-index --find-links=wheels -r requirements.txt
```

* For packages with C extensions, ensure wheel is available for your platform or you'll need a compiler toolchain.

## e) Python version management + venvs

* Use `pyenv` to manage interpreters.
* `pyenv-virtualenv` integrates pyenv and virtualenv.
* Typical flow:

```bash
pyenv install 3.12.0
pyenv local 3.12.0
python -m venv .venv   # uses 3.12.0
```

## f) Virtual environments and containers (Docker)

* Use Docker for true isolation of runtime + OS-level dependencies.
* In Dockerfiles, you usually don’t create venvs — Docker isolate the system.

# 9 — Security & hygiene

* Don’t `pip install` packages from unknown sources or untrusted URLs.
* Prefer pinned dependencies and lock files for deployment.
* Regularly update dependencies and monitor CVE feeds for your stack.
* Isolate build-time secrets from venv (use environment variables, secret managers).

# 10 — Common mistakes & how to avoid them

1. **Forgetting to activate** — installs go to system Python (use `pip --version` to confirm path; or run `which python` / `where python`).
2. **Using `sudo pip install`** — bad: installs globally and can break system packages.
3. **Committing venv to git** — bloats repo; instead use `requirements.txt`.
4. **Assuming `pip freeze` is enough for cross-platform reproducibility** — some packages are platform-specific.
5. **Using `--system-site-packages` by accident** — removes isolation.

# 11 — Step-by-step learning path (progressive exercises)

Work through these to gain mastery.

## Beginner exercises (do all)

1. **Create and activate**

   * Create `.venv` for a new folder, activate, install `requests`, import it in an interpreter.
   * Verify pip points to the venv: `which pip` or `pip --version`.
2. **requirements.txt**

   * `pip freeze > requirements.txt`, create a fresh directory, make a new venv, `pip install -r requirements.txt`.
3. **Deactivate**

   * Activate, install a package, `deactivate`, then run system `python -c "import requests"` and observe failure (if system doesn't have it).

## Intermediate exercises

1. **Editable package**

   * Make a simple package:

     ```
     mypkg/
       src/mypkg/__init__.py
       pyproject.toml or setup.cfg
     ```
   * `pip install -e .` and modify code to observe behavior without reinstalling.
2. **Build a wheel**

   * `pip wheel .` or `python -m build` (if using `build` package).
3. **Use constraints**

   * Create `requirements.in` with top-level libs, run `pip-compile` (pip-tools) to generate precise pins.

## Advanced exercises

1. **CI script**

   * Write a CI job snippet (GitHub Actions) that sets up Python, creates a venv, installs deps, runs tests.
2. **Multiple Python versions**

   * Use `pyenv` or `actions/setup-python` to test the same test suite under 3.9, 3.10, 3.11 in CI.
3. **Binary deps**

   * Install a package with native dependency (e.g., `lxml`) and configure build tools to compile it, or use wheels.
4. **Dependency audits**

   * Use `pip-audit` or `safety` to scan installed packages for vulnerabilities.

# 12 — Cheatsheet (quick commands)

```bash
# create
python -m venv .venv

# activate (bash)
source .venv/bin/activate

# activate (PowerShell)
.venv\Scripts\Activate.ps1

# install packages
pip install -U pip setuptools wheel
pip install flask

# freeze and restore
pip freeze > requirements.txt
pip install -r requirements.txt

# run without activation
.venv/bin/python script.py

# reinstall from scratch
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
