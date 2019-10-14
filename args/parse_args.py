import argparse

def parse_args():
    """
    Parse the CLI args
    """
    parser = argparse.ArgumentParser(description="Example of argument parsing")
    parser.add_argument("argument_1")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(args)
