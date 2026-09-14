from heaps.infinite_set import SmallestInfiniteSet

if __name__ == '__main__':
    smallestInfiniteSet = SmallestInfiniteSet()

    smallestInfiniteSet.addBack(2)
    # 2 is already in the set, so no change is made.

    print(smallestInfiniteSet.popSmallest())
    # return 1, since 1 is the smallest number,
    # and remove it from the set.

    print(smallestInfiniteSet.popSmallest())
    # return 2, and remove it from the set.

    print(smallestInfiniteSet.popSmallest())
    # return 3, and remove it from the set.

    smallestInfiniteSet.addBack(1)
    # 1 is added back to the set.

    print(smallestInfiniteSet.popSmallest())
    # return 1, since 1 was added back to the set
    # and is the smallest number, then remove it.

    print(smallestInfiniteSet.popSmallest())
    # return 4, and remove it from the set.

    print(smallestInfiniteSet.popSmallest())
    # return 5, and remove it from the set.