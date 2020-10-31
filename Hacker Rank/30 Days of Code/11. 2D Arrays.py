def hourglass_pattern(array):
    WITHIN_RANGE = range(1, len(array) - 1)
    hourglass_sums = []
    for index in WITHIN_RANGE:
        for jndex in WITHIN_RANGE:
            TOP = array[index - 1][(jndex - 1):(jndex + 2)]
            MIDDLE = array[index][jndex]
            BOTTOM = array[index + 1][(jndex - 1):(jndex + 2)]
            hourglass_sums.append(sum([sum(TOP), MIDDLE, sum(BOTTOM)]))
    return max(hourglass_sums)
