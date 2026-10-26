def int_to_roman(num):
    """
    Converts an integer to a Roman numeral string.
    Handles numbers from 1 to 3999.
    """
    if not 1 <= num <= 3999:
        return "Enter a valid integer from 1 to 3999."

    # Map the values to their Roman symbols, in descending order
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []
    for value, symbol in roman_map:
        # Append the symbol as many times as the value fits into the number
        while num >= value:
            result.append(symbol)
            num -= value
    
    return "".join(result)

# Example Usage:
number = int(input("Enter a decimal number (1-3999): "))
roman_equivalent = int_to_roman(number)
print(f"The Roman equivalent of {number} is {roman_equivalent}")