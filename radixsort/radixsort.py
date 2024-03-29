@profile
def radixsort( aList ):
    RADIX = 4
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range( RADIX )]

        # split aList between lists
        for i in aList:
            tmp = i // placement
            buckets[int(int(tmp) % RADIX)].append( int(i) )
            if maxLength and tmp > 0:
                maxLength = False
        # empty lists into aList array
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX
    return aList
