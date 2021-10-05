
def recur_merge(n):
    if len(n) > 1:
        mid = len(n)//2
        fir_half = n[:mid]
        sec_half = n[mid:]
        recur_merge(fir_half)
        recur_merge(sec_half)
        i = 0
        j = 0
        k = 0
        while i < len(fir_half) and j < len(sec_half):
            if fir_half[i] > sec_half[j]:
                n[k] = sec_half[j]
                j += 1
            else:
                n[k] = fir_half[i]
                i += 1
            k += 1

        while i < len(fir_half):
            n[k] = fir_half[i]
            i += 1
            k += 1
        while j < len(sec_half):
            n[k] = sec_half[j]
            j += 1
            k += 1


