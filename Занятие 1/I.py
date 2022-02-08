A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


def solve(A, B, C, D, E):
    if (A <= D and B <= E) or (A <= E and B <= D):
        return "YES"
    elif (A <= D and C <= E) or (A <= E and C <= D):
        return "YES"
    elif (B <= D and C <= E) or (B <= E and C <= D):
        return "YES"
    else:
        return "NO"


print(solve(A, B, C, D, E))
