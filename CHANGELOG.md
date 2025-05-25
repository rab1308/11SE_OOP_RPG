# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2025-05-23]

### Added
- Forked from [Mr-Zamora/11SE_OOP_RPG](https://github.com/Mr-Zamora/11SE_OOP_RPG.git)
- Refactored single-file implementation into multi-file structure
- Added `constants.py` for centralized configuration management
- Implemented type hints throughout the codebase
- Added comprehensive docstrings to all classes and methods

### Changed
- Improved code style to follow PEP 8 guidelines
- Refactored string formatting for better readability
- Updated ROADMAP.md to reflect new project structure

### Fixed
- Fixed long lines to comply with PEP 8 (88 character limit)
- Eliminated magic numbers and hardcoded strings

## [2025-05-26]

### Changed
- Simplified project structure by removing package architecture
- Removed `__init__.py` files to make the project a standard Python project
- Modified import statements to work without package structure
- Renamed `project_rules.md` to `RULES.md` for better consistency

### Removed
- Deleted `setup.py` and package installation files
- Removed `run_game.py` in favor of using `rpg_game/main.py` directly

## [Unreleased]

### Planned
- Add unit tests with 80%+ coverage
- Implement error handling with specific exceptions
- Add inventory system for characters
- Expand character types (Sidekick, Villain classes)
- Enhance combat system
