## 1.0.3 (September 19, 2017)

### Improvement:
  - performance: ``init()``, ``create()``.
  - memory: ``init()``. 

### Added:
  - unittests.
  - 1 example.
  - initialization module:
    - ``_create_elements()``.
  - creation module:
    - ``_create_text()``.
  - handling import exceptions for "file" extension.

### Changed:
  - minor changes in the comments in the code.
  - in README.md updated "API Reference" and "Examples".
  - interaction module:
    - ``**data`` can be any iterable type.
    - ``**data`` defaults to ``tuple``.
  - initialization module:
    - ``data`` can be any iterable type.
    - ``_initialization`` returns generator.
  - examples folder:
    - most of functions from "./common/functions.py" was moved into "generation.py".

### Removed:
  - initialization module:
    - ``init_append()``.
  - creation module:
    - ``create_append()``.


## 1.0.2 (September 14, 2017)

### Added:
  - an information in the "README.md".
  - the "README.md" and the "CHANGELOG.md" translated into Russian. The translated version is in the "README.ru.md" and the "CHANGELOG.ru.md".

### Changed:
  - updated format of the "CHANGELOG.md".
  - updated "init.py" of the "files" extension. Changed ``__title__`` and added ``__description__``.
  - minor changes in the code.


## 1.0.1 (September 13, 2017)

Project rewritten on Python 3.

### Added:
  - extensions.
  - examples.

### Changed:
  - splitting the program logic. Now there are 5 modules: "_main.py", "interaction.py", "initialization.py", "creation.py", "generation.py".
  - "file.py" (work with a files) now is an extension.
  - for work with a SQLite database is now used extensions.file.SQLiteFile instance, not MarkovChain instance.

### Fixed:
  - when you try to create a SQLite file that already exists, an error is thrown.


## 1.0.0

Release of the project.

### Features:
  - text generation.
  - work with a files: ".json", ".pickle", ".sqlite".
