"""
Module for generating a random array using a subprocess.
"""

import subprocess


def random_array(arr):
    """
    Populates the given array with random integers between 1 and 20.

    Args:
        arr (list): A list of placeholders to be filled with random integers.

    Returns:
        list: The input array filled with random integers.
    """
    for i, _ in enumerate(arr):
        # Using subprocess to run the 'shuf' command and generate a random number
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
