def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid                  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

entrada = int(input())

elementos =list(map(int,input().split()))

elementos.sort()

casos = int(input())

for i in range(casos):
    a,b=map(int,input().split())
    aP=binary_search(elementos,a)
    bP=binary_search(elementos,b)
    print(f"{abs(aP-bP)} kms")