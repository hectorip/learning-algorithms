class Stack():
    def __init__(self, initial_array=[]):
        if initial_array:
            self._stack = initial_array[:]
        else:
            self._stack = []
            self._maxes = []

    def push(self, el):
        self._stack.append(el)
        if self._maxes and el >= self._maxes[-1]:
            self._maxes.append(el)
        elif not self._maxes:
            self._maxes.append(el)

    def pop(self):
        if self._stack:
            el = self._stack.pop()
            if el == self._maxes[-1]:
                self._maxes.pop()
            return el

        return None

    def max(self):
        if self._maxes:
            return self._maxes[-1]

        return None


t = "12345"
t = "0162345"
e = "5432610"



s = Stack()
for el in t:
    s.push(int(el))

r = ""
print(s.max())

while True:
    el = s.pop()
    print(s.max())

    if not el:
        break
    r += str(el)
if r == e:
    print("Success")
else:
    print("File")

