import random
import numpy as np

# Wstępna definicja wag
def CalculateWeights(patterns):
    n = patterns[0].size
    w = np.zeros((n, n))
    for pattern in patterns:
        pattern_flat = pattern.flatten()
        w += np.outer(pattern_flat, pattern_flat)
    np.fill_diagonal(w, 0)  # Wyzeruj przekątną
    return w

def outputFunction(net):
    if net > 0:
        return 1
    elif net == 0:
        return 0
    else:
        return -1

def learn(w, test, max_epochs=200):
    n = test.size
    test_flat = test.flatten()
    for epoch in range(max_epochs):
        random_order = list(range(n))
        random.shuffle(random_order)
        
        previous_state = test_flat.copy()
        
        for idx in random_order:
            input_sum = np.dot(w[idx], test_flat)  # Oblicz sumę wag
            test_flat[idx] = outputFunction(input_sum)  # Zaktualizuj stan

        test = test_flat.reshape((7, 7))
        print(f"{epoch + 1} EPOKA")
        for row in test:
            print(row)
        print('\n')

        if np.array_equal(test_flat, previous_state):  # Jeśli sieć się ustabilizowała
            print("Sieć osiągnęła stan stabilny.")
            break

# Przygotowanie danych
patterns = [
    np.array([
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0]
    ])
]

test = np.array([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0]
])

w = CalculateWeights(patterns)
learn(w, test)