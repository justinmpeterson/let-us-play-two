class Player:
    def __init__(self, p_Id, p_First, p_Last, p_Pos, p_Class):
        self.info = {"player_id": p_Id,
            "first_name": p_First,
            "last_name": p_Last,
            "position": p_Pos,
            "classification": p_Class}
        self.game_info = {"gs": 0,
            "gp": 0}
        self.bat_stats = {"pa": 0,
            "ab": 0,
            "h": 0,
            "2b": 0,
            "3b": 0,˝
            "hr": 0,
            "so": 0,
            "bb": 0,
            "r": 0}
        self.field_stats = {"ch": 0,
            "po": 0,
            "ast": 0,
            "e": 0}
        self.pit_stats = {"bfp": 0,
            "outs": 0,
            "so": 0,
            "bb": 0,
            "r": 0}
