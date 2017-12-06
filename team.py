from player import Player

class Team:
    def __init__(self, p_Id, p_Location, p_Name, p_Abbr, p_Home, p_Players, p_Lineup, p_Pitchers):
        self.players = {}
        self.lineup = {}
        self.pitchers = p_Pitchers

        self.info = {"team_id": p_Id,
            "team_location": p_Location,
            "team_name": p_Name,
            "team_abbr": p_Abbr,
            "is_home": p_Home}

        self.game_info = {"r": 0,
            "h": 0,
            "e": 0}

        for k, v in p_Players.items():
            self.players[k] = v

        for k, v in p_Lineup.items():
            self.lineup[k] = v
            self.lineup[k].game_info.gs = 1
            self.lineup[k].game_info.gp = 1
