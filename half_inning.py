class HalfInning:
    def __init__(self, p_Index, p_BatTeam, p_PitTeam):
        self.half_inning_idx = p_Index
        self.tb = "Top" if self.half_inning_idx % 2 == 1 else "Bottom"
        self.ntb = "Top" if self.tb == "Bottom" else "Bottom"
        self.bat_team_id = p_BatTeam
        self.pit_team_id = p_PitTeam
        self.runs = 0
        self.hits = 0
        self.errors = 0
        self.id_1st = 0
        self.id_2nd = 0
        self.id_3rd = 0
        self.base_situation = 0
