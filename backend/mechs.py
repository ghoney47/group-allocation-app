import graphlib
# TODO DA for 1:1



# TODO: how are we going to store users and their prefernces? hash map, rethink outputs


# calculating group preference per user
# user_prefs[i] => user i's preference list
# user_prefs[i][i] => user i's ith preference tuple of (user, value)
# curr_groups => curr_groups[i] = list of members in that group
# outputs an array of tuples st res[i] = (group, value)
def calc_user_group_prefs (user_prefs: dict, curr_groups: list[list[int]]) -> list[tuple[int, int]]:



# TODO: TTC first round only (so we only run their top preference)
# user_prefs[i] => user i's preference list
# user_prefs[i][i] => user i's ith preference tuple of (group, value)
# b: budget (maybe set as constant)
# ouput tuples of matches
def ttc(user_group_prefs: dict, group_prefs: dict)-> list[tuple[int, int]]:
    res = []  # to store tuple (user, group number)

    #build edges
    edges = []


    # think- how do we update the preferences as we go?
    # maybe some flag- or we just hold dictionary of marked users (or we just remove those matched from the user prefs)


    # building user -> group
    for i in range(0, len(user_prefs)):
        edges.append((i, user_prefs[i][0]))



    # build graph


# TODO: Borda Count (with budget)
def borda_count(user_prefs: list[list[tuple[int, int]]], b: int):
