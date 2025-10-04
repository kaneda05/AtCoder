import sys

def solve():
    
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()

    prefix_zeros = [0] * (N + 1)
    prefix_ones = [0] * (N + 1)
    for i in range(N):
        prefix_zeros[i+1] = prefix_zeros[i] + (1 if S[i] == '0' else 0)
        prefix_ones[i+1] = prefix_ones[i] + (1 if S[i] == '1' else 0)

    cost_to_zero = N
    if prefix_zeros[N] > 0:
        min_cost_zero = float('inf')
        i = 0
        while i < N:
            if S[i] == '0':
                j = i
                while j + 1 < N and S[j+1] == '0':
                    j += 1
                
                outside_chars = i + (N - 1 - j)
                outside_zeros = prefix_zeros[i] + (prefix_zeros[N] - prefix_zeros[j+1])
                
                cost = outside_chars + outside_zeros
                min_cost_zero = min(min_cost_zero, cost)
                i = j + 1
            else:
                i += 1
        cost_to_zero = min_cost_zero

    cost_to_one = N
    if prefix_ones[N] > 0:
        min_cost_one = float('inf')
        i = 0
        while i < N:
            if S[i] == '1':
                j = i
                while j + 1 < N and S[j+1] == '1':
                    j += 1

                outside_chars = i + (N - 1 - j)
                outside_ones = prefix_ones[i] + (prefix_ones[N] - prefix_ones[j+1])

                cost = outside_chars + outside_ones
                min_cost_one = min(min_cost_one, cost)
                i = j + 1
            else:
                i += 1
        cost_to_one = min_cost_one

    print(min(cost_to_zero, cost_to_one))


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        solve()
    
if __name__ == "__main__":
    main()