#! /usr/local/bin/python3


def main():
    l = [1, 2, 3]
    print(l * 5)
    # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    print(5 * 'abcd')
    # 'abcdabcdabcdabcdabcd'

    board = [['_'] * 3 for i in range(3)]
    print(board)
    # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    board[1][2] = 'X'
    print(board)
    # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

    board = []
    for i in range(3):
        row = ['_'] * 3
        board.append(row)
    print(board)
    # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    board[2][0] = 'X'
    print(board)
    # [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]


if __name__ == "__main__":
    main()
