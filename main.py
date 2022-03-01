no_of_ways_missed_grad = 0


def num_ways(length,
             miss_left,
             days_miss_allowed,
             path):
    global no_of_ways_missed_grad

    if length == 0:
        if path[-1] == 0:
            no_of_ways_missed_grad += 1
        return 1

    if miss_left > 0:
        # day by day
        # either miss or not
        # miss depends on the number of miss left (at max 4)
        miss_path = num_ways(length - 1, miss_left - 1, days_miss_allowed, path + [0])
    else:
        miss_path = 0

    # reset miss left when combinations are over
    no_miss_path = num_ways(length - 1, days_miss_allowed, days_miss_allowed, path + [1])

    print(f'{length = } {miss_left = } {miss_path = } {no_miss_path = }')

    return miss_path + no_miss_path


if __name__ == "__main__":
    n = 5
    consecutive_days_miss_le = 4
    no_of_ways_missed_grad = 0

    total = num_ways(n,
                     consecutive_days_miss_le - 1,
                     consecutive_days_miss_le - 1,
                     [])

    print(no_of_ways_missed_grad, "/", total)