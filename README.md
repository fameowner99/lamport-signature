# 🔏 Lamport One-Time Signatures 🔏

Lamport one-time signature scheme is a simple but effective mechanism for creating signatures built on top of hash functions.
Any cryptograph hash function can be used to implement the scheme.
Signatures using large hash functions are understood so far to be "quantum resistant"

## ⚠ Warning ⚠

The lamport one-time signature scheme uses 50% of your **private** key as the signature, this is why they are for one time use only.

Do not use a single private key to sign more than once piece of data.

## How to use

1) python generate_keys.py - creates private and public keys
2) python sign_message.py - generate signature for message
3) python verify_signature.py - verify message with signature