from game import Game

if __name__ == "__main__":
    game_id = 1
    lpt_game = Game(game_id)
    lpt_game.play_ball()
    '''
    curr_tb = lpt_game.hinning_stats["tb"]
    curr_ntb = lpt_game.hinning_stats["ntb"]
    print(curr_tb)
    print(lpt_game.teams[curr_tb].info["team_abbr"])
    print(lpt_game.teams[curr_ntb].game_info["r"])
    print(lpt_game.teams[curr_tb].players[9].info["position"])
    print(lpt_game.teams[curr_ntb].players[53].field_stats["po"])
    '''
