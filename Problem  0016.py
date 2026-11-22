def summation_of_digits(num):
    summation = 0
    for x in str(num):
        summation = summation + int(x)
    return summation


print(
    "This program finds the summation of digits of a natural number or an exponential expression.\n"
)
print("What is your number? If integer, input 0? Else, input 1.\n")
determiner = int(input("Enter the number-code: "))

desired_summation = 0

if determiner == 0:
    number = input("Enter the intended number: ")
    has_dot = False
    for x in number:
        if x == ".":
            has_dot = True
            print(
                "Floating-point numbers will be truncated and then the remaining digits will be added."
            )
            break

    if has_dot:
        number = int(float(number))
    else:
        number = int(number)

    if number < 0:
        digits = str(abs(number))
        desired_summation = -int(digits[0]) + summation_of_digits(digits[1:])
    else:
        desired_summation = summation_of_digits(number // 1)

    print("Your summation is: ", desired_summation)

elif determiner == 1:
    base = int(input("What is the base of your number? "))
    exponent = int(input("What is the exponent of your number? "))
    print("Your summation is: ", summation_of_digits(base**exponent))




#Alternative by GEMINI
def digit_sum(n: int) -> int:
    s = str(abs(n))
    return sum(int(ch) for ch in s)


if __name__ == "__main__":
    code = int(input("Enter 0 for a number or 1 for base^exponent: "))
    if code == 0:
        val = int(float(input("Enter number: ")))
        print("Digit sum:", digit_sum(val))
    elif code == 1:
        base = int(input("Base: "))
        exp = int(input("Exponent: "))
        print("Digit sum:", digit_sum(base**exp))
    else:
        print("Invalid code.")
