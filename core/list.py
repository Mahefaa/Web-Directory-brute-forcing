
def split(lst, n):
    """Yield successive n-sized chunks from lst."""
    from more_itertools import divide
    for sub in divide(n, lst):
        yield list(sub)