"""
Command-line interface for envinfo package.

Provides a CLI tool to display environment information and installed packages.
"""

import argparse
import sys
from .core import list_packages, get_environment_info, format_package_list


def main():
    """Main entry point for the envinfo CLI tool."""
    parser = argparse.ArgumentParser(
        description="Display Python environment information and installed packages",
        prog="envinfo"
    )
    
    parser.add_argument(
        "--packages", "-p",
        action="store_true",
        help="List all installed packages and their versions"
    )
    
    parser.add_argument(
        "--environment", "-e",
        action="store_true",
        help="Show Python environment information"
    )
    
    parser.add_argument(
        "--location", "-l",
        action="store_true",
        help="Include package installation locations (use with --packages)"
    )
    
    parser.add_argument(
        "--count", "-c",
        action="store_true",
        help="Show only the count of installed packages"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="envinfo 0.1.0"
    )
    
    args = parser.parse_args()
    
    # If no specific options are provided, show both environment and packages
    if not any([args.packages, args.environment, args.count]):
        args.environment = True
        args.packages = True
    
    try:
        if args.environment:
            print("=== Python Environment Information ===")
            env_info = get_environment_info()
            for key, value in env_info.items():
                if isinstance(value, list):
                    print(f"{key}:")
                    for item in value:
                        print(f"  - {item}")
                else:
                    print(f"{key}: {value}")
            print()
        
        if args.packages or args.count:
            packages = list_packages()
            
            if args.count:
                print(f"Total installed packages: {len(packages)}")
            else:
                print("=== Installed Packages ===")
                if packages:
                    formatted_output = format_package_list(packages, show_location=args.location)
                    print(formatted_output)
                    print(f"\nTotal: {len(packages)} packages")
                else:
                    print("No packages found.")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
