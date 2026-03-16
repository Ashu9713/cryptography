import pgpy

key = pgpy.PGPKey.new(pgpy.constants.PubKeyAlgorithm.RSAEncryptOrSign, 2048)

uid = pgpy.PGPUID.new('Alice', email='alice@example.com')

key.add_uid(
    uid,
    usage={pgpy.constants.KeyFlags.Sign, pgpy.constants.KeyFlags.EncryptCommunications},
    hashes=[pgpy.constants.HashAlgorithm.SHA256],
    ciphers=[pgpy.constants.SymmetricKeyAlgorithm.AES256],
    compression=[pgpy.constants.CompressionAlgorithm.ZLIB]
)

message = pgpy.PGPMessage.new("Hello this is a secret message")

encrypted = key.pubkey.encrypt(message)

decrypted = key.decrypt(encrypted)

print("Encrypted Message:")
print(encrypted)

print("Decrypted Message:")
print(decrypted.message)
