#!/usr/bin/python3

def set2dict(s):
    return {x:1 for x in s}

def addTo(container, x):
    if type(container) is set:
        container.add(x)
    elif type(container) is dict:
        if x in container:
            container[x] = container[x]+1
        else:
            container[x] = 1
    else:
        raise RuntimeError

def getOptions(minVal, maxVal):
    optionSet = {x for x in range(minVal,maxVal+1)}
    return optionSet

def getSums(options, cells, total, allow_repeats = False):
    # edge cases
    if type(options) is not set:
        raise RuntimeError
    if cells < 1:
        return []
    if total < 1:
        return []
    if min(options) > total:
        return []
    if not allow_repeats:
        if len(options) < cells:
            return []
        if sum(options) < total:
            return []
        elif sum(options) == total:
            return [options]

    # actual work
    if cells == 1:
        if total in options:
            return [{total}]
        else:
            return []
    else:
        solutions = []
        for x in options:
            newOptions = options.copy()
            if not allow_repeats:
                newOptions.remove(x)

            newSolutions = getSums(newOptions, cells - 1, total - x)
            for s in newSolutions:
                if allow_repeats:
                    if type(s) is set:
                        s = set2dict(s)
                addTo(s,x)
                if s not in solutions:
                    solutions.append(s)
        return solutions

def sandwich_clue(cells, total):
    return getSums(getOptions(2,8),cells,total)

def killer_cage(cells, total):
    return getSums(getOptions(1,9),cells,total)

def killer_diag(cells, total):
    return getSums(getOptions(1,9),cells,total,True)

def sanity_check(solutions):
    totals = []
    for solution in solutions:
        if type(solution) is set:
            totals.append(sum(solution))
        elif type(solution) is dict:
            total = 0
            for k, v in solution.items():
                total += k*v
            totals.append(total)
    return totals


