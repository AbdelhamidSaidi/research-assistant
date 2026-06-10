import sys
from pathlib import Path

# Add src directory to path so we can import the actual main module
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run the main application
from main import main

if __name__ == "__main__":
    main()
