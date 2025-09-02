"""
Core functionality for envinfo package.

Provides functions to list installed packages and get environment information.
"""

import sys
import platform
from typing import List, Dict, Any

try:
    from importlib import metadata
except ImportError:
    # Fallback for Python < 3.8
    import importlib_metadata as metadata


def list_packages() -> List[Dict[str, str]]:
    """
    List all installed Python packages and their versions.
    
    Returns:
        List of dictionaries containing package name and version information.
    """
    packages = []
    
    try:
        # Get all installed packages using importlib.metadata
        installed_packages = metadata.distributions()
        
        for package in installed_packages:
            # Get package location from files if available
            location = "Unknown"
            try:
                if package.files:
                    # Get the first file's parent directory as location
                    first_file = next(iter(package.files))
                    location = str(first_file.locate().parent.parent)
            except (AttributeError, StopIteration, OSError):
                # Fallback to package metadata if files not available
                try:
                    location = str(package.locate_file(""))
                except (AttributeError, OSError):
                    pass
            
            packages.append({
                'name': package.metadata['Name'],
                'version': package.version,
                'location': location
            })
        
        # Sort packages by name for consistent output
        packages.sort(key=lambda x: x['name'].lower())
        
    except Exception as e:
        print(f"Error retrieving package information: {e}")
        return []
    
    return packages


def get_environment_info() -> Dict[str, Any]:
    """
    Get Python environment information.
    
    Returns:
        Dictionary containing environment details.
    """
    return {
        'Python Version': sys.version.split()[0],
        'Python Executable': sys.executable,
        'Platform': platform.platform(),
        'Architecture': platform.architecture()[0],
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'Python Path': sys.path[0] if sys.path else 'Unknown',
        'Site Packages': [p for p in sys.path if 'site-packages' in p]
    }


def format_package_list(packages: List[Dict[str, str]], show_location: bool = False) -> str:
    """
    Format the package list for display.
    
    Args:
        packages: List of package dictionaries
        show_location: Whether to include package location in output
        
    Returns:
        Formatted string representation of packages
    """
    if not packages:
        return "No packages found."
    
    output_lines = []
    max_name_length = max(len(pkg['name']) for pkg in packages)
    
    for package in packages:
        name = package['name'].ljust(max_name_length)
        version = package['version']
        
        if show_location:
            location = package.get('location', 'Unknown')
            line = f"{name} {version:>15} ({location})"
        else:
            line = f"{name} {version:>15}"
        
        output_lines.append(line)
    
    return '\n'.join(output_lines)
