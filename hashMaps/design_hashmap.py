class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.bucket = [None] * self.size

    def put(self, key, val):
        index = key % self.size

        if not self.bucket[index]:
            self.bucket[index] = ListNode(key, val)
        else:
            cur = self.bucket[index]

            while cur:
                if cur.key == key:
                    cur.val = val
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = ListNode(key, val)

    def get(self, key):
        index = key % self.size

        cur = self.bucket[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        index = key % self.size
        prev = cur = self.bucket[index]

        if not cur:
            return
        if cur.key == key:
            self.bucket[index] = cur.next
            return

        cur = cur.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                break
            else:
                cur = cur.next
                prev = prev.next
