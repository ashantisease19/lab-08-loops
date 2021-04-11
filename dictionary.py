myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
v = []
f = []
for a, x, in myData.items():
    print('key:', a, ', value:', x)
    v.append(a)
    f.append(x)
    print('all keys:', v, ', all values:', f)
