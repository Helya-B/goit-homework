def is_valid_route(route: [str], time: int):
    if len(route) != time and len(route) // 2 != 0:
        return False

    way_for = route[:len(route) // 2]
    way_back = route[len(route) // 2:]
    way_back.reverse()

    i = len(way_for) - 1
    while i >= 0:
        if way_for[i] != way_back[i]:
            return False
        i -= 1

    return True


test_route = ['n', 's', 'w', 'e', 'n', 'n', 'e', 'w', 's', 'n']

print(is_valid_route(test_route, 10))
