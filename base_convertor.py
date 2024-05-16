def universal_wrapper(d:int, base:int = 2) -> str:
    numsandchars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    notchanged = d
    absolute = abs(d)
    run = []

    if absolute == 0:
        return '0'
    while absolute != 0:
        runner = absolute % base # 0 -> base - 1
        run.insert(0, str(numsandchars[runner]))
        absolute = absolute // base
    
    return ''.join(run) if notchanged >= 0 else "-" + ''.join(run)
