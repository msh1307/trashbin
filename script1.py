import gdb
import re

gdb.execute("file ./prob")
gdb.execute("set disable-randomization off ")
gdb.execute("b * main+141")

while (True):
    gdb.execute("r")
    mem = gdb.execute("vmmap libc",to_string=True) # -> for provided libc
    p = re.compile("0x")
    idx = re.search(p,mem).start()
    libc_base = int(mem[idx:idx+18],16)
    main_arena = libc_base + 0x1ebbd8
    start = main_arena& 0xfffffffffffff000
    print("start : "+hex(start))
    if(start & 0x000000000000f000 == 0):
        break
    
# main_arena = gdb.parse_and_eval("&main_arena") #-> for local libc
# start = (main_arena.cast(gdb.lookup_type("unsigned long long")) + 88) & 0xfffffffffffff000


# i = start + 0x110   
# for j in range(20):
#     gdb.execute("set {long long int}%d = 0x7f"%i)
#     print(hex(i) + ' = 0x7f')
#     i+=8
    
# printf strlen 040
# puts strlen 0a8

'''
gef➤  x/20xi 0x00007f3ddd490007
   0x7f3ddd490007:      mov    eax,DWORD PTR [rcx+rax*4]
   0x7f3ddd49000a:      sub    eax,edx
   0x7f3ddd49000c:      ret
'''