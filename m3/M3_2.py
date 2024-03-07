import random



def get_number_ticket(min, max, quantity):
    if quantity > max - min or min <= 0 or max > 1000:
        return []

    tickets = random.sample(range(min, max), quantity)
    return sorted(tickets)


print(get_number_ticket(1, 49, 6))



