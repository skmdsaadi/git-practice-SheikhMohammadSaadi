import datetime
from utils import add, subtract, multiply, divide

def main():
    print("Name: Your Name Here")
    print(f"Today's date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    
    print("\nCalculator Functions Demo:")
    print(f"Addition: 10 + 5 = {add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
    print(f"Division: 10 / 5 = {divide(10, 5)}")
    print(f"Division by zero: 10 / 0 = {divide(10, 0)}")

if __name__ == "__main__":
    main()
