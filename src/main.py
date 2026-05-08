import datetime
from utils import add, subtract, multiply, divide, power, modulo

def main():
    print("=" * 50)
    print("GIT PRACTICE PROJECT - CALCULATOR DEMO")
    print("=" * 50)
    
    print(f"\n👤 Name: Your Name Here")
    print(f"📅 Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    
    print("\n📊 CALCULATOR FUNCTIONS:")
    print("-" * 30)
    
    # Test basic operations
    test_cases = [
        ("Addition", add, 10, 5),
        ("Subtraction", subtract, 10, 5),
        ("Multiplication", multiply, 10, 5),
        ("Division", divide, 10, 5),
        ("Division by zero", divide, 10, 0),
        ("Power", power, 2, 3),
        ("Modulo", modulo, 10, 3),
        ("Modulo by zero", modulo, 10, 0),
    ]
    
    for operation_name, func, a, b in test_cases:
        try:
            result = func(a, b)
            print(f"{operation_name:15}: {a} {func.__name__} {b} = {result}")
        except Exception as e:
            print(f"{operation_name:15}: Error - {e}")
    
    print("\n✅ Error handling successfully implemented!")
    print("=" * 50)

if __name__ == "__main__":
    main()
