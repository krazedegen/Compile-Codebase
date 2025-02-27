# Codebase Compiler

A simple Python script to compile an entire codebase into a single text file for quick sharing. This tool recursively scans a directory, gathers all text-based files (e.g., `.py`, `.js`, `.md`), and concatenates them into a single output file with clear file separators.

## Features
- **Automatic Output**: Saves the compiled codebase to a default file (e.g., `<directory_name>_compiled.txt`) if no output file is specified.
- **Custom Output**: Allows you to specify a custom output file path.
- **Text-Only**: Intelligently includes only text files (based on MIME types or no extension) and skips binary files.
- **Excludes Clutter**: Ignores common non-source directories like `.git`, `node_modules`, and `build`.
- **Cross-Platform**: Works on Windows, macOS, and Linux without modification.
- **No Intervention**: Runs without needing adjustments between different codebases.

Basic Usage (Default Output)
Compile a codebase into a default file named after the directory:
bash
```
python compile_codebase.py /path/to/your/codebase
```
Output: Saves to <codebase_name>_compiled.txt in the current directory.

Example: For a directory myproject, it creates myproject_compiled.txt.

Custom Output File
Specify a custom output file:
bash
```
python compile_codebase.py /path/to/your/codebase output.txt
```
Output: Saves to output.txt in the current directory.

