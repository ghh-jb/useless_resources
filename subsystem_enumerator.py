def enumerate_subsystems(system:list) -> list:
    subsystems = []
    for i in range(len(system)):
        for j in range(i, len(system)):
            subsystem = []
            for r in range(i, j+1):
                # === debug ===
                # print(a[r], end = " ") 
                # =============
                subsystem.append(system[r])
            # === debug ===
            # if j != i:
            #     print()
            # =============
            if subsystem != []:
                    subsystems.append(subsystem)
    return subsystems
