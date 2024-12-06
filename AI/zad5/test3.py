import random

# Przygotowanie wag jako macierzy 2D
w = [[0 for _ in range(7)] for _ in range(7)]

# Wzorce
p = [
    [
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, 1, -1, 1, -1, 1, 1],
        [1, 1, 1, -1, 1, 1, 1],
        [1, 1, -1, 1, -1, 1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
    ],
    [
        [1, -1, -1, -1, -1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, -1, 1],
        [1, -1, -1, -1, -1, -1, 1],
    ],
]

# Testowy wzorzec
test = [
    [1, -1, 1, 1, 1, -1, 1],
    [1, -1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, -1, 1, 1],
    [1, 1, 1, -1, 1, 1, 1],
    [1, 1, -1, 1, -1, 1, 1],
    [1, 1, 1, 1, 1, -1, 1],
    [1, -1, 1, 1, 1, -1, 1],
]


def calculate_weights():
    rows, cols = 7, 7
    # Obliczanie wag dla wzorców
    for i in range(rows):
        for j in range(cols):
            w[i][j] = 0  # Zerowanie wag
            for pattern in p:
                w[i][j] += pattern[i][j]  # Hebb rule
            w[i][j] /= len(p)  # Uśrednianie
    print("Macierz wag:")
    for row in w:
        print(row)


def output_function(net):
    if net > 0:
        return 1
    elif net == 0:
        return 0
    else:
        return -1


def learn():
    print("\nUczenie...")
    rows, cols = 7, 7
    for epoch in range(200):
        # Losowe kolejności neuronów
        random_positions = [(i, j) for i in range(rows) for j in range(cols)]
        random.shuffle(random_positions)

        stable = True  # Flaga stabilności sieci

        # Aktualizacja neuronów w losowej kolejności
        for i, j in random_positions:
            net_input = 0
            for k in range(rows):
                for l in range(cols):
                    if (i, j) != (k, l):  # Pomijanie samego neuronu
                        net_input += w[i][j] * test[k][l]
            new_state = output_function(net_input)
            if test[i][j] != new_state:
                stable = False
                test[i][j] = new_state

        # Wyświetlenie stanu sieci po epoce
        print(f"{epoch + 1} EPOKA")
        for row in test:
            print(row)
        print("\n")

        if stable:
            print("Sieć osiągnęła stan stabilny.")
            break


# Obliczenie wag i uruchomienie uczenia
calculate_weights()
learn()