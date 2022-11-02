# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%201&url=worlds%2Ftutorial_en%2Fhome1.json
# This was an interesting set of games that worked on the understanding of If/Else and While statements to perform a series of moves.
# I made a challenge to myself to only call the minimum number of commandes to execute the level.
# To speed up the process place "think(0)" just before the first executable command.

# HOME world 1-4
# This code is built to properly function in any of the 4 levels.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_home():
    if at_goal():
        done()
    elif front_is_clear():
        move()
        go_home()
    elif wall_in_front():
        if right_is_clear():
            turn_right()
            go_home()
        else:
            turn_left()
            go_home()
    else:
        go_home()

go_home()

# AROUND world 1, 1-variable, 2, 3, and 4. 1-apple had to be built separate as it had a different requirement

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def movement():
    if object_here():
        done()
    elif right_is_clear():
        turn_right()
        move()
        movement()
    elif front_is_clear():
        move()
        movement()
    elif wall_in_front():
        turn_left()
        movement()
def start():
    put()
    if wall_in_front():
        turn_left()
        start()
    else:
        move()
        movement()
start()

# AROUND world 1-apple

def apple_picker():
    if at_goal():
        done()
    elif object_here():
        take()
        apple_picker()
    elif front_is_clear():
        move()
        apple_picker()
    elif wall_in_front():
        turn_left()
        apple_picker()
        
move()
apple_picker()

# Center 1 and 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def center_finder():
    if front_is_clear():
        move()
        center_finder()
    elif wall_in_front():
        turn_left()
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            turn_left()
            build_wall()
            turn_left()
            turn_left()
            center_finder()
        else:
            find_north()

def find_north():
    if not is_facing_north():
        turn_left()
        find_north()
    else:
        center_finder_horizontal()
    
def center_finder_horizontal():
    if front_is_clear():
        move()
        turn_left()
        build_wall()
        turn_around()
        build_wall()
        turn_left()
        center_finder_horizontal()
    else:
        turn_left()
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            turn_left()
            build_wall()
            turn_left()
            turn_left()
            horizontal_wall_builder()
        else:
            put()
            done()
def horizontal_wall_builder():
    if front_is_clear():
        move()
        horizontal_wall_builder()
    else:
        turn_left()
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            turn_left()
            build_wall()
            turn_left()
            turn_left()
            center_finder()
        else:
            put()
            done()
def turn_around():
    turn_left()
    turn_left()
    
center_finder()

# Harvest 1 and 2

def harvest():
    if object_here("carrot"):
        take()
        harvest()
    elif front_is_clear():
        move()
        harvest()
    elif wall_in_front():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            start_of_line()
        else:
            done()
def start_of_line():
    if front_is_clear():
        move()
        start_of_line()
    else:
        turn_left()
        turn_left()
        harvest()
        
harvest()

# Harvest 3 required the command to plant new seeds and cannot function with the first two levels.

def harvest_check():
    if object_here():
        harvest_time()
    else:
        move()
        if object_here():
            return_to_start_row()
        else:
            move()
            if object_here():
                return_to_start_row()
            else:
                move()
                if object_here():
                    return_to_start_row()
                else: 
                    move()
                    if object_here():
                        return_to_start_row()
                    else:
                        move()
                        if object_here():
                            return_to_start_row()
                        else:
                            done()

def return_to_start_row():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    move()
    move()
    harvest_time()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def starting_position():
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    harvest_check()

def harvest_time():
    if object_here():
        take()
        harvest_time()
    else:
        put()
        move()
        move()
        if front_is_clear():
            turn_left()
            turn_left()
            move()
            turn_left()
            turn_left()
            harvest_time()
        else:
            harvest_reset()
        
def harvest_reset():
    if wall_in_front():
        while not is_facing_north():
            turn_left()
        move()
        if wall_on_right():
            turn_left()
            move()
            move()
            harvest_check()
        else:
            turn_right()
            move()
            move()
            harvest_check()
        
