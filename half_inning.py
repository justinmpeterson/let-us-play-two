from player import Player
from team import Team

class HalfInning:
    def plate_appearance(self):
        self.bat_team.game_info["curr_slot"] = 1 if self.bat_team.game_info["curr_slot"] == 9 else self.bat_team.game_info["curr_slot"] + 1
        slot = self.bat_team.game_info["curr_slot"]
        batter = self.bat_team.lineup[slot]
        pitcher = self.pit_team.pitchers[len(self.pit_team.pitchers) - 1]

        print("{} facing {}.".format(batter.info["last_name"], pitcher.info["last_name"]))

        self.outs += 1

    def __init__(self, p_Index, p_BatTeam, p_PitTeam):
        self.half_inning_idx = p_Index
        self.tb = "Top" if self.half_inning_idx % 2 == 1 else "Bottom"
        self.ntb = "Top" if self.tb == "Bottom" else "Bottom"
        self.bat_team = p_BatTeam
        self.pit_team = p_PitTeam
        self.outs = 0
        self.runs = 0
        self.hits = 0
        self.errors = 0
        self.id_1st = 0
        self.id_2nd = 0
        self.id_3rd = 0
        self.base_situation = 0
