N = int(input())
T = input()

prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + (1 if T[i] == '1' else 0)
ans = 0

count = {0:1}
for i in range(N):
    idx_parity = (i+1) % 2
    ps_parity = prefix_sum[i+1] % 2
    current_xor_sum = idx_parity ^ ps_parity

    if current_xor_sum in count:
        ans += count[current_xor_sum]
        count[current_xor_sum] += 1
    else:
        count[current_xor_sum] = 1

print(ans)