def diff(current, target):
    additions = [x for x in target if x not in current]
    subtractions = [x for x in current if x not in target]

    return sorted(additions), sorted(subtractions)
