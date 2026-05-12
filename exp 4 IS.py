# RSA Algorithm in Python

# Function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

# RSA key generation
p = 53
q = 59
n = p * q
phi = (p - 1) * (q - 1)

e = 3   # public key exponent
d = mod_inverse(e, phi)   # private key exponent

print("Public Key (n, e) =", (n, e))
print("Private Key (n, d) =", (n, d))

# Message to encrypt
msg = "HI"

# Convert letters to numbers: A=1, B=2, ..., Z=26
plain_nums = [ord(ch) - 64 for ch in msg]

# Encryption
cipher = []
for m in plain_nums:
    c = pow(m, e, n)
    cipher.append(c)

print("Encrypted Message:", cipher)

# Decryption
decrypted = ""
for c in cipher:
    m = pow(c, d, n)
    decrypted += chr(m + 64)

print("Decrypted Message:", decrypted)