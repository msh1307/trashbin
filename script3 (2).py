import gdb
import re
libc_base = 0
start = 0
gdb.execute("file ./prob")
gdb.execute("set disable-randomization off ")
gdb.execute("b * main+141")
while (True):
    gdb.execute("r")
    mem = gdb.execute("vmmap libc",to_string=True) # -> for provided libc
    p = re.compile("0x")
    idx = re.search(p,mem).start()
    libc_base = int(mem[idx:idx+18],16)
    main_arena = libc_base + 0x1ebbd8 #0x1ecbd8 
    start = main_arena& 0xfffffffffffff000
    print("start : "+hex(start))
    if(start & 0x000000000000f000 == 0):
        break
strlen = libc_base + 0x18b660
print("strlen : "+hex(strlen))

#gdb.execute("set {long long}"+hex(start+0xa8)+'='+hex((strlen & 0xffffffffffff0000)+i))
resar = []
for i in range(0x100):
    res = gdb.execute('x/20xi '+hex((strlen & 0xffffffffffff0000)+i),to_string=True)
    if('ret' in res):
        print(hex((strlen & 0xffffffffffff0000)+i))
        resar.append(hex((strlen & 0xffffffffffff0000)+i))


# gdb.execute("del breakpoints")
# gdb.execute("set {long long}"+hex(start+0xa8)+'='+resar[i])
# gdb.execute("b * puts+15")
# gdb.execute("c")

# main_arena = gdb.parse_and_eval("&main_arena") #-> for local libc
# start = (main_arena.cast(gdb.lookup_type("unsigned long long")) + 88) & 0xfffffffffffff000

# i = start + 0x110   
# for j in range(20):
#     gdb.execute("set {long long int}%d = 0x7f"%i)
#     print(hex(i) + ' = 0x7f')
#     i+=8
    
# printf strlen 040
# puts strlen 0a8

