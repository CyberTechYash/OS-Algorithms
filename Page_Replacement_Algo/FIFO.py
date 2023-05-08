# FIFO Replacement

capacity = int(input("Enter the number of frames: "))
s = list(map(int,input("Enter the reference string: ").strip().split()))
f,fault,top,pf = [],0,0,'No'

print("\nString|Frame →\t",end='')

for i in range(capacity):
    print(i,end=' ')

print("Fault\n   ↓\n")

for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)

        else:
            f[top] = i
            top = (top+1)%capacity

        fault += 1
        pf = 'Yes'

    else:
        pf = 'No'

    print("   %d\t\t"%i,end='')

    for x in f:
        print(x,end=' ')

    for x in range(capacity-len(f)):
        print(' ',end=' ')

    print(" %s"%pf)

print("\nTotal requests: %d\nTotal Page Faults: %d"%(len(s),fault))
