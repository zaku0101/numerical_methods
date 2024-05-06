import numpy as np


def simplex(A, b, c):
    m, n = A.shape
    # Stwórz tablicę zera o wymiarach (m+1) x (n+m+1)
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:m, :n] = A
    tableau[:m, -1] = b
    tableau[-1, :n] = c

    while min(tableau[-1, :-1]) < 0:
        pivot_col = np.where(tableau[-1, :-1] < 0)[0][0]
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        pivot_row = np.where(ratios == min(ratios))[0][0]

        # Wykonaj operacje pivot
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    # Sprawdź czy rozwiązanie jest nieograniczone
    if min(tableau[-1, :-1]) < 0:
        return None, None

    # Pobierz rozwiązanie i wartość funkcji celu
    solution = {f'x{i + 1}': 0 for i in range(n)}
    for i in range(m):
        if np.count_nonzero(tableau[i, :-1]) == 1 and tableau[i, -1] != 0:
            col = np.where(tableau[i, :-1] != 0)[0][0]
            solution[f'x{col + 1}'] = tableau[i, -1]
    objective_value = -tableau[-1, -1]

    return solution, objective_value