def add_item(item, items=[]):
    items.append(item)
    return items


def get_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)


def fetch_user(user_id, users):
    try:
        return users[user_id]
    except:
        pass
