a = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
n = len(a)
m = 2

def __lfu():
    global a, n, m
x = 0
page_faults = 0
page = []
time = {}
b = list(a)

for i in range(m):
    page.append(-1)

for i in a:
    time[i] = 0

for i in range(n):
    flag = 0
    for j in range(m):
        if (page[j] == a[i]):
            flag = 1
            time[a[i]] += 1
            break

    if flag == 0:
        rpage = -1
        if page[x] != -1:

            t = []
            for k in page:
                t.append(time[k])

            minis = min(t)

            gpage = []
            for k in page:
                if time[k] == minis:
                    gpage.append(k)

            maxi = -1
            flag = 0

            for k in gpage:
                for n in range(0, i):
                    if (k == b[n]):
                        if maxi == -1:
                            maxi = n
                            rpage = k
                        elif n < maxi:
                            maxi = n
                            rpage = k
                flag = 1

            if (flag == 1):
                b[maxi] = -1
                x = page.index(rpage)

        if rpage != -1:
            time[rpage] = 0

        page[x] = a[i]
        x = (x + 1) % m
        time[a[i]] += 1
        page_faults += 1
        print("\n#->" , (a[i]))
        for j in range(m):
            if page[j] != -1:
                print(page[j])
            else:
                print("-")
    else:
        print("\n#-> No Page Fault" ,a[i])

print("\nTotal page faults : ",page_faults)
print("\nFrequencies of pages: ", time)