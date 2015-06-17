def perm(array, k, n):
    for i in range(k, n):
        tmp = array[k]; array[k] = array[i]; array[i] = tmp
        perm(array, k+1, n)
        tmp = array[k]; array[k] = array[i]; array[i] = tmp

perm([1, 2, 3, 4, 5], 0, 5)