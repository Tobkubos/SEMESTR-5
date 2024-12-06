import random

def CalculateWeights(patterns):
    rows = len(patterns[0])
    cols = len(patterns[0][0])
    w = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(rows * cols)]

    for pattern in patterns:
        for i in range(rows):
            for j in range(cols):
                for k in range(rows):
                    for l in range(cols):
                        if not (i == k and j == l):  # Brak wag na przekątnej
                            w[i * cols + j][k][l] += pattern[i][j] * pattern[k][l]
    return w

def outputFunction(net):
    if net > 0:
        return 1
    elif net == 0:
        return 0
    else:
        return -1

def learn(w, test, max_epochs=200):
    rows = len(test)
    cols = len(test[0])

    for epoch in range(max_epochs):
        random_positions = [(i, j) for i in range(rows) for j in range(cols)]
        random.shuffle(random_positions)  # Losowa kolejność odwiedzania neuronów
        
        previous_test = [row[:] for row in test]  # Kopiujemy stan test
        
        for i, j in random_positions:
            input_sum = 0
            for k in range(rows):
                for l in range(cols):
                    if not (i == k and j == l):  # Nie uwzględniamy samych siebie
                        input_sum += w[i * cols + j][k][l] * test[k][l]
            test[i][j] = outputFunction(input_sum)  # Aktualizacja stanu

        # Wyświetlenie stanu sieci
        print(f"{epoch + 1} EPOKA")
        for row in test:
            print(row)
        print('\n')
        
        # Sprawdzenie stabilności
        if test == previous_test:
            print("Sieć osiągnęła stan stabilny.")
            break

# Przygotowanie wzorców i danych testowych
patterns = [
    [
    [1, 1, 1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, 1, 1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, 1, 1, -1, -1, -1, -1]
    ]
]

test = [
    [1, 1, 1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, -1],
    [1, 1, 1, -1, -1, -1, -1]
]

# Obliczenie wag i uruchomienie uczenia
w = CalculateWeights(patterns)
learn(w, test)