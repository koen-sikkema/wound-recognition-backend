
results = {}

def store_result(filename: str, label: str, score: float):
    results[filename] = {
        "label": label,
        "score": score
    }

def get_result(filename: str):
    return results.get(filename)