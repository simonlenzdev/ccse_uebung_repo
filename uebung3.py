def max(**args):
    vals = list(args.values())
    vals.sort()
    return vals[-1]


print(max(first=3, second=17))
