def rotation_arr(numbers,direction):
    return numbers[-1:]+numbers[:-1] if direction == "right" else numbers[1:]+numbers[0:1]
