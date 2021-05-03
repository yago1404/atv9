def main():
    CURRENT_FLOOR = 1
    DIRECTION = 1
    DESTINES = []
    OPEN_DOORS = False

    while True:
        print("\n############################################################\n")

        if OPEN_DOORS:
            print("##############\nportas abertas\n###############")
            OPEN_DOORS = False

        print('\nO elevador esta no {}º andar'.format(CURRENT_FLOOR))

        if len(DESTINES) > 0 and DESTINES[0] == CURRENT_FLOOR:
            print("\n##############\nportas abertas\n###############\n")
            DESTINES.pop(0)
            if len(DESTINES) > 0:
                if len(DESTINES) > 0:
                    if DESTINES[0] < CURRENT_FLOOR:
                        DIRECTION = -1
                    else:
                        DIRECTION = 1
        
        if len(DESTINES) > 0:
            print('\nProximo andar: {}'.format(DESTINES[0]))
        else:
            print('\nSem destinos no momento')

        new_destination = int(input('entre com o andar de destino ou 0 para pular\n==>'))

        if new_destination < 0:
            print("\n############\nAndar invalido\n###############\n")
            continue
        elif new_destination == CURRENT_FLOOR:
            OPEN_DOORS = True
            continue
        elif new_destination == 0:
            if len(DESTINES) == 0:
                print("\n############\nNenhum andar para ir, encerrando sistema\n###############\n")
                break
            else:
                if len(DESTINES) > 0:
                    if DESTINES[0] < CURRENT_FLOOR:
                        DIRECTION = -1
                    else:
                        DIRECTION = 1
                CURRENT_FLOOR += DIRECTION
                continue
        else:
            if DIRECTION == 1:
                if len(DESTINES) > 0 and new_destination > CURRENT_FLOOR and new_destination < DESTINES[0]:
                    DESTINES.insert(0, new_destination)
                else:
                    DESTINES.append(new_destination)
            else:
                if len(DESTINES) > 0 and new_destination < CURRENT_FLOOR and new_destination > DESTINES[0]:
                    DESTINES.insert(0, new_destination)
                else:
                    DESTINES.append(new_destination)

            if len(DESTINES) > 0:
                if DESTINES[0] < CURRENT_FLOOR:
                    DIRECTION = -1
                else:
                    DIRECTION = 1
            CURRENT_FLOOR += DIRECTION
            

        

        

if __name__ == '__main__':
    main()