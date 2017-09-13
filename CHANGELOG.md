# Changelog
All changes to this project will be documented in this file.


## 1.0.1 (September 13, 2017)
Project rewritten on Python 3.

### Changed:
  - splitting the program logic. Now there are 5 files: _main, interaction, initialization, creation, generation.
  - file (work with a files) now is extension.
  - for work with the sqlite database is now used extensions.file.SQLiteFile instance, not MarkovChain instance.

### Added:
  - extensions.
  - examples.

### Fixed:
  - when you try to create a sqlite file that already exists, an error is thrown.


## 1.0.0
Release.

### Features:
  - text generation.
  - work with a files: .json, .pickle, .sqlite.
