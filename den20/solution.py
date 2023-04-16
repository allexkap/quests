from base64 import b64decode
from itertools import cycle

raw = b64decode(open('raw', 'rb').read())

for key in ('stage II', 'stage III', 'stage IV'):
    raw = bytes(d ^ k for d, k in zip(raw, cycle(key.encode())))

print(raw.decode(errors='replace'))
