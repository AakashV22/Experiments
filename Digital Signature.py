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

M=int(input("Enter Message (M): "))

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

# Multiplicative inverse
def exteuclid(a, b):
	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:
		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a
		
	return (r1, t1)

#Calculating d
r, d = exteuclid(phi, e)
if r == 1:
	d = int(d)
	print(f"The private key is d: {d}")
	
else:
	print("Multiplicative inverse for\
	the given encryption key does not \
	exist. Choose a different encryption key ")

S=(M**d)%n
M1=(S**e)%n

if M==M1:
    print("Message Accepted")
else:
    print("Message Rejected")






        