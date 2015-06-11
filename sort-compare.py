from datetime import datetime
import random

N = 10000
arr = [random.randint(0,10000) for r in xrange(N)]

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp


def merge_sort(a):
    if len(a) > 1:
        mid = len(a) / 2        # Determine the midpoint and split
        left = a[0:mid]
        right = a[mid:]

        merge_sort(left)            # Sort left list in-place
        merge_sort(right)           # Sort right list in-place

        l_index, r_index = 0, 0
        for i in range(len(a)):     # Merging the left and right list
            l_val = left[l_index] if l_index < len(left) else None
            r_val = right[r_index] if r_index < len(right) else None

            if (l_val and r_val and l_val < r_val) or r_val is None:
                a[i] = l_val
                l_index += 1
            elif (l_val and r_val and l_val >= r_val) or l_val is None:
                a[i] = r_val
                r_index += 1


def quick_sort(a):
    if len(a) > 1:
        pivot_index = len(a) / 2
        pivot = a[pivot_index]
        left_items = []
        right_items = []

        for i, val in enumerate(a):
            if i != pivot_index:
                if val < pivot:
                    left_items.append(val)
                else:
                    right_items.append(val)

        quick_sort(left_items)
        quick_sort(right_items)
        a[:] = left_items + [a[pivot_index]] + right_items


start = datetime.now()

# bubble_sort(arr)
# merge_sort(arr)
quick_sort(arr)

end = datetime.now()
print "Time: ", end - start