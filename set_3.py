#232324 DUNGO, Marc Audryn A.
#ITMGT45 Assignment Set 3

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    from_following = social_graph.get(from_member, {}).get("following", [])
    to_following = social_graph.get(to_member, {}).get("following", [])

    from_follows_to = to_member in from_following
    to_follows_from = from_member in to_following

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    size = len(board)

    for row in board:
        if all(cell == row[0] and cell != '' for cell in row):
            return row[0]

    for col in range(size):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(size)):
            return board[0][col]

    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(size)):
        return board[0][0]

    if all(board[i][size - 1 - i] == board[0][size - 1] and board[i][size - 1 - i] != '' for i in range(size)):
        return board[0][size - 1]

    return "NO WINNER"



def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    current_stop = first_stop
    total_time = 0
    
    if first_stop == second_stop:
        return 0

    while current_stop != second_stop:
        found_next_stop = False
        for (start, end), details in route_map.items():
            if start == current_stop:
                total_time += details['travel_time_mins']
                current_stop = end
                found_next_stop = True
                break
        if not found_next_stop:
            return 0 # incase path is not found

    return total_time
