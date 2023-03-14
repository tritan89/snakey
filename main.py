# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

#import random
import typing



# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "tritan89",  # TODO: Your Battlesnake Username
        "color": "#420969",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")

def relative_distance(coord1, coord2):
  return abs(coord1['x'] - coord2['x']) + abs(coord1['y'] - coord2['y'])
  
#calculates the relative distance of all food on board and returns the closest food
def get_closest_food(head, foods):
  min_food = foods[0]
  relative_min = relative_distance(head, foods[0])
  cur_relative = 0
  
  for food in foods:
    cur_relative = relative_distance(head, food)
    if cur_relative < relative_min:
      relative_min = cur_relative
      min_food = food
  return min_food
  
# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"

    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        is_move_safe["up"] = False

    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    # board_width = game_state['board']['width']
    # board_height = game_state['board']['height']
    if my_head["x"] == 10:
        
        is_move_safe["right"] = False

    if my_head["x"] == 0:
       
        is_move_safe["left"] = False

    if my_head["y"] == 0:
        
        is_move_safe["down"] = False

    if my_head["y"] == 10:
       
        is_move_safe["up"] = False

    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    # my_body = game_state['you']['body']
    my_body = game_state['you']['body']
    for coord in my_body:

        # if body is left
        if my_head["y"] == coord["y"] and my_head['x']-1 == coord['x']:
            is_move_safe["left"] = False

        # if body is right
        if my_head['y'] == coord['y'] and my_head['x']+1 == coord['x']:
            is_move_safe['right'] = False

        # if body is down
        if my_head['x'] == coord['x'] and my_head['y']-1 == coord['y']:
            is_move_safe['down'] = False

        # if body is up
        if my_head['x'] == coord['x'] and my_head['y']+1 == coord['y']:
            is_move_safe['up'] = False

    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    opponents = game_state['board']['snakes']
    for opp in opponents:
        opp_body = opp["body"]
        for seg in opp_body:
            if my_head["y"] == seg["y"] and my_head['x'] - 1 == seg['x']:
                is_move_safe["left"] = False

            # if body is right
            if my_head['y'] == seg['y'] and my_head['x'] + 1 == seg['x']:
                is_move_safe['right'] = False

            # if body is down
            if my_head['x'] == seg['x'] and my_head['y'] - 1 == seg['y']:
                is_move_safe['down'] = False

            # if body is up
            if my_head['x'] == seg['x'] and my_head['y'] + 1 == seg['y']:
                is_move_safe['up'] = False

              
    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

   

    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    food = game_state['board']['food']
    closest_food = get_closest_food(my_head, food)      

    best_moves = []
    
    if my_head['x'] < closest_food['x']:
      best_moves.insert(0, 'right')
      
    else:
      best_moves.append('right')
      
    if my_head['x'] > closest_food['x']:
      best_moves.insert(0, 'left')
    else:
      best_moves.append('left')
    
    if my_head['y'] < closest_food['y']:
        best_moves.insert(0, 'up')
    else:
        best_moves.append('up')

    if my_head['y'] > closest_food['y']:
      best_moves.insert(0, 'down')
    else:
      best_moves.append('down')


    for move in best_moves:
      if move in safe_moves:
        next_move = move
        break
  

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


def closest_enemy(head, my_len, enemies):
  cur_relative = 0
  elist = []
  for enemy in enemies:
    e_len = enemy["length"]
    cur_relative = relative_distance(head, enemy["head"])
    if cur_relative <= 2:
      if e_len >= my_len:
        elist.append(enemy)
  return elist
    
    

  
  
  
  
# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})

