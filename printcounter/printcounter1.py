import time
start_time = time.time()

counter = 0

print('Starting up')
for i in range(10):
    counter += 1
    print('The count is %d' % counter)
    print('---------------')
print('Finishing up')
print("--- %s seconds ---" % (time.time() - start_time))