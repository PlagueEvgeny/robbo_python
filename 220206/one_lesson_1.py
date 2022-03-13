i = 1
p = 1
while i < 10:
    while p < 10:
        print(i * p, end='\t')
        p += 1
    print("\n")
    p = 1
    i += 1


for c1 in "abc":
    for c2 in 'cba':
        for c3 in "bac":
            print(f"{c1}{c2}{c3}")



