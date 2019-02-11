import itertools


def _is_pre(s, ch, need_space):
    if not s.startswith(ch):
        return
    r = len(list(itertools.takewhile(lambda c: ch == c, s)))
    if not need_space:
        return r
    if r < len(s) and s[r].isspace():
        return r


def is_line_head(s):
    return _is_pre(s, '+', True)


def get_headers(filename, lines):
    '''
    Gets list of tuples in format:
    ((x1, y1, x2, y2), level, title, icon)
    '''
    res = []
    tick = False
    for i, s in enumerate(lines):
        if not s.strip():
            continue
        if s.lstrip().startswith('<<'):
            tick = True
            continue
        if s.lstrip().startswith('>>'):
            tick = False
            continue
        if tick:
            continue
        r = is_line_head(s)
        if r:
            res.append( ((0, i, 0, i+1), r, s[r:].strip(), -1) )
    return res
