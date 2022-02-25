def FindStart(adj_list):
    start = {}
    for one in adj_list:
        start.setdefault(one, 0)
        start[one] += len(adj_list[one])
    end = {}
    for one in adj_list:
        for two in adj_list[one]:
            end.setdefault(two, 0)
            end[two] += 1
    for one in end:
        try: 
            if start[one] != end[one]:
                if start[one] > end[one]:
                    start_node = one
                if start[one] < end[one]:
                    end_node = one
        except KeyError:
            end_node = one

    for one in start:
        try:
            if end[one] != start[one]:
                if end[one] < start[one]:
                    start_node = one
                if end[one] > start[one]:
                    end_node = one
        except KeyError:
            start_node = one
    return start_node, end_node

