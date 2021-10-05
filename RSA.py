import math

#function to check if prime number or not
def prime(num):
    inc=0
    for i in range(1,int(num)+1):
        if num%i==0:
            inc+=1
    if inc==2:
        print(f"{num} is a prime number")        
    else:
        print(f"{num} is not a prime number")
        exit()

#Take two inputs
print("Enter two large prime numbers")

p=int(input("Enter p: "))
q=int(input("Enter q: "))

#To check if input numbers are prime numbers
prime(p)
prime(q)

#Calculating n
n=p*q
print(f"n value:{n}")

#Calculating phi(n)
phi=(p-1)*(q-1)
print(f"phi(n) value:{phi}")

#Take e from user
e=int(input("Give value of e: "))

#function to check if e is valid for RSA
def echeck(e,phi):
    if 1<e<phi and math.gcd(e,phi)==1:
        print("e is valid")
    else:
        print("e is invalid")
        exit()

#To check if e satisfies the condition of public key
echeck(e,phi)

print(f"The public key is (e,n): ({e},{n})")

#Calculating d
k=2 #A constant value
d=(k*phi+1)//e
print(f"The private key is d: {d}")

#Taking choice of user and printing output accordingly
print("Enter 1 for Encryption")
print("Enter 2 for Decryption")
choice=int(input("Choice: "))

if choice==1:
    num=""
    print("Encryption from plain text to cipher text")
    plain=input("Enter plain text in caps: ")    
    for i in plain:        
        num+=str(ord(i)-64)    
    num=int(num)    
    cipher=pow(num,e)%n
    print(f"The cipher text is: {cipher}")


elif choice==2:
    print("Decryption from cipher text to plain text")
    cipher=int(input("Enter cipher text in caps: "))   
    plain=pow(cipher,d)%n   
    plain=str(plain)
    print(f"The plain text is:")
    for i in plain:
        print(chr(int(i)+64),end="")

else:
    print("Wrong input")
    exit()







        