import argparse

parser = argparse.ArgumentParser(
    description="Tools to help with PyUnity development")

def main():
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
