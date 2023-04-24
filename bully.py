# Bully Algorithm
n = int(input("Enter Number of process: "))
active={}
for i in range(0,n):
    active[i] = True
print(f"Process {n-1} has crashed")
active[n-1] = False
c = int(input("Enter Coordinator ID: "))
ok = []
for i in range(c+1,n):
    print(f"Coordinator message sent to {i}")
    if active[i] == True:
        ok.append(i)
        print(f"Okay message from {i}")
c = ok[0]
for i in range(0,len(ok)):
    print("New Elections Start")
    e = ok[i]
    for j in range(e+1,n):
        print(f"Election message sent from {e} to {j}")
        if active[j] == True:
            c = j
            print(f"Okay message from {j}") 
print(f"Final cooradinator is {c}")
for i in range(0,n):
    if(i != c and i < c):
        print(f"Message to {i}: Coordinator is {c}")   