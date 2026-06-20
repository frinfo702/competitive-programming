n = int(input())

receiver_giver = [[0] * (n + 1) for _ in range(n + 1)]

for giver_i in range(1, n + 1):
    line = list(map(int, input().split()))
    k = line[0]
    receivers = line[1:]

    for receiver_i in receivers:
        receiver_giver[receiver_i][giver_i] = 1

for receiver_i in range(1, n + 1):
    givers = [
        giver_i
        for giver_i in range(1, n + 1)
        if receiver_giver[receiver_i][giver_i] == 1
    ]

    print(len(givers), *givers)
