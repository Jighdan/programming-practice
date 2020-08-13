"""
Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
"""

def who_likes_it(people):
    TEXT = "likes this" if len(people) < 2 else "like this"
    if len(people) == 0:
        return f"No one {TEXT}"
    elif len(people) == 2:
        return f"{people.join(" and ")} {TEXT}"
    elif len(people) == 3:
        return f"{people[0]}, {people[1]} and {people[2]} {TEXT}"
    else:
        return f"{people[0]}, {people[1]} and {len(people) - 2} {TEXT}"
