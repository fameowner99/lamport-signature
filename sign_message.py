import hashlib
import os

def generate_hash(input):
    return hashlib.md5(str(input).encode('utf-8')).hexdigest()

def get_hash_byte_array(hash):
	num_of_characters = 2
	splitted_array = [hash[i:i + num_of_characters] for i in range(0, len(hash), num_of_characters)]
	return [int(numeric_string, 16) for numeric_string in splitted_array]

def check_and_create_directory(directory):
	if not os.path.exists(directory):
	    os.makedirs(directory)

def read_private_key():
	 with open("keys/lamport") as f:
	 	lines = f.readlines()
	 	return [line.split() for line in lines]

def main():
	check_and_create_directory("signature")

	message = input("Enter message to sign with ./keys/lamport key: \n")

	message_hash = generate_hash(message)
	bytes_array = get_hash_byte_array(message_hash)

	private_key_values = read_private_key()

	with open("signature/lamport.sign", "w") as f:
		bits_in_byte = 8
		for idx, num in enumerate(bytes_array):
			for i in range(0, bits_in_byte):
				private_key_index = idx * bits_in_byte + i;
				if (num & 1 << i):
					f.write(private_key_values[private_key_index][1] + "\n")
				else:
					f.write(private_key_values[private_key_index][0] + "\n")

	print("Success! Signature created at ./signatur/lamport.sign for message:\n" + message)

if __name__ == "__main__":
    main()