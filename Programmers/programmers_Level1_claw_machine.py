board = [[0, 0, 0, 0, 0],\
        [0, 0, 1, 0, 3],\
        [0, 2, 5, 0, 1],\
        [4, 2, 4, 4, 2],\
        [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
bucket = []
count = 0

for i in moves:
    for j in range (len (board)):
        if board[j][i - 1] == 0:
            continue
        bucket.append (board[j][i - 1])
        board[j][i - 1] = 0
        if len(bucket) <= 1:
            break
        if bucket[len(bucket) - 1] == bucket[len(bucket) - 2]:
            del bucket[len(bucket) - 1]
            del bucket[len(bucket) - 1]
            count += 2
            break
        else:
            break

print (count)