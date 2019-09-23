from pprint import pprint

keys = 'yu derrick brian erik isabel'.split()
color = 'blue orange green yellow red'.split()
city =  'shanghai tokyo sunnyvale san_jose taipei'.split()
fruit = 'apple banana orange pear peach'.split()

hashes = list(map(abs, map(hash, keys)))
entries = list(zip(hashes, keys, color))

def separate_chaining(n):
    buckets = [[] for i in range(n)]
    for pair in entries:
        h, key, value = pair
        # naive hash function
        i = h % n
        buckets[i].append(pair)
    pprint(buckets)

separate_chaining(8)