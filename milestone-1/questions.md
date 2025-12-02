# **SECTION A — BASICS (1–20)**

### **1. What is `venv`?**

`venv` is Python’s built-in tool for creating isolated virtual environments to manage project-specific dependencies.

### **2. What is a virtual environment?**

An isolated Python environment with its own packages, interpreter, and `site-packages` folder.

### **3. Why do we use virtual environments?**

To avoid dependency conflicts between multiple projects.

### **4. What command creates a virtual environment?**

```bash
python -m venv .venv
```

### **5. How do you activate a venv in Linux/macOS?**

```bash
source .venv/bin/activate
```

### **6. How do you activate a venv in Windows PowerShell?**

```bash
.venv\Scripts\Activate.ps1
```

### **7. How do you deactivate a venv?**

```bash
deactivate
```

### **8. Where are packages installed inside a venv?**

`<env>/lib/pythonX.Y/site-packages/`

### **9. How do you list installed packages?**

```bash
pip list
```

### **10. How do you save dependencies?**

```bash
pip freeze > requirements.txt
```

### **11. How do you install from requirements.txt?**

```bash
pip install -r requirements.txt
```

### **12. How do you generate a venv without activating?**

Just run:

```bash
python -m venv .venv
```

### **13. Does venv come with pip?**

Yes, pip is automatically included in venv.

### **14. How to check which python you're using?**

```bash
which python
```

(Or `where python` on Windows)

### **15. What does activation actually do?**

Modifies PATH so `python` and `pip` refer to the venv binaries.

### **16. Does deleting the venv folder deactivate it?**

Yes—just remove the folder.

### **17. Should venv be committed to Git?**

No. Add `.venv/` to `.gitignore`.

### **18. Why choose `.venv` as the name?**

Many tools (VS Code, PyCharm) auto-detect `.venv`.

### **19. Can projects share a single venv?**

Not recommended. Use one venv per project.

### **20. Does venv isolate Python version?**

No. venv uses whichever interpreter created it.

---

# **SECTION B — PYENV BASICS (21–40)**

### **21. What is pyenv?**

A tool to install and switch between multiple Python versions.

### **22. Does pyenv manage packages?**

No. It manages **Python versions**, not dependencies. Use venv for that.

### **23. Where does pyenv install Python versions?**

`~/.pyenv/versions/`

### **24. How do you install Python 3.12 with pyenv?**

```bash
pyenv install 3.12.2
```

### **25. List installed versions?**

```bash
pyenv versions
```

### **26. Set a global (system-wide default) Python?**

```bash
pyenv global 3.12.2
```

### **27. Set a Python version only for a project?**

```bash
pyenv local 3.10.13
```

### **28. How does pyenv choose a Python version?**

Order:
shell > local > global > system

### **29. What files does pyenv create?**

`.python-version` in project folders.

### **30. How does pyenv work internally?**

By placing **shims** in PATH that redirect to correct versions.

### **31. How to rehash shims?**

```bash
pyenv rehash
```

### **32. How to update pyenv?**

```bash
cd ~/.pyenv && git pull
```

(or Homebrew upgrade)

### **33. What does `pyenv which python` do?**

Shows the exact python binary pyenv resolves to.

### **34. Can pyenv install PyPy?**

Yes:

```bash
pyenv install pypy3.10-7.3.14
```

### **35. Can pyenv manage system Python?**

Yes, using version name `system`.

### **36. Is pyenv available for Windows?**

Not officially—use **pyenv-win** instead.

### **37. Difference between `pyenv global` and `local`?**

* `global`: system-wide default
* `local`: project-specific

### **38. How to see current active Python?**

```bash
pyenv version
```

### **39. Will pyenv affect Docker?**

No—Docker containers have isolated environments.

### **40. Does pyenv require shell initialization?**

Yes, via `.bashrc`, `.zshrc`, etc.

---

# **SECTION C — ADVANCED VENV (41–60)**

### **41. How to create venv with a specific Python?**

```bash
pyenv local 3.11.6
python -m venv .venv
```

### **42. How to run Python inside venv without activating?**

```bash
.venv/bin/python script.py
```

### **43. How to check pip path inside venv?**

```bash
pip --version
```

### **44. Why use `python -m pip` instead of `pip`?**

Guarantees pip tied to the active interpreter is used.

### **45. How to recreate a corrupted venv?**

Delete folder → recreate → reinstall dependencies.

### **46. What is `site-packages`?**

Directory containing installed Python libraries.

### **47. How to use editable installs?**

```bash
pip install -e .
```

### **48. Are C extensions isolated in venv?**

Yes, compiled wheels install per environment.

### **49. How to distribute a venv?**

You don't. Share `requirements.txt` instead.

### **50. Do system packages leak into venv?**

Only if using `--system-site-packages` (not recommended).

### **51. How does venv affect PATH?**

Puts `.venv/bin` at front.

### **52. Can venv override system libraries?**

Yes—venv’s pip installs take priority.

### **53. Are environment variables preserved across venvs?**

