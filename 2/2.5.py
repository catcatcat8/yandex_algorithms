folders = int(input())
diploms = list(map(int, input().split()))
diploms.remove(max(diploms))
print(sum(diploms))
