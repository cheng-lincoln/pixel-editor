def clamp(n: float, smallest: float, largest: float):
    return max(smallest, min(n, largest))

def trpad(l: list, n: int, pad_element):
    return l[:n] + [pad_element]*(n-len(l))