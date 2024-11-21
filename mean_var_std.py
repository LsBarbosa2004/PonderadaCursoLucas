import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("A lista tem que ter 9 numeros")
    
    matrix = np.array(input_list).reshape(3, 3)
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }
    
    return calculations

if __name__ == "__main__":
    user_input = input("Digite 9 numeros separados por espaços")
    input_list = [float(x) for x in user_input.split()]
    try:
        result = calculate(input_list)
        print(result)
    except ValueError as e:
        print(e)
