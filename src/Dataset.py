from Crypto.Cipher import AES, DES3, Blowfish, ARC2, CAST, Salsa20
from Crypto.Random import get_random_bytes
import os

encryption_algorithm = {"AES":AES , "3DES":DES3 , "Blowfish":Blowfish , "RC4": ARC2 , "CAST":CAST}

#fixed file size = 8kb
file_size = 8*1024

#no of sample for each algorithm 
num_samples = 100

output_dir = "encrypted data"
os.makedirs(output_dir , exist_ok=True)

def generate_plaintext(file_size):
    hex_string = get_random_bytes(file_size).hex()
    return bytes.fromhex(hex_string)

def encrypt_data(algorithm, plaintext):
    key_size = algorithm.key_size if isinstance(algorithm.key_size, int) else min(algorithm.key_size)
    key = get_random_bytes(key_size)
    cipher = algorithm.new(key, algorithm.MODE_ECB)
    padded_plaintext = plaintext + b"\0" * (cipher.block_size - len(plaintext) % cipher.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

## generating samples
for alg_name,alg in encryption_algorithm.items():
    for i in range(num_samples):
        plaintext = generate_plaintext(file_size)
        ciphertext = encrypt_data(alg , plaintext)
        
        filename = f"{alg_name}_8KB_{i}.bin"
        with open(os.path.join(output_dir,filename),"wb") as f:
            f.write(ciphertext)
            
        print(f"Generated {filename}")

print("Data generation complete.")