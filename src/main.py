import datetime
from utils import add, subtract

def main():
    print("Name: Your Name Here")
    print(f"Today's date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    
    # Test calculator functions
    print(f"\nCalculator Test:")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")

if __name__ == "__main__":
    main()
