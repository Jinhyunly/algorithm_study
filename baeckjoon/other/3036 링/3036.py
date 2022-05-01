def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
num_list = list(map(int, input().split()))

for i in range(1, len(num_list)):
    gcd_num = gcd(num_list[0], num_list[i])
    # print(gcd_num)
    print(int(num_list[0] / gcd_num), num_list[i] // gcd_num, sep='/')