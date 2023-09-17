import os
import time

def main():
   user = os.getenv("USERNAME") if os.getenv("USERNAME") is not None else "visitor"
   print(f"Hi {user} from a Github Actions worflow")

if __name__ == "__main__":
   main()
