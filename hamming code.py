def parityBits(lst):
    for pos in pos_p:
        i = pos
        temp=[]
        while(i<m+p):
            temp.extend(lst[i:pos+i+1])
            i=(pos+i+1)+pos+1
        count_ones="".join(temp).count('1')
        if(count_ones%2)==0:
            lst[pos]='0'
        else:
            lst[pos]='1'
    return lst
    
def toggleBits(lst, ep):
    if(lst[ep]=='1'):
        lst[ep]='0'  
    else:
        lst[ep]='1'
    return lst
    
def printParity(lst):
    for i in pos_p:
        print('P',i+1,' : ',lst[i], sep="")
    
    
s=input("Enter the message to Encode: ")
l=[bin(ord(c)) for c in s]
k=[]
for i in range(len(l)):
    l[i]=l[i].replace("0b","")
    l[i]=l[i].zfill(8)
    k.extend(list(l[i]))
l=k
print("Sender Message in Binary : ","".join(l))
m=len(l)
for p in range(1,m+1):
    if(2**p >= m+p+1):
        break
print("no. of parity bits : ",p)

pos_p=[]
for i in range(p):
    l.insert((2**i)-1, 'x')
    pos_p.append((2**i)-1)

l=parityBits(l)
hamming_code="".join(l)

print("Parity Bits/ Redundant Bits for Sent Message :")
printParity(hamming_code)
print("The Hamming code for given message is(even parity) {SENDER} :",hamming_code)     

receiver_code=list(hamming_code)
# error_pos = 6-1
error_pos=int(input('Enter position to change the bit : '))-1

receiver_code = toggleBits(receiver_code, error_pos) 
print("The Received code is (after error) {RECEIVER} :","".join(receiver_code))     
receiver_code=parityBits(receiver_code)
print("Parity Bits/ Redundant Bits for Received Message :")
printParity(receiver_code)

error_index=""
pos_p.reverse()
for i in pos_p:
    error_index = error_index + receiver_code[i]
error_index = int(error_index,2)-1                          #error pos
receiver_code=toggleBits(receiver_code,error_index)         #corrected receiver_code
print("Error detected and corrected at position :",error_index+1)       
# print("corrected receiver code : ","".join(receiver_code))       

for i in pos_p:                              #removing parity bits
    receiver_code.pop(i)

receiver_code="".join(receiver_code)         #Message in binary format
print("Received Message in Binary : ",receiver_code)

decoded_list=[]
for i in range(0, len(receiver_code), 8):
    decoded_list.append(receiver_code[i:i+8])

decoded_msg=""
for i in decoded_list:
    decoded_msg= decoded_msg + chr(int(i,2))
print("Decoded Message at Receiver Side : ",decoded_msg).63

3\
