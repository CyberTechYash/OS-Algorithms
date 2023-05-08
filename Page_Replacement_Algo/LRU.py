# LRU Replacement

capacity = int(input("Enter the number of frames: "))
s = list(map(int, input("Enter the reference string: ").strip().split()))
f, st, fault, pf = [], [], 0, 'No'

print("\nString|Frame →\t", end='')

for i in range(capacity):
    print(i, end=' ')

print("Fault\n   ↓\n")

for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
            st.append(len(f) - 1)

        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)

        pf = 'Yes'
        fault += 1

    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'No'

    print("   %d\t\t" % i, end='')

    for x in f:
        print(x, end=' ')

    for x in range(capacity - len(f)):
        print(' ', end=' ')

    print(" %s" % pf)

print("\nTotal Requests: %d\nTotal Page Faults: %d" % (len(s), fault))
