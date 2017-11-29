from player import Player
from team import Team

class Game:
    def reset_hinning_stats(self):
        self.hinning_stats["half_inning"] += 1
        self.hinning_stats["tb"] = "Top" if self.hinning_stats["half_inning"] % 2 == 1 else "Bottom"
        self.hinning_stats["ntb"] = "Top" if self.hinning_stats["tb"] == "Bottom" else "Bottom"
        self.hinning_stats["r"] = 0
        self.hinning_stats["h"] = 0
        self.hinning_stats["e"] = 0
        self.hinning_stats["run_1st"] = 0
        self.hinning_stats["run_2nd"] = 0
        self.hinning_stats["run_3rd"] = 0
        self.hinning_stats["base_situation"] = 0

    def __init__(self, p_Id):
        self.teams = {}

        self.game_info = {"game_id": p_Id,
            "bat_slots": {"Top": 0, "Bottom": 0},
            "pit_slots": {"Top": 0, "Bottom": 0}}

        self.hinning_stats = {"half_inning": 1,
            "tb": "Top",
            "ntb": "Bottom",
            "r": 0,
            "h": 0,
            "e": 0,
            "run_1st": 0,
            "run_2nd": 0,
            "run_3rd": 0,
            "base_situation": 0}

        a_players = {}
        a_players[1] = Player(1, "Willie", "Mays", "CF", "STAR")
        a_players[3] = Player(3, "Roberto", "Clemente", "CF", "STAR")
        a_players[9] = Player(9, "Brooks", "Robinson", "3B", "STAR")

        h_players = {}
        h_players[51] = Player(51, "Rickey", "Henderson", "CF", "ROOKIE")
        h_players[52] = Player(52, "Dave", "Henderson", "LF", "VETERAN")
        h_players[53] = Player(53, "Andre", "Dawson", "RF", "STAR")

        self.teams["Top"] = Team(101, "Austin", "Zeppelins", "AUS", False, a_players)
        self.teams["Bottom"] = Team(102, "Chicago", "Aeronauts", "CHI", True, h_players)
