import time

start = time.time()
end = time.time()


print('ready')

s = time.time()
e = time.time()
while (end-start) <= 4.5*3:
    e = end = time.time()
    dt  = e - s

    if   dt == 0.5:
        print('rock')
    elif dt == 1:
        print('paper')
    elif dt == 1.5:
        print('scissors')
    elif dt == 4.5:
        print('reset')
        s = time.time()
    elif dt > 1.5 and dt < 4.5:
        continue
print( end - start)