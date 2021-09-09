lst = list(map(int, input().split()))

st = set()
for num in lst:
    if (num in st):
        print("YES")
    else:
        st.add(num)
        print("NO")
