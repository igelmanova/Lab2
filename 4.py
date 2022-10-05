A = list(map(int, input().split()))
if len(A) < 4:
    print("Error. Enter more than 3 numbers")
else:
    A1 = A.copy()
    del A[A.index(max(A))]
    del A[A.index(min(A))]
    print(A1, A)
# A = lst_numbers
# A1 = lst_no_extremum