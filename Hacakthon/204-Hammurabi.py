import numpy as np

#---------------------#
# HAMMURABI IN PYTHON #
#---------------------#


# WELCOME MESSAGE 
print("------------------------------------------------")
print("HAMURABI")
print("CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
print("------------------------------------------------")
print("TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
print("FOR A TEN-YEAR TERM OF OFFICE")
print("------------------------------------------------")

Z=0
D1=0
P1=0
P=95
S=2800
H=3000
E=H-S
Y=3
A=H/Y
I=5
Q=1
D=0

print(f"HAMURABI: I BEG TO REPORT TO YOU,")
Z=Z+1
print(f"IN YEAR {Z}, {D} PEOPLE STARVED, {I} CAME TO THE CITY,")
P=P+I
if(Q>0):
    print(f"POPULATION IS NOW {P}")
P=int(P/2)
print("------------------------------------------------")
print("A HORRIBLE PLAGUE STRUCK! HALF THE PEOPLE DIED!!")
print("------------------------------------------------")

print(f"POPULATION IS NOW {P}")
print("------------------------------------------------")
print(f"THE CITY NOW OWNS {A} ACRES.")
print(f"YOU HARVESTED {Y} BUSHELS PER ACRE.")
print(f"YOU NOW HAVE {S} BUSHELS IN STORE.")
C = np.random.randint(0,10)
Y=C+17
print(f"LAND IS TRADING AT {Y} BUSHELS PER ACRE.")

while(True):
    Q = int(input("HOW MANY ACRES DO YOU WISH TO BUY? "))
    if (Q < 0):
        print("------------------------------------------------")
        print("HAMURABI: I CANNOT DO WHAT YOU WISH.")
        print("GET YOURSELF ANOTHER STEWARD!!!!!")
        print("------------------------------------------------")
        break
    elif (Y * Q <= S or Q == 0):
        A=A+Q
        S=S-(Y*Q)
        C=0
        while(True):
            Q = int(input("HOW MANY ACRES YOU WISH TO SELL? "))
            if(Q < 0):
                print("------------------------------------------------")
                print("HAMURABI: I CANNOT DO WHAT YOU WISH.")
                print("GET YOURSELF ANOTHER STEWARD!!!!!")
                print("------------------------------------------------")
                break
            elif(Q<A or Q == 0):
                A=A-Q
                S=S+(Y*Q)
                C=0
                break
            else:
                print("------------------------------------------------")
                print(f"HAMURABI: THINK AGAIN. YOU HAVE ONLY {A} ACRES.")
                print("NOW THEN,")
                continue
            
        break
    else:
        print("------------------------------------------------")
        print(f"HAMURABI: THINK AGAIN. YOU HAVE ONLY {S} BUSHELS")
        print("OF GRAIN. NOW THEN,")
        continue
           
        
# This will happen when the 10 year tenure has passed !
#if(Z==11):
 #   print(f"IN YOUR 10-YEAR TERM OF OFFICE, {P1} PERCENT OF THE")
  #  print(f"POPULATION STARVED PER YEAR ON THE AVERAGE,")
   # print(f", I.E. A TOTAL OF {D1} PEOPLE DIED! ")
    #L = A/P
    
print("------------------------------------------------")
