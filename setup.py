#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def create_venv():
    """Create a virtual environment if it doesn't exist using uv."""
    venv_path = Path(".venv") # uv typically creates .venv
    if not venv_path.exists():
        print("Creating virtual environment with uv...")
        subprocess.run(["uv", "venv"], check=True)
        print("Virtual environment created successfully!")
    else:
        print("Virtual environment already exists.")

def get_uv_executable():
    """Get the uv executable from the system's PATH."""
    return "uv"

def install_requirements():
    """Install requirements from requirements.txt using uv."""
    # No need to check for uv_path.exists() here as uv is expected to be in PATH
    print("Installing requirements with uv...")
    try:
        # Use 'uv pip install' as a direct replacement for 'pip install'
        subprocess.run(["uv", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

def main():
    """Main function to set up the project."""
    create_venv()
    install_requirements()
    print("\nSetup completed successfully!")
    print("\nTo activate the virtual environment:")
    if sys.platform == "win32":
        print("    .\\.venv\\Scripts\\activate")
    else:
        print("    source ./.venv/bin/activate")

if __name__ == "__main__":
    main() 