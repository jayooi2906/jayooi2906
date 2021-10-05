def merge_sort(n):
    fir_half = []
    sec_half = []
    final_list = []
    for i in range(len(n) // 2):
        fir_int = n[0]
        fir_half.append(fir_int)
        n.remove(n[0])
    sec_half = n
    for i in range(len(fir_half)-1):
        if fir_half[i] >= fir_half[i+1]:
            fir_int = fir_half[i]
            fir_half.remove(fir_half[i])
            fir_half.append(fir_int)
    for j in range(len(sec_half)-1):
        if sec_half[j] >= sec_half[j+1]:
            sec_int = sec_half[j]
            sec_half.remove(sec_half[j])
            sec_half.append(sec_int)
    i = 0
    j = 0
    a = len(fir_half)
    b = len(sec_half)
    while i < a and j < b:
        if fir_half[0] < sec_half[0]:
            final_list.append(fir_half[0])
            fir_half.remove(fir_half[0])
            i += 1
        else:
            final_list.append(sec_half[0])
            sec_half.remove(sec_half[0])
            j += 1

    final_list.extend(fir_half)
    final_list.extend(sec_half)
    print(fir_half, sec_half)
    print(final_list)


nums = [4, 1, 3, 9, 7]
#print(merge_sort(nums))