def Nand(A,B):

    if A>1:
        return None
    if B>1:
        return None

    if A==0:
        if B==0: 
            return A , B , 1
        if B==1:
            return A , B , 1

    if A==1:
        if B==0: 
            return A , B , 1
        if B==1:
            return A , B , 0



def Full_Adder(A,B,C):

    if A>1:
        return None
    if B>1:
        return None
    if C>1:
        return None

    Sum=0
    carry=0

    Sum=A+B+C               #   'sum' is an inbult function, hence use 'Sum' with capital 'S'

    if Sum==2:
        Sum=0
        carry=1

    if Sum==3:
        Sum=1
        carry=1    
    
    return A , B , C , Sum , carry




print("\nNand Truth Table\n\n(A, B, X)")
print(Nand(0,0))
print(Nand(0,1))
print(Nand(1,0))
print(Nand(1,1))

print("\nFull_Adder Truth Table\n\n(A, B, C, S, C)")
print((Full_Adder(0,0,0)))
print((Full_Adder(0,0,1)))
print((Full_Adder(0,1,0)))
print((Full_Adder(0,1,1)))
print((Full_Adder(1,0,0)))
print((Full_Adder(1,0,1)))
print((Full_Adder(1,1,0)))
print((Full_Adder(1,1,1)))