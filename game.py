from player import Player
from team import Team

class Game:
    def __init__(self, p_Id):
        self.game_info = {"game_id": p_Id}

        a_players = {}
        a_players[1] = Player(1, "Willie", "Mays", "CF", "STAR")
        a_players[3] = Player(3, "Roberto", "Clemente", "CF", "STAR")
        a_players[9] = Player(9, "Brooks", "Robinson", "3B", "STAR")

        h_players = {}
        h_players[51] = Player(51, "Rickey Henderson", "CF", "ROOKIE")
        h_players[52] = Player(52, "Dave Henderson", "LF", "VETERAN")
        h_players[53] = Player(53, "Andre Dawson", "RF", "STAR")

        self.teams["Top"] = Team(101, "Austin", "Zeppelins", "AUS", False, a_players)
        self.teams["Bottom"] = Team(102, "Chicago", "Aeronauts", "CHI", True, h_players)
