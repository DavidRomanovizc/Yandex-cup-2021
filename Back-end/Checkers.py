a = input()
x1 = int(a.split(" ")[0])
x2 = int(a.split(" ")[1])
white_count = int(input())
white = []
for i in range(white_count):
    tmp = input()
    white.append([int(tmp.split(" ")[0]), int(tmp.split(" ")[1])])
    tmp = 0
black_count = int(input())
black = []
for i in range(black_count):
    tmp = input()
    black.append([int(tmp.split(" ")[0]), int(tmp.split(" ")[1])])
    tmp = 0
answer = 0
first = input()
if first == "white":

    for i in white:
        for j in black:

            if (abs(i[0] - j[0]) == 1) and (abs(i[1] - j[1]) == 1):
                x = [(i[0] - (2 * (i[0] - j[0]))), (i[1] - (2 * (i[1] - j[1])))]
                if 0 < x[0] < (x1 + 1) and 0 < x[1] < (x2 + 1):
                    if (x not in black) and (x not in white):
                        if answer != 1:
                            print("Yes")
                            answer = 1



else:
    for i in black:
        for j in white:
            if (abs(i[0] - j[0]) == 1) and (abs(i[1] - j[1]) == 1):
                x = [(i[0] - (2 * (i[0] - j[0]))), (i[1] - (2 * (i[1] - j[1])))]
                if 0 < x[0] < (x1 + 1) and 0 < x[1] < (x2 + 1):
                    if (x not in black) and (x not in white):

                        if answer != 1:
                            print("Yes")
                            answer = 1
if answer == 0:
    print("No")
