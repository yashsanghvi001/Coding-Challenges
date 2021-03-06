def compute(ca,cb,ma,mb):
    if (ma==0 and mb==0) or (ca==0 and cb==0) :
        return 0
    if ma==0 or ca==0:
        return mb
    if mb==0 or cb==0:
        return ma
    if ca==cb :
        return 2*ca
    if ca<cb :
        min_groups = ca
        max_groups = ca+1
        max_limit = mb
        max_count = cb
    else :
        min_groups = cb
        max_groups = cb+1
        max_limit = ma
        max_count = ca
    if max_groups*max_limit>=max_count:
        return min_groups+max_count
    else :
        return min_groups+max_groups*max_limit


def main():
    countA = int(input())
    countB = int(input())
    maxA = int(input())
    maxB = int(input())

    print(compute(countA, countB, maxA, maxB))

if __name__ == '__main__':
    main()
