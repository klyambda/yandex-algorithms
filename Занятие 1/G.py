N, K, M = map(int, input().split())


def details_count(N, K, M):
    if N < K or K < M:
        return 0

    d_count = 0
    while N >= K:
        # количество заготовок
        z_count = N // K
        # оставшийся материал от заготовок
        remainder = N % K
        # количество деталей
        d_count += z_count * (K // M)
        # добавляем к общему остатку остаток от изготовления деталей
        remainder += z_count * (K % M)
        N = remainder
        remainder = 0

    return d_count


print(details_count(N, K, M))
