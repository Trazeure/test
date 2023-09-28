import math
import random
import string

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def siguiente_primo(n):
    candidate = n + 1
    while not primo(candidate):
        candidate += 1
    return candidate

def mediana(a, b, c):
    return sorted([a, b, c])[1]

def password():
    length = random.randint(7, 10)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)


if __name__=="__main__":
    x= float(input("Ingrese el primer numero: "))
    y=float(input("Ingrese el segundo numero: "))
    z=float(input("Ingrese el tercer numero: "))
    print(f"la mediana de {x},{y},{z} es {mediana(x,y,z)}")