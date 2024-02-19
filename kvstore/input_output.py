# Ejercicio: https://jojozhuang.github.io/algorithm/problem-versioned-key-value-store

class KVStore():
    def __init__(self):
        self._version = 0
        self._store = {}

    def PUT(self, key, value):
        self._version += 1
        key_store = self._store.get(key, [])
        key_store = [(self._version, value)] + key_store
        self._store[key] = key_store

        return self._version

    def GET(self, key, version=None):
        key_store = self._store.get(key)
        value = None

        if not key_store:
            return value

        if not version:
            value = key_store[0]
        else:
            for v, val in key_store:
                if v <= version:
                    value = (v, val)
                    break
        return value
    def print(self):
        print(self._store)


kv = KVStore()

while True:
    command = input("Give me a command:")
    if not command:
        print("Bye!")
        break

    parts = command.lower().strip().split(" ")

    if parts[0] == "put":
        v = kv.PUT(parts[1], int(parts[2]))
        print(f"PUT(#{v}) {parts[1]} = {parts[2]}")
    elif parts[0] == "get":
        params_len = len(parts[1:])
        v = None
        if params_len == 2:
            v = kv.GET(parts[1], int(parts[2]))
            if not v:
                print(f"GET {parts[1]}(#{parts[2]}) = <NULL>")
            else:
                print(f"GET {parts[1]}(#{parts[2]})  = {v[1]}")
        elif params_len == 1:
            v = kv.GET(parts[1])
            if not v:
                print(f"GET {parts[1]} = <NULL>")
            else:
                print(f"GET {parts[1]} = {v[1]}")
    else:
        kv.print()
