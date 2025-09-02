# envinfo

A simple and lightweight tool to display Python environment information and list installed packages with their versions.

## Overview

`envinfo` is a handy utility for Python developers and system administrators who need quick access to environment details and package information. Perfect for debugging, environment auditing, and development setup verification.

## Features

- **Environment Information**: Display Python version, platform, architecture, and paths
- **Package Listing**: List all installed packages with versions and locations
- **Clean CLI Interface**: Easy-to-use command-line tool with multiple options
- **Lightweight**: No external dependencies, uses only Python standard library
- **Cross-platform**: Works on Windows, macOS, and Linux

## Python API

You can also use `envinfo` programmatically in your Python code:

```python
import envinfo

# Get environment information
env_info = envinfo.get_environment_info()
print(f"Python Version: {env_info['Python Version']}")
print(f"Platform: {env_info['Platform']}")

# List all installed packages
packages = envinfo.list_packages()
for pkg in packages:
    print(f"{pkg['name']}: {pkg['version']}")

# Show a quick demo (combines both)
envinfo.show_demo()
```

### Available Functions

- `get_environment_info()` - Returns a dictionary with Python environment details
- `list_packages()` - Returns a list of dictionaries with package information
- `show_demo()` - Prints a formatted display of environment and package info

## CLI Options

The `envinfo` command supports several options:

- `envinfo` - Show both environment info and installed packages (default)
- `envinfo -e` or `--environment` - Show only environment information
- `envinfo -p` or `--packages` - Show only installed packages
- `envinfo -l` or `--location` - Include package installation locations
- `envinfo -c` or `--count` - Show only the count of installed packages
- `envinfo -v` or `--version` - Show version information

### Installation

```bash
# Using pixi (recommended)
pixi install
pixi run install

# Or using pip directly
pip install -e .
```

### Development with Pixi

This project uses [pixi](https://pixi.sh/) for dependency management and task automation:

```bash
# Install dependencies and the package in development mode
pixi run install

# Run the CLI tool
pixi run demo

# Test specific functionality
pixi run test-cli
pixi run test-packages
pixi run test-env

# Build the package
pixi run build

# Clean build artifacts
pixi run clean
```

### Usage Examples

```bash
# Show all information (default)
envinfo

# Show only environment information
envinfo --environment

# Show only installed packages
envinfo --packages

# Show packages with their installation locations
envinfo --packages --location

# Get just the count of installed packages
envinfo --count
```

### Sample Output

```
=== Python Environment Information ===
Python Version: 3.11.5
Python Executable: /usr/bin/python3
Platform: Linux-5.15.0-78-generic-x86_64-with-glibc2.35
Architecture: 64bit
Machine: x86_64
Python Path: /home/user/project

=== Installed Packages ===
certifi                    2023.7.22
charset-normalizer         3.2.0
idna                       3.4
pip                        23.2.1
requests                   2.31.0
setuptools                 68.0.0
urllib3                    2.0.4

Total: 7 packages
```

## Use Cases

- **Development Environment Setup**: Verify your development environment has the right packages
- **Debugging**: Quickly check what's installed when troubleshooting issues
- **Documentation**: Generate environment snapshots for bug reports
- **System Administration**: Audit Python installations across systems
- **CI/CD Pipelines**: Validate environment consistency in automated builds

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
