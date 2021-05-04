# Finding all subsets in an array


def all_subsets(arr):
    if not arr:
        return [[]]  # the empty subset
    el = arr[0]
    prev_subsets = all_subsets(arr[1:])
    new_subsets = []
    for subset in prev_subsets:
        ns = subset[:]
        ns.append(el)
        new_subsets.append(ns)
    r = prev_subsets + new_subsets
    # breakpoint()
    return r


if __name__ == "__main__":
    example = list(range(100))
    print(all_subsets(example))
