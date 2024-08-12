from math import inf

def divide(first, second):
    
    if second == 0:
        div_ = inf
    else:
        div_ = first / second

    return div_


if __name__ == '__main__':
    print(divide(77,7))
