import fibonacci

def main():
    print("starting main...")
    number = int(input("Enter the length of fibonacci series:"))

    series = fibonacci.get_fibonacci_series(number)

    print(series)

main()    
"""hello world"""