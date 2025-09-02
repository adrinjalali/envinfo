"""
envinfo - A simple tool to display Python environment information and installed packages.

This package provides utilities to inspect the current Python environment,
including installed packages and their versions.
"""

__version__ = "0.1.0"
__author__ = "Environment Info"

from .core import list_packages, get_environment_info

def show_demo():
    """Show a demonstration of the environment info functionality."""
    print("=== Environment Information ===")
    env_info = get_environment_info()
    for key, value in env_info.items():
        print(f"{key}: {value}")
    
    print("\n=== Installed Packages ===")
    packages = list_packages()
    for pkg in packages[:10]:  # Show first 10 packages
        print(f"{pkg['name']}: {pkg['version']}")
    
    if len(packages) > 10:
        print(f"... and {len(packages) - 10} more packages")

__all__ = ["list_packages", "get_environment_info", "show_demo"]
