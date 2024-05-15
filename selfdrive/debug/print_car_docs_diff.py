import argparse

def print_car_docs_diff(base):
    pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--base", required=True)
  args = parser.parse_args()
  print_car_docs_diff(args.base)
