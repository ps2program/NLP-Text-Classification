#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def create_venv():
    """Create a virtual environment if it doesn't exist using venv."""
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("Creating virtual environment with venv...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("Virtual environment created successfully!")
    else:
        print("Virtual environment already exists.")

def install_requirements():
    """Install requirements from requirements.txt using pip from the venv."""
    print("Installing requirements with pip...")
    if sys.platform == "win32":
        pip_executable = Path(".venv") / "Scripts" / "pip"
    else:
        pip_executable = Path(".venv") / "bin" / "pip"
    try:
        subprocess.run([str(pip_executable), "install", "-r", "requirements.txt"], check=True)
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