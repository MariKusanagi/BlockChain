import hashlib as hl
complexity = 2

block = {
    'nonce': 0
}
# код для хеширования блока
hash_block = hl.sha256(str(block).encode()).hexdigest()
# print(hash)

#Цикл для нахождения nonce
while hash_block[0:complexity] != '0'*complexity:
    block['nonce'] += 1
    hash_block = hl.sha256(str(block).encode()).hexdigest()

print(block['nonce'])
print(hash_block)