Yes, except PATH is modified.

### **54. Can you rename an existing venv?**

Not safely. Recreate it.

### **55. How to activate venv inside a script?**

Use the interpreter path, not activation.

### **56. Does venv work inside Docker?**

Usually not needed, but possible.

### **57. Is venv cross-platform?**

The folder content isn't; recreate per OS.

### **58. How do you lock dependencies fully?**

Use **pip-tools** or **poetry** (not venv).

### **59. Can you have multiple venvs in one project?**

Yes, but uncommon. Usually one per project.

### **60. How to detect if you're inside a venv?**

```python
import sys
print(hasattr(sys, 'real_prefix') or sys.prefix != sys.base_prefix)
```

---

# **SECTION D — ADVANCED PYENV (61–80)**

### **61. How does pyenv interact with venv?**

pyenv picks Python version → venv inherits it.

### **62. What is pyenv-virtualenv?**

A plugin adding virtualenv management to pyenv.

### **63. How to install using pyenv-virtualenv?**

```bash
pyenv virtualenv 3.10.9 myenv
```

### **64. How to activate virtualenv via pyenv?**

```bash
pyenv activate myenv
```

### **65. How to deactivate pyenv virtualenv?**

```bash
pyenv deactivate
```

### **66. Where does pyenv save virtualenvs?**

Inside `~/.pyenv/versions/<envname>`.

### **67. Does pyenv modify pip?**

No. Only the interpreter.

### **68. Does pyenv replace venv?**

No.
pyenv = Python version manager
venv = dependency isolation

### **69. How to uninstall a Python version?**

```bash
pyenv uninstall 3.12.2
```

### **70. How to force reinstall Python version?**

```bash
pyenv uninstall <version>
pyenv install <version>
```

### **71. Why does pyenv require build dependencies?**

Because it compiles Python from source.

### **72. How to fix pyenv “Python build failed” errors?**

Install missing dev libs (OpenSSL, readline, zlib, etc.)

### **73. Does pyenv slow down Python execution?**

No—shims only affect startup, not runtime.

### **74. Does pyenv support Anaconda?**

Yes:

```bash
pyenv install anaconda3-2022.05
```

### **75. How to disable pyenv temporarily?**

Comment out init lines from `.zshrc`/`.bashrc`.

### **76. What does `pyenv doctor` do?**

Diagnoses installation issues.

### **77. How to install Python faster?**

Use:

```bash
PYENV_GITHUB_MIRROR=<mirror_url>
```

or use prebuilt binaries (Linux).

### **78. Can pyenv handle multiple architectures?**

Yes — separate versions for ARM/x86.

### **79. How does pyenv handle miniconda?**

Treats it like any other version.

### **80. Does pyenv work in WSL?**

Yes, fully supported.

---

# **SECTION E — SCENARIOS & REAL-WORLD (81–100)**

### **81. Create a project with a specific Python + venv**

```bash
pyenv install 3.12.2
pyenv local 3.12.2
python -m venv .venv
```

### **82. Running tests across Python versions**

Use:

```bash
pyenv local 3.10.13 3.11.6 3.12.2
```

Supported by tools like tox.

### **83. Why is venv empty after activation?**

Because no packages installed yet.

### **84. “pip is not recognized” after activation — why?**

Activate using correct shell script:
PowerShell → `Activate.ps1`

### **85. “command not found: pyenv” — why?**

PATH + init not set in shell config.

### **86. Why `python3` vs `python` confusion?**

pyenv places shims using the same name; use version rules.

### **87. Best way to select Python inside VS Code**

Select interpreter pointing to `.venv/bin/python`.

### **88. Why venv still uses old Python version?**

Because pyenv wasn't set BEFORE creating venv.

### **89. How to rebuild venv after changing Python version?**

Delete `.venv` → recreate with new pyenv interpreter.

### **90. Should CI use venv or pyenv?**

venv for dependencies
pyenv or `actions/setup-python` for version

### **91. How to verify pyenv is active?**

```bash
pyenv version
```

### **92. Why is pyenv not picking your version?**

Another rule (shell/global/local) overrides it.

### **93. Why venv activation doesn’t work in fish shell?**

Use the fish activation script:

```bash
source .venv/bin/activate.fish
```

### **94. How to use multiple python versions in same project?**

Tox + pyenv installed versions.

### **95. Why not use global pip installs?**

Pollutes system environment; breaks OS tools.

### **96. How does pyenv affect cron or systemd?**

It usually doesn’t—those don’t load your shell RC files.

### **97. Can pyenv and conda coexist?**

Yes, but order in PATH matters.

### **98. How to detect the interpreter inside a script?**

```python
import sys
print(sys.executable)
```

### **99. Why is pyenv preferred over system Python?**

System Python is tied to the OS; modifying it can break system tools.

### **100. Ultimate workflow for most developers?**

1. Use **pyenv** to manage Python versions
2. Use **venv** for project isolation
3. Use **pip-tools / poetry** for dependency management
4. Use **VS Code + .venv** for development