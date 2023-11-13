import hashlib
import os
import sys
import random

hash_bits_size = 128

def generate_hash(input):
    return hashlib.md5(str(input).encode('ASCII')).hexdigest()

def check_and_create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    # create directory keys if not exist
    check_and_create_directory("keys")

    private_key_file = open("keys/lamport", "w")
    public_key_file = open("keys/lamport.pub", "w")

    for i in range(hash_bits_size):
        random_num1 = random.randint(0,sys.maxsize)
        random_num2 = random.randint(0,sys.maxsize)
        private_num1 = generate_hash(random_num1)
        private_num2 = generate_hash(random_num2)
        public_num1 = generate_hash(private_num1)
        public_num2 = generate_hash(private_num2)

        private_key_file.write(private_num1 + " " + private_num2 + "\n")
        public_key_file.write(public_num1 + " " + public_num2 + "\n")


    private_key_file.close()
    public_key_file.close()

    print("Success! Keys were created\n\nPrivate - at ./keys/lamport\nPublic - at ./keys/lamport.pub")

if __name__ == "__main__":
    main()