"""
Implements a method to generate an array.
"""
import random

def random_array(arr):
    """
    Generates a random array of integers from 1 to 20.

    Args:
        arr (list): The array to fill with random integers.

    Returns:
        list: The filled array with random integers.
    """
    for i,_ in enumerate(arr):
        try:
            arr[i] = random.randint(1, 20)
        except Exception as e:
            print(e)
            arr[i] = 0
    return arr
