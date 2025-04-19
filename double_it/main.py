def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))  # Convert the input to an integer
    
    print(curr_value, end=' ')  # Print the initial value 
    
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=' ')  # Print the doubled value without a newline
    
    print()  # Print a newline at the end for better output formatting

if __name__ == '__main__':
    main()