starting_position()

# Hurdle level 1 through 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def not_clear():
    turn_left()
    start()

def clear_right():
    turn_right()
    move()
    turn_right()
    move()
    start()
    
def start():
    while not at_goal():
        if right_is_clear():
            clear_right()
        elif front_is_clear():
            move()
            start()
        else:
            not_clear()
start()

# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def maze_runner():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
            maze_runner()
        elif front_is_clear():
            move()
            maze_runner()
        elif wall_in_front():
            turn_left()
            maze_runner()
    while at_goal():
        done()
maze_runner()

# Newspaper world 1
# Can only solve Newspaper 1 since Newspaper 0 only has a basic move here drop return without the ability to automate

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def paper_boy_drop():
    while object_here("token"):
        take()
    put("star")
    turn_left()
    turn_left()
    paper_boy_return_move()
    
def paper_boy_start():
    if object_here("star"):
        take()
        paper_boy_client_move()
    else:
        paper_boy_client_move()
        
def paper_boy_client_move():
    if object_here("token"):
        paper_boy_drop()
    elif front_is_clear():
        move()
        paper_boy_client_move()
    else:
        turn_left()
        move()
        turn_right()
        paper_boy_client_move()
        
def paper_boy_return_move():
    if front_is_clear():
        move()
        paper_boy_return_move()
    else:
        turn_left()
        if front_is_clear():
            move()
            turn_right()
            paper_boy_return_move()
        else:
            done()
            
paper_boy_start()

# Rain worlds 0 through 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def clear_right():
    if wall_on_right() and front_is_clear():
        move()
        clear_right()
    else:
        turn_left()
        window_install()
        
def window_install():
    if at_goal():
        done()
    elif right_is_clear():
        move()
        if right_is_clear():
            turn_left()
            turn_left()
            move()
            turn_left()
            move()
            window_install()
        else:      
            turn_right()
            turn_right()
            move()
            turn_left()
            build_wall()
            turn_left()
            move()
            window_install()
    elif front_is_clear():
        move()
        window_install()
    elif wall_in_front():
        turn_left()
        window_install()
            
def starter():
    if at_goal():
        start()
    else:
        move()
        starter()
        
def start():
    if right_is_clear():
        turn_right()
        move()
        clear_right()
    else:
        window_install()
        
starter()

# Storm 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def return_home():
    while not at_goal():
        if right_is_clear():
            turn_right()
            while front_is_clear():
                move()
            return_home()
        elif front_is_clear():
            move()
            return_home()
        elif wall_in_front():
            turn_left()
            return_home()
    while at_goal():
        if not is_facing_north():
            turn_right()
            return_home()
        elif carries_object():
            toss()
            return_home()
        else:
            done()
def second_sweep():
    turn_left()
    turn_left()
    leaf_cleaner2()
    
def leaf_cleaner2():
    if object_here("leaf"):
        take()
        leaf_cleaner2()
    elif front_is_clear():
        move()
        leaf_cleaner2()
    elif not front_is_clear():
        turn_right()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            leaf_cleaner2()
        else:
            return_home()
    else:
        return_home()
    
def new_line():
    if not is_facing_north():
        turn_left()
        new_line()
    elif front_is_clear():
        move()
        turn_left()
        while front_is_clear():
            move()
        turn_left()
        turn_left()
        leaf_cleaner()
    else:
        second_sweep()
        
def leaf_cleaner():
    if object_here("leaf"):
        take()
        leaf_cleaner()
    elif front_is_clear():
        move()
        leaf_cleaner()
    elif wall_in_front():
        new_line()

leaf_cleaner()

# Tokens

def token_game():
    move()
    if object_here():
        take()
        token_game()
    elif at_goal():
        done()
    elif carries_object():
        while carries_object():
            put()
            if not carries_object():
                token_game()
    else:
        token_game()
        
def start_check():
    if object_here():
        take()
        token_game()
    else:
        token_game()
        
start_check()