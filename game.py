from half_inning import HalfInning
from player import Player
from team import Team

class Game:
    def play_ball(self):
        keep_playing = True
        half_inning_idx = 1
        tb = None
        ntb = None

        while(keep_playing):
            self.game_info["curr_tb"] = "Top" if half_inning_idx % 2 == 1 else "Bottom"
            tb = self.game_info["curr_tb"]
            self.game_info["curr_ntb"] = "Top" if self.game_info["curr_tb"] == "Bottom" else "Bottom"
            ntb = self.game_info["curr_ntb"]
            this_hinning = HalfInning(half_inning_idx, self.teams[tb], self.teams[ntb])

            while(this_hinning.outs < 3):
                this_hinning.plate_appearance()

            half_inning_idx += 1

            # game over if home team is beating away team after Top 9th
            if(half_inning_idx == 18 and self.teams[ntb].game_info.r > self.teams[tb].game_info.r):
                keep_playing = False
            # game over if score is different after Bottom 9th
            elif(half_inning_idx == 19 and self.teams[ntb].game_info.r != self.teams[tb].game_info.r):
                keep_playing = False
            # (temporary) game over after the 10th
            elif(half_inning_idx == 21):
                keep_playing = False
            elif input("Keep going? ").upper() == "N":
                keep_playing = False

    def __init__(self, p_Id):
        self.teams = {}

        self.game_info = {"game_id": p_Id,
            "curr_tb": "Top",
            "curr_ntb": "Bottom",
            "pit_slots": {"Top": 0, "Bottom": 0}}

        a_players = {}
        a_lineup = {}
        a_pitchers = []
        a_players[1] = Player(1, "Keith", "Hernandez", "1B", "STAR")
        a_players[3] = Player(3, "Ryne", "Sandberg", "2B", "STAR")
        a_players[9] = Player(9, "Wade", "Boggs", "3B", "STAR")
        a_players[10] = Player(10, "Ozzie", "Smith", "SS", "STAR")
        a_players[20] = Player(20, "Johnny", "Bench", "C", "STAR")
        a_players[25] = Player(25, "Ted", "Williams", "LF", "STAR")
        a_players[30] = Player(30, "Ty", "Cobb", "CF", "STAR")
        a_players[50] = Player(50, "Hank", "Aaron", " RF", "STAR")
        a_players[75] = Player(75, "Curt", "Schilling", "P", "VETERAN")

        a_lineup[1] = a_players[3]
        a_lineup[2] = a_players[10]
        a_lineup[3] = a_players[1]
        a_lineup[4] = a_players[50]
        a_lineup[5] = a_players[9]
        a_lineup[6] = a_players[25]
        a_lineup[7] = a_players[20]
        a_lineup[8] = a_players[30]
        a_lineup[9] = a_players[75]

        a_pitchers.append(a_players[75])

        h_players = {}
        h_lineup = {}
        h_pitchers = []
        h_players[2] = Player(2, "Gil", "Hodges", "1B", "ROOKIE")
        h_players[4] = Player(4, "Joe", "Morgan", "2B", "VETERAN")
        h_players[6] = Player(6, "Ron", "Santo", "3B", "STAR")
        h_players[15] = Player(15, "Alan", "Trammell", "SS", "VETERAN")
        h_players[28] = Player(28, "Ray", "Fosse", "C", "VETERAN")
        h_players[40] = Player(40, "Roberto", "Clemente", "LF", "VETERAN")
        h_players[41] = Player(41, "Willie", "Mays", "CF", "VETERAN")
        h_players[60] = Player(60, "Ken", "Griffey Jr", "RF", "VETERAN")
        h_players[70] = Player(70, "Greg", "Maddux", "P", "ACE")

        h_lineup[1] = h_players[2]
        h_lineup[2] = h_players[60]
        h_lineup[3] = h_players[41]
        h_lineup[4] = h_players[15]
        h_lineup[5] = h_players[40]
        h_lineup[6] = h_players[6]
        h_lineup[7] = h_players[4]
        h_lineup[8] = h_players[28]
        h_lineup[9] = h_players[70]

        h_pitchers.append(h_players[70])

        self.teams["Top"] = Team(101, "Austin", "Zeppelins", "AUS", False, a_players, a_lineup, a_pitchers)
        self.teams["Bottom"] = Team(102, "Chicago", "Aeronauts", "CHI", True, h_players, h_lineup, h_pitchers)
