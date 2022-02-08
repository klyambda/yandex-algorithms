troom, tcond = map(int, input().split())
mode = input()


def conditioner(troom, tcond, mode):
    if mode == "freeze":
        return min(troom, tcond)

    elif mode == "heat":
        return max(troom, tcond)

    elif mode == "auto":
        return tcond

    elif mode == "fan":
        return troom


print(conditioner(troom, tcond, mode))
