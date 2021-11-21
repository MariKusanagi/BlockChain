import hashlib

text = input();
byte_text = text.encode() # Переводим в байтык
hash_text_sha256 = hashlib.sha256(text.encode()).hexdigest()
hash_text_sha384 = hashlib.sha384(text.encode()).hexdigest()
# hash_text_sha512 = hashlib.she512(text.encode()).hexdigets()

print("sha256: " + hash_text_sha256)
print("sha384: " + hash_text_sha384)
#print("sha512: " + hash_text_sha512)
