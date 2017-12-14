import numpy as np

def create_data_sets(data, training, validation, test):
    if training + validation + test != 100:
        raise ValueError("The percentages must add to 100.")
    N = len(data)
    random_indices = np.random.permutation(N)
    random_values = data[random_indices]
    training_limit = (int)(round((training / 100) * N))
    validation_limit = (int)(round((validation / 100) * N))
    return random_values[:training_limit], random_values[training_limit : training_limit + validation_limit], random_values[training_limit + validation_limit :]


