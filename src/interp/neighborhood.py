from copy import deepcopy

def reduce(matrix: list) -> list:
  len_x, len_y = len(matrix[0]), len(matrix)

  new_matrix = list()

  for y in range(len_y):
    if y % 2 != 0:
      continue
    new_line = []
    for x in range(len_x):
      if x % 2 != 0:
        continue
      new_line.append(matrix[y][x])
    new_matrix.append(new_line)

  return new_matrix

def magnify(matrix: list) -> list:
  len_x, len_y = len(matrix[0]), len(matrix)

  new_matrix = list()

  for y in range(len_y):
    new_line = []
    for x in range(len_x):
      new_line.append(matrix[y][x])
      new_line.append(matrix[y][x])
    new_matrix.append(new_line)
    new_matrix.append(deepcopy(new_line))

  return new_matrix