#finding the number with the longest collatz chain under a given number: MY CODE


def collatz_chain_generator(number):
    chain_list = []
    if number == 1 or number == 0:
        chain_list.append(number)
        return chain_list
    n = 0   
    while n != 1:
        if number % 2 == 0 :
            chain_list.append(number)
            n = number//2
            number = n
            if n == 0 or n == 1:
                chain_list.append(n)
                return chain_list
                
        else:
            chain_list.append(number)
            n = (3 * number ) + 1
            number = n
            if n == 0 or n == 1:
                chain_list.append(n)
                return chain_list
        


def lengthiest_list_determiner(number1):
    length_of_chain = len(collatz_chain_generator(number1))
    return length_of_chain, number1
    
n = int(input("Please specify the upper bound to determine the integer beneath it that yields the longest Collatz sequence: "))
desired_number = 0
max_length = 0
for x in range(1, n):
    current_length, candidate_number = lengthiest_list_determiner(x)
    if current_length > max_length:
        max_length = current_length
        desired_number = candidate_number
    
print(desired_number)




# Alternative solution by GEMINI

from functools import cache


@cache
def chain_len(n: int) -> int:
    if n == 1:
        return 1
    return 1 + chain_len(n // 2 if n % 2 == 0 else 3 * n + 1)


def longest_collatz_under(limit: int) -> int:
    return max(range(1, limit), key=chain_len)


if __name__ == "__main__":
    upper_bound = int(input("Upper bound: "))
    print(longest_collatz_under(upper_bound))








        
