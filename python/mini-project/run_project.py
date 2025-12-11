import sys
from src.main import main, dev_entrypoints

if __name__ == "__main__":
    dev_option = len(sys.argv) > 1 and sys.argv[1] == "dev"

    if dev_option:
        dev_entrypoints()
    else:
        main()
