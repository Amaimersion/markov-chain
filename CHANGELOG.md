## 1.0.2 (September 14, 2017)
### Changed:
  - updated format of the CHANGELOG.md.
  - updated ``__init__.py`` of the files extension. Changed ``__title__`` and added ``__description__``.
  - minor changes in the code.

### Added:
  - added an information in the README.md.
  - the README.md and the CHANGELOG.md translated into Russian. The translated version is in the README.ru.md and the CHANGELOG.ru.md.


## 1.0.1 (September 13, 2017)
Project rewritten on Python 3.

### Changed:
  - splitting the program logic. Now there are 5 files: _main.py, interaction.py, initialization.py, creation.py, generation.py.
  - file.py (work with a files) now is an extension.
  - for work with a SQLite database is now used extensions.file.SQLiteFile instance, not MarkovChain instance.

### Added:
  - extensions folder.
  - examples folder.
  - added generation example and files usage example.

### Fixed:
  - when you try to create a SQLite file that already exists, an error is thrown.


## 1.0.0
Release of the project.

### Features:
  - text generation.
  - work with a files: .json, .pickle, .sqlite.
