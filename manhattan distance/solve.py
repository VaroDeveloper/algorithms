def solve(input_list):
    # Resuelve aqui este ejercicio
    x, y = 0, 0
    
    # Direcciones en orden: Norte, Este, Sur, Oeste
    addresses = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    adress_act = 0
    
    for instruction in input_list:
        turn = instruction[0]
        steps = int(instruction[1:])
        if turn == 'R':
            adress_act = (adress_act + 1) % 4
        elif turn == 'L':
            adress_act = (adress_act - 1) % 4

        dx, dy = addresses[adress_act]
        x += dx * steps
        y += dy * steps

    
    return abs(x) + abs(y)
