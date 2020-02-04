def secondGreatLow(arr):
    arr.sort()
    if arr:
        if len(arr) > 2:
            print("{} {}".format(arr[0], arr[-2]))
        else:
            print("{} {}".format(arr[0], arr[1]))
    else:
        print("array will not be empty")

secondGreatLow([7,12,7,98,106])

secondGreatLow([12,7])

secondGreatLow([])
