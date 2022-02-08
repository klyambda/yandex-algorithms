a = int(input())
b = int(input())
n = int(input())
m = int(input())
a = int(input())
b = int(input())
n = int(input())
m = int(input())


def print_min_max_time(a, b, n, m):
	t_min = max(n + (n - 1) * a, m + (m - 1) * b)
	t_max = min(n + (n + 1) * a, m + (m + 1) * b)

	if t_max < t_min:
		print(-1)
	else:
		print(t_min, t_max)

print_min_max_time(a, b, n, m)

def print_min_max_time(a, b, n, m):
	t_min = max(n + (n - 1) * a, m + (m - 1) * b)
	t_max = min(n + (n + 1) * a, m + (m + 1) * b)

	if t_max < t_min:
		print(-1)
	else:
		print(t_min, t_max)

print_min_max_time(a, b, n, m)