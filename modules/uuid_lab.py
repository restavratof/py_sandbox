import uuid

in_data = 'My database'

# make a UUID based on the host ID and current time
result1 = uuid.uuid1()
print(f'UUID 1 - {result1}')

# make a UUID using an MD5 hash of a namespace UUID and a name
result3 = uuid.uuid3(uuid.NAMESPACE_DNS, in_data)
print(f'UUID 3 - {result3}')

# make a random UUID
result4 = uuid.uuid4()
print(f'UUID 4 - {result4}')

# make a UUID using a SHA-1 hash of a namespace UUID and a name
result5 = uuid.uuid5(uuid.NAMESPACE_DNS, in_data)
print(f'UUID 5 - {result5}')

print('-'*50)

# make a UUID from a string of hex digits (braces and hyphens ignored)
x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
print(f'X - {str(x)}')

# get the raw 16 bytes of the UUID
xbytes = x.bytes
print(f'XBytes - {xbytes}')

# make a UUID from a 16-byte string
result = uuid.UUID(bytes=xbytes)
print(f'Result - {result}')
