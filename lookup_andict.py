from ADict import ADict
import time

file = open('fixture.csv', 'r')

ad = ADict.ADict()

start_time = time.time()
print("creating ADict from file...")
for line in file.read().splitlines():
    split = line.split(',')
    #ad.put(split[0], split[1])
    ad.putUnsafe(split[0], split[1])

created_time = time.time()

print("performing lookup...")
print ad.get('8888888')

end_time = time.time()

print "create: " + str(created_time - start_time)
print "lookup: " + str(end_time - created_time)
