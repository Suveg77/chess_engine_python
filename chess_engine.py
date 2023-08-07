class GameState():
    def __init__(self):
        # board is a 8x8 2d list. string "--" denotes empty strings.
        
        self.board=[
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
            ["bp", "bp", "bp", "bp", "bp", "bp","bp", "bp"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["wp", "wp", "wp", "wp", "wp", "wp","wp", "wp"]
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
      