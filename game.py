from player import Player
from team import Team

class Game:
    def __init__(self, p_Id):
        self.teams = {}

        self.game_info = {"game_id": p_Id,
            "bat_slots": {"Top": 0, "Bottom": 0},
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

        self.teams["Top"] = Team(101, "Austin", "Zeppelins", "AUS", False, a_players)
        self.teams["Bottom"] = Team(102, "Chicago", "Aeronauts", "CHI", True, h_players)
