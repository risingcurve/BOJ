n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
sum_list = []

for i in range(6):
    max_dice_list = []
    bottom_dice = [1,2,3,4,5,6]

    bottom_side = dice[0][i]
    upper_side = dice[0][rotate[i]]

    bottom_dice.remove(bottom_side)
    bottom_dice.remove(upper_side)

    max_dice_list.append(max(bottom_dice))

    for j in range(1, n):
        next_dice = [1,2,3,4,5,6]
        bottom_side = upper_side

        upper_side_index = rotate[dice[j].index(upper_side)]
        upper_side = dice[j][upper_side_index]

        next_dice.remove(bottom_side)
        next_dice.remove(upper_side)

        max_dice_list.append(max(next_dice))

    sum_list.append(sum(max_dice_list))

print(max(sum_list))