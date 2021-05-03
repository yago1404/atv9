
QUESTIONS = ['Seu dino é herbívoro?\n', 'Possui algum adorno na face?\n', 'É grande?\n']
FEATURES = {
    'herbivore': False,
    'adorne': False,
    'big': False,
}
DINOS = []
HERBIVORE = []
CARNIVORE = []
ADORNE = []
NOT_ADORNE = []
BIG = []
SMALL = []

def find_intersection():
    final_intersection = None
    if FEATURES['herbivore']:
        if FEATURES['adorne']:
            if FEATURES['big']:
                final_intersection = set(set(HERBIVORE).intersection(ADORNE)).intersection(BIG)
            else:
                final_intersection = set(set(HERBIVORE).intersection(ADORNE)).intersection(SMALL)
        else:
            if FEATURES['big']:
                final_intersection = set(set(HERBIVORE).intersection(NOT_ADORNE)).intersection(BIG)
            else:
                final_intersection = set(set(HERBIVORE).intersection(NOT_ADORNE)).intersection(SMALL)
    else:
        if FEATURES['adorne']:
            if FEATURES['big']:
                final_intersection = set(set(CARNIVORE).intersection(ADORNE)).intersection(BIG)
            else:
                final_intersection = set(set(CARNIVORE).intersection(ADORNE)).intersection(SMALL)
        else:
            if FEATURES['big']:
                final_intersection = set(set(CARNIVORE).intersection(NOT_ADORNE)).intersection(BIG)
            else:
                final_intersection = set(set(CARNIVORE).intersection(NOT_ADORNE)).intersection(SMALL)
        
    return final_intersection

def read_dbfile():
    f = open('db.txt', 'r')
    f_content = f.read().split()
    for i in f_content:
        DINOS.append(i)

def create_dino_groups():
    for i in DINOS:
        if i.find('herbivoro') != -1:
            HERBIVORE.append(i.split('-')[1])
        if i.find('carnivoro') != -1:
            CARNIVORE.append(i.split('-')[1])
        if i.find('grande') != -1:
            BIG.append(i.split('-')[1])
        if i.find('pequeno') != -1:
            SMALL.append(i.split('-')[1])
        if i.find('adorno') != -1 and i.find('semadorno') == -1:
            ADORNE.append(i.split('-')[1])
        if i.find('semadorno') != -1:
            NOT_ADORNE.append(i.split('-')[1])

def main():
    read_dbfile()
    create_dino_groups()
    print("\n\n------------ Sistema especialista Dinossauro ------------ \n\n")
    print("Responda com s(sim) ou n(não)\n\n")

    FEATURES['herbivore'] = True if input(QUESTIONS[0]) == 's' else False
    FEATURES['adorne'] = True if input(QUESTIONS[1]) == 's' else False
    FEATURES['big'] = True if input(QUESTIONS[2]) == 's' else False

    intersection = find_intersection()

    print("Seu dinossauro é o {}".format(list(intersection)[0]))

if __name__ == "__main__":
    main()