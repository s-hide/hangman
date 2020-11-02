def hangman(word):
    wrong = 0
    stage = ["",
             "_____      "
             "|          "
             "|    |     "
             "|    O     "
             "|   /| \   "
             "|   / \    "
             "|          "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
