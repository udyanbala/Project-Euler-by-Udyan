#Lattice Pattern

def factorial(x):
    product = 1
    if x == 0 :
        return 1
    else:
        for n in range(1,x+1):
            product = product * n
    return product
    
print("This function is going to count the number of ways one can go from one corner to the opposite corner of a grid with 'a' rows and 'b' columns provided that only rightward/leftward and downward/upward movements are possible.")

rows = int(input("Number of Rows: "))
columns = int(input("Number of Columns: "))

ways = factorial(rows+columns)/(factorial(rows) * factorial(columns))
    
print(f'You have {int(ways)} ways to reach your destination.')

#alternative solution by GEMINI

from math import comb

if __name__ == "__main__":
    rows = int(input("Number of Rows: "))
    columns = int(input("Number of Columns: "))
    ways = comb(rows + columns, rows)
    print(f"You have {ways} ways to reach your destination.")
