import random
hints = {
    1: "It is a unique number because it is neither a prime nor a composite number.",
    2: "It is the first prime number and the only even prime number.",
    3: "It is the smallest odd prime number.",
    4: "It is the first composite number and the square of 2.",
    5: "It is the second odd prime number.",
    6: "It is the smallest perfect number, having divisors 1, 2, and 3 which sum up to 6.",
    7: "It is the third odd prime number.",
    8: "It is the first cube number (2^3).",
    9: "It is the square of 3 and the first perfect square.",
    10: "It is the smallest even composite number.",
    11: "It is the fourth odd prime number.",
    12: "It is the smallest abundant number, having divisors 1, 2, 3, 4, and 6 which sum up to 16.",
    13: "It is the fifth odd prime number.",
    14: "It is the smallest even composite number greater than 10.",
    15: "It is the smallest number with 4 divisors (1, 3, 5, and 15).",
    16: "It is the smallest square number (4^2).",
    17: "It is the sixth odd prime number.",
    18: "It is the smallest number with 6 divisors (1, 2, 3, 6, 9, and 18).",
    19: "It is the seventh odd prime number.",
    20: "It is the smallest number with 6 divisors and the smallest composite number divisible by all digits from 1 to 5.",
    21: "It is the smallest number with 4 divisors that are co-prime (1, 3, 7, and 21).",
    22: "It is the smallest number with 4 divisors that are not co-prime.",
    23: "It is the eighth odd prime number.",
    24: "It is the smallest number with 8 divisors (1, 2, 3, 4, 6, 8, 12, and 24).",
    25: "It is the square of 5 and the second perfect square.",
    26: "It is the smallest composite number greater than 25.",
    27: "It is the smallest cube number (3^3).",
    28: "It is the second perfect number, having divisors 1, 2, 4, 7, and 14 which sum up to 28.",
    29: "It is the ninth odd prime number.",
    30: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 6.",
    31: "It is the tenth odd prime number.",
    32: "It is the fifth power of 2 (2^5).",
    33: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    34: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    35: "It is the smallest number with 4 divisors that are co-prime and not divisible by any of its digits.",
    36: "It is the smallest number with 9 divisors (1, 2, 3, 4, 6, 9, 12, 18, and 36).",
    37: "It is the eleventh odd prime number.",
    38: "It is the smallest number with 4 divisors that are co-prime and divisible by its digits.",
    39: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    40: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 7.",
    41: "It is the twelfth odd prime number.",
    42: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 6.",
    43: "It is the thirteenth odd prime number.",
    44: "It is the smallest number with 6 divisors and the smallest even number with 6 divisors.",
    45: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    46: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    47: "It is the fourteenth odd prime number.",
    48: "It is the smallest number with 10 divisors (1, 2, 3, 4, 6, 8, 12, 16, 24, and 48).",
    49: "It is the square of 7 and the third perfect square.",
    50: "It is the smallest number with 6 divisors and the smallest number divisible by all digits from 1 to 5.",
    51: "It is the smallest number with 4 divisors that are co-prime and not divisible by any of its digits.",
    52: "It is the smallest number with 6 divisors and the smallest even number with 6 divisors.",
    53: "It is the fifteenth odd prime number.",
    54: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 6.",
    55: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    56: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 7.",
    57: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    58: "It is the smallest number with 4 divisors that are co-prime and divisible by its digits.",
    59: "It is the sixteenth odd prime number.",
    60: "It is the smallest number with 12 divisors (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60).",
    61: "It is the seventeenth odd prime number.",
    62: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    63: "It is the smallest number with 6 divisors and the smallest number divisible by all digits from 1 to 6.",
    64: "It is the fourth power of 2 (2^6).",
    65: "It is the smallest number with 4 divisors that are co-prime and not divisible by any of its digits.",
    66: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 7.",
    67: "It is the eighteenth odd prime number.",
    68: "It is the smallest number with 6 divisors and the smallest even number with 6 divisors.",
    69: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    70: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 8.",
    71: "It is the nineteenth odd prime number.",
    72: "It is the smallest number with 12 divisors and the smallest number divisible by all digits from 1 to 7.",
    73: "It is the twentieth odd prime number.",
    74: "It is the smallest number with 4 divisors that are co-prime and divisible by its digits.",
    75: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    76: "It is the smallest number with 6 divisors and the smallest even number with 6 divisors.",
    77: "It is the smallest number with 4 divisors that are co-prime and not divisible by any of its digits.",
    78: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 7.",
    79: "It is the twenty-first odd prime number.",
    80: "It is the smallest number with 10 divisors and the smallest number divisible by all digits from 1 to 8.",
    81: "It is the fourth power of 3 (3^4).",
    82: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    83: "It is the twenty-second odd prime number.",
    84: "It is the smallest number with 12 divisors and the smallest number divisible by all digits from 1 to 8.",
    85: "It is the smallest number with 4 divisors that are co-prime and not divisible by any of its digits.",
    86: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    87: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    88: "It is the smallest number with 8 divisors and the smallest number divisible by all digits from 1 to 8.",
    89: "It is the twenty-third odd prime number.",
    90: "It is the smallest number with 12 divisors and the smallest number divisible by all digits from 1 to 9.",
    91: "It is the smallest number with 4 divisors that are co-prime and not divisible by any of its digits.",
    92: "It is the smallest number with 4 divisors that are not co-prime and divisible by its digits.",
    93: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    94: "It is the smallest number with 4 divisors that are co-prime and divisible by its digits.",
    95: "It is the smallest number with 4 divisors that are not co-prime and not divisible by any of its digits.",
    96: "It is the smallest number with 12 divisors and the smallest number divisible by all digits from 1 to 9.",
    97: "It is the twenty-fourth odd prime number.",
    98: "It is the smallest number with 6 divisors and the smallest number divisible by all digits from 1 to 8.",
    99: "It is the smallest number with 6 divisors and the smallest odd number with 6 divisors.",
    100: "It is the smallest number with 9 divisors and the smallest square number divisible by all digits from 1 to 9."
}


score=10
def guess(n):#n is the range between number is generated
    global score
    x=random.randint(1,n)#x=number genereated by the computer 
    print(f"HINT: {hints[x]}")
    while True:
     try:
         
         y=int(input("GUESS: "))#y=guess
         

         if y<0:
             print("pls give a positive integer".capitalize())
             continue

         if x==y:
             print("JUST RIGHT!")
             return False# return false is to break the loop
     
         elif x>y:
             print("TOO SMALL!")
             score -= 5
    
         elif x<y:
             print("TOO LARGE!")
             score -= 5
         if score <0:
             print(f"GAME OVER\nNUMBER WAS {x}")
             return False# return false is to break the loop
     except ValueError:
         print("PLS GIVE A VALID INTEGER")



if __name__=="__main__":
 while True:
     Level=int(input("LEVEL: "))
     if Level >100:
         print("LEVEL GREATER THAN 100 NOT ALLOWED")
     else:
         guess(Level)