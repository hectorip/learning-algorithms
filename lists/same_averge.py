# Return true if the list can be divided in two sublists with the same average

# Hypotesis
# If you find a subset with the same averge than the complete list,
# the complement will have the same average.

# Proof (Try):
# The averge of an array A is sum(A)/len(A) if B is subset of with the same average the
# complement, we will call C the complement of B. So its average is: avg(C) = (sum(A) - sum(B))/(len(A)-len(B))
# avg(B) = (sum(A) - sum(C))/(len(A)-len(C))
# 2avg(A) = ()

# [0, 0, 9, 3]

def average(a):
    return sum(a)/len(a)

def get_complement(a, a2):
    return [x for x in a if x not in a2]


def traverse_all_subsets(a, c=[], avg=None):
    print("A:", a, len(a))
    print("AVG:", avg)
    if not(len(a)-1):
        print("OUT")
        return False
    print("DDDD")
    if avg is None:
        # size = len(a)
        a = sorted(a)
        a.reverse()
        avg = sum(a)/len(a)

    for i, e in enumerate(a):
        print("A loop:", a, len(a))
        cd = c + [e]
        print(c)
        print("element: ", e)
        c_avg = average(cd)
        if c_avg == avg:
            print("Found!")
            print("B: ", cd)
            print("C: ", get_complement(a, cd))
            return True
        # if c_avg > avg:
        #     return False
        if traverse_all_subsets(a[i+1:], cd, avg):
            return True
    return False


input = [1, 2, 3, 4, 5, 6, 7, 8]
input = [1, 2, 3, 4, 3, 1, 814332, 8, 9, 1, 2, 3, 4, 3, 1,
        814332, 8, 9, 1, 2, 3, 4, 3, 1, 814332, 8, 9, 814332, 8, 9, 1, 2, 3, 4, 3, 1, 814332, 8, 9,1]

traverse_all_subsets(input)


def search_average(a):
    a = sorted(a)
