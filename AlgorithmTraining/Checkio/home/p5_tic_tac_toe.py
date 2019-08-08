def checkio(game_result):
    def judge(R):
        for i in R:
            if i.count("X") == 3:
                return "X"
            if i.count("O") == 3:
                return "O"
    # Horizontal line, go straight with judge()

    # Vertical line
    def f(n):
        v = []
        for i in range(3):
            v.append(game_result[i][n])
        return v

    # corss line
    c1 = []; c2 = []; cline = [c1, c2]
    for i in list(range(3)):
        c1.append(game_result[i][2-i])
    for i in list(range(3)):
        c2.append(game_result[i][i])

    # Return result
    return judge(game_result) or judge(list(map(f, (0, 1, 2)))) or judge(cline) or "D"


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
