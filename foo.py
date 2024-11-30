bar = input()
foo = []
c = 1
small = 1
maxx = 1

for i in range(len(bar)):
    foo.append(bar[i])
baz = i in range(len(foo) -1, -1, -1)
	
if baz == False:
    print("Something went wrong")
    c = 0
if foo[i] > foo[i -1]:
    small = i - 1
    maxx = i
print(small, maxx, len(foo), foo, end="")
for i in range(small + 1, len(foo)):
    if foo[i] > foo[small] and foo[i] < foo[maxx]:
        maxx =  i
foo[small], foo[maxx] = foo[maxx], foo[small]
foo = foo[: small +1] + sorted(foo[small + 1 :])
if c:
    for i in range(len(foo)):
        print(foo[i], end="")
