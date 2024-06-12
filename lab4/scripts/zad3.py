import numpy as np

# Definicja macierzy A 
A = np.array([
    [1, 2, 2, 3, 1],
    [0, 4, 4, 6, 2],
    [3, 6, 6, 9, 6],
    [1, 2, 4, 5, 3]
])

# Funkcja do generowania rzadkich sygnałów z dyskretnym czasem
def generate_sparse_signals(num_signals, sample_count):
    signals = []
    for _ in range(num_signals):
        signal = np.zeros(sample_count)
        non_zero_indices = np.random.choice(sample_count, 3, replace=False)
        signal[non_zero_indices] = np.random.randint(-10, 11, 3)
        signals.append(signal)
    return np.array(signals)

# Projekcja sygnałów na podprzestrzeń kolumnową macierzy A
def project_signals(A, signals):
    return np.dot(A, signals.T)

# Estymacja sygnałów oryginalnych na podstawie sygnałów zmieszanych
def regularized_focuss(A, mixed_signals, regularization_lambda):
    I = np.eye(A.shape[1])
    regularization_term = regularization_lambda * I

    estimated_signals = np.linalg.lstsq(A, mixed_signals)[0]
    return estimated_signals

# Estymacja sygnałów oryginalnych z regulatorem M-FOCUSS
def regularized_m_focuss(A, mixed_signals, regularization_lambda):
    I = np.eye(A.shape[1])
    regularization_term = regularization_lambda * np.dot(mixed_signals, mixed_signals.T)

    inv_term = np.linalg.inv(np.dot(A, A.T) + regularization_term)
    pseudo_inverse_A = np.dot(A.T, inv_term)

    estimated_signals = np.dot(pseudo_inverse_A, mixed_signals)
    return estimated_signals

# Generowanie 5 rzadkich sygnałów
sparse_signals = generate_sparse_signals(5, A.shape[1])

# Projekcja sygnałów
projected_signals = project_signals(A, sparse_signals)

# Estymacja sygnałów z regulatorem FOCUSS (lambda = 0.1)
estimated_signals_focuss = regularized_focuss(A, projected_signals, 0.1)

# Estymacja sygnałów z regulatorem M-FOCUSS (lambda = 0.1)
estimated_signals_m_focuss = regularized_m_focuss(A, projected_signals, 0.1)

# Porównanie wyników
print("Oryginalne sygnały:")
print(sparse_signals)
print("\nSygnały zmieszane:")
print(projected_signals.T)
print("\nEstymacja sygnałów z regulatorem FOCUSS (lambda = 0.1):")
print(estimated_signals_focuss.T)
print("\nEstymacja sygnałów z regulatorem M-FOCUSS (lambda = 0.1):")
print(estimated_signals_m_focuss.T)