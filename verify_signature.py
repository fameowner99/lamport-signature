import hashlib

def read_signature():
	 with open("signature/lamport.sign") as f:
	 	return f.read().splitlines()

def hash_signature(private_key_signature):
	return [generate_hash(value) for value in private_key_signature]

def generate_hash(input):
	return hashlib.md5(str(input).encode('utf-8')).hexdigest()

def read_public_key():
	 with open("keys/lamport.pub") as f:
	 	lines = f.readlines()
	 	return [line.split() for line in lines]

def get_hash_byte_array(hash):
	num_of_characters = 2
	splitted_array = [hash[i:i + num_of_characters] for i in range(0, len(hash), num_of_characters)]
	return [int(numeric_string, 16) for numeric_string in splitted_array]

def main():
	message = input("Enter message to validate with ./signature/lamport.sign signature: \n")

	private_key_signature = read_signature()
	hashed_private_key_signature = hash_signature(private_key_signature)

	message_hash = generate_hash(message)
	bytes_array = get_hash_byte_array(message_hash)

	public_key_values = read_public_key()

	public_key_signature = []
	bits_in_byte = 8
	for idx, num in enumerate(bytes_array):
		for i in range(0, bits_in_byte):
			public_key_index = idx * bits_in_byte + i;
			if (num & 1 << i):
				public_key_signature.append(public_key_values[public_key_index][1])
			else:
				public_key_signature.append(public_key_values[public_key_index][0])

	if (hashed_private_key_signature == public_key_signature):
		print("Signature signature/lamport.sign VALID for message " + message)
	else:
		print("Signature signature/lamport.sign NOT VALID for message " + message)

if __name__ == "__main__":
    main()