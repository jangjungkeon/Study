def solution(places):
    for i in range(5):
        for j in range(5):
            places[i][j] = list(places[i][j])

    result = [1 for _ in range(5)]
    chk_1_dx = [1, -1, 0, 0]
    chk_1_dy = [0, 0, 1, -1]
    chk_2_dx = [2, -2, 0, 0]
    chk_2_dy = [0, 0, 2, -2]
    chk_3_dx = [1, 1, -1, -1]
    chk_3_dy = [-1, 1, -1, -1]

    for i in range(5):
        chk = False
        for j in range(5):
            if chk:
                break
            for k in range(5):
                if chk:
                    break
                if places[i][j][k] == "P":
                    for m in range(4):
                        x1 = j + chk_1_dx[m]
                        y1 = k + chk_1_dy[m]
                        if 0 <= x1 < 5 and 0 <= y1 < 5 and places[i][x1][y1] == "P":
                            result[i] = 0
                            chk = True
                            break

                        x2 = j + chk_2_dx[m]
                        y2 = k + chk_2_dy[m]
                        if 0 <= x2 < 5 and 0 <= y2 < 5 and places[i][x2][y2] == "P":
                            if places[i][(j+x2)//2][(k+y2)//2] != "X":
                                result[i] = 0
                                chk = True
                                break

                        x3 = j + chk_3_dx[m]
                        y3 = k + chk_3_dy[m]
                        if 0 <= x3 < 5 and 0 <= y3 < 5 and places[i][x3][y3] == "P":
                            if places[i][x3][k] != "X" or places[i][j][y3] != "X":
                                result[i] = 0
                                chk = True
                                break
    return result