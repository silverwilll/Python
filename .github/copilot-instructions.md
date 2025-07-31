# Copilot Instructions for This Python Learning Codebase

## Overview
This repository is a collection of Python scripts and notebooks organized by topic for learning and experimentation. It is not a monolithic application, but a set of self-contained examples and exercises.

## Directory Structure & Patterns
- **01basics/** to **10panda/**: Each numbered folder covers a specific Python topic (e.g., basics, functions, containers, strings, exceptions, classes, modules, functional programming, numpy, pandas).
- Each topic folder contains multiple small scripts, each demonstrating a focused concept or feature.
- Scripts are named descriptively (e.g., `for_loops.py`, `dict.py`, `main.py` in subfolders) and are intended to be run independently.
- Some folders (e.g., `07modules/`) contain subfolders to demonstrate Python module/package structure and import patterns.
- The `script/` directory contains standalone scripts (e.g., `stock.py`).

## Conventions
- No central entry point; each script is self-contained.
- Use `main.py` in subfolders for demonstration or aggregation of concepts in that topic.
- Naming is descriptive and matches the concept being demonstrated.
- Minimal use of external dependencies except for `numpy` and `pandas` in relevant folders.
- No test framework or build system is present; scripts are run directly with Python.

## Developer Workflows
- To run a script: `python <path/to/script.py>`
- For numpy/pandas examples, ensure those packages are installed in your environment.
- No special build, test, or lint commands are required.

## Examples
- `09numpy/03function/main.py`: Demonstrates numpy array functions and methods.
- `07modules/import_modules/main.py`: Shows how to import from sibling and nested modules.
- `10panda/main.py`: Contains pandas usage examples.

## Integration & External Dependencies
- Only standard Python and common data science libraries (`numpy`, `pandas`) are used.
- No web, database, or external service integration.

## Guidance for AI Agents
- When adding new examples, follow the topic-based folder structure and descriptive naming.
- Keep scripts focused and independent; avoid cross-file dependencies unless demonstrating imports.
- Reference existing scripts for style and structure.
- Do not add unnecessary boilerplate or project scaffolding.

