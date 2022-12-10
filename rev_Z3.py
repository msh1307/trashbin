from z3 import *
s = Solver()
FLAG = [BitVec("FLAG_%d"%i,32) for i in range(4)]
name = [x for x in FLAG]
#name = b'abcd'
serial = b'76876-77776'

s.add(name[3] == ord('p'))
for i in range(4):
    s.add(name[i] >= ord('a'))
    s.add(name[i] <= ord('z'))
    
v40 = (name[0] & 1) + 5
v48 = ((name[0] >> 4) & 1) + 5
v42 = ((name[0] >> 1) & 1) + 5
v44 = ((name[0] >> 2) & 1) + 5
v46 = ((name[0] >> 3)  & 1) + 5
v32 = (name[1] & 1) + 1
v38 = ((name[1] >> 4) & 1) + 1
v34 = ((name[1] >> 1) & 1) + 1
v8 = ((name[1] >> 2) & 1) + 1
v36 = ((name[1] >> 3) & 1) + 1

s.add(v40 + v8 + ord('0') == serial[0])
s.add(v46 + v36 + ord('0') == serial[1])
s.add(v42 + v38 + ord('0') == serial[2])
s.add(v44 + v32 + ord('0') == serial[3])
s.add(v48 + v34 + ord('0') == serial[4])

v41 = (name[2] & 1) + 5
v49 = ((name[2] >> 4) & 1) + 5
v43 = ((name[2] >> 1) & 1) + 5
v45 = ((name[2] >> 2) & 1) + 5
v47 = ((name[2] >> 3) & 1) + 5
v33 = (name[3] & 1) + 1
v39 = ((name[3] >> 4) & 1) + 1
v35 = ((name[3] >> 1) & 1) + 1
v21 = ((name[3] >> 2) & 1) + 1
v37 = ((name[3] >> 3) & 1) + 1

s.add(v41 + v21 + ord('0') == serial[6])
s.add(v47 + v37 + ord('0') == serial[7])
s.add(v43 + v39 + ord('0') == serial[8])
s.add(v45 + v33 + ord('0') == serial[9])
s.add(v49 + v35 + ord('0') == serial[10])

if (s.check() == sat):
    for i in FLAG:
        print(chr(s.model()[i].as_long()),end='')

# buf = [0 for i in range(11)]
# buf[0] = (str(v40 + v8).encode())
# if(serial[0] == buf[0]):
#     buf[1] = (str(v46 + v36).encode())
#     if(serial[1] == buf[1]):
#         buf[2] = (str(v42 + v38).encode())
#         if(serial[2] == buf[2]):
#             buf[3] = (str(v44 + v32).encode())
#             if(serial[3] == buf[3]):
#                 buf[4] = (str(v48 + v34).encode())
#                 if(serial[4] == buf[4]):
#                     v41 = (name[2] & 1) + 5
#                     v49 = ((name[2] & 0x10) != 0) + 5
#                     v43 = ((name[2] & 2) != 0) + 5
#                     v45 = ((name[2] & 4) != 0) + 5
#                     v47 = ((name[2] & 8) != 0) + 5
#                     v33 = (name[3] & 1) + 1
#                     v39 = ((name[3] & 0x10) != 0) + 1
#                     v35 = ((name[3] & 2) != 0) + 1
#                     v21 = ((name[3] & 4) != 0) + 1
#                     v37 = ((name[3] & 8) != 0) + 1
#                     buf[6] = (str(v41 + v21).encode())
#                     if(serial[6] == buf[6]):
#                         buf[7] = (str(v47 + v37).encode())
#                         if(serial[7] == buf[7]):
#                             buf[8] = (str(v43 + v39).encode())
#                             if(serial[8] == buf[8]):
#                                 buf[9] = (str(v45 + v33).encode())
#                                 if(serial[9] == buf[9]):
#                                     buf[10] = (str(v49 + v35).encode())
#                                     if(serial[10] == buf[10]):
#                                         print("pass")
                                        

                                        
                                    