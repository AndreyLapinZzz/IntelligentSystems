import numpy as np

def generate_calls(total_floors: int, n_calls: int):
    rows = n_calls
    cols = 2
    call_floors = list(range(1, total_floors))
    directions = [-1, 1]
    
    calls = np.empty((rows, cols))
    calls[:, 0] = np.random.choice(call_floors, size=rows)
    calls[:, 1] = np.random.choice(directions, size=rows)

    destination_floors = []
    
    for call_floor, direction in calls:
        if direction == 1:
            destination_floor = np.random.randint(call_floor + 1, total_floors + 2)
        else:
            destination_floor = np.random.randint(0, call_floor)
        
        destination_floors.append(destination_floor)
    
    calls = calls.astype(int)

    return calls.tolist(), destination_floors
