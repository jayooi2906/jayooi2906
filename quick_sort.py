def quick_sort(n, fir_index, last_index):
    if fir_index != last_index:
        x = 0
        pivot_num = n[last_index]
        i = 0
        j = len(n) - 1
        while i < last_index-1:
            if n[i] > pivot_num:
                break
            i += 1
        while j >= 0:
            if n[j] < pivot_num:
                break
            j -= 1
        if j > i:
            n[i], n[j] = n[j], n[i]
            quick_sort(n, 0, last_index-1)
        if i > j:
            n[i], n[last_index] = n[last_index], n[i]
            quick_sort(n, 0, i)
            quick_sort(n, i+1, last_index)





nums = [7, 3, 4, 1, 8, 5]

(quick_sort(nums, 0, len(nums) - 1))
print(nums)