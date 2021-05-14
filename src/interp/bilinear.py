from ..helper.array_operations import sum_lists, mean_list

def reduce(old_img: list) -> list:
  size_column = len(old_img[0])
  size_line = len(old_img)
  
  new_img = []
  new_line = []

  line = 0
  column = 0

  while(line < size_line):
    cont = 0

    sum_values = [0, 0, 0]

    sum_values = sum_lists(sum_values, old_img[line][column])
    cont += 1

    if column + 1 < size_column:
      sum_values = sum_lists(sum_values, old_img[line][column + 1])
      cont += 1

    if line + 1 < size_line:
      sum_values = sum_lists(sum_values, old_img[line + 1][column])
      cont += 1

    if line + 1 < size_line and column + 1 < size_column:
      sum_values = sum_lists(sum_values, old_img[line + 1][column + 1])
      cont += 1

    new_line.append(mean_list(sum_values, cont))
      
    column += 2
    
    if column >= size_column:
      new_img.append(new_line)
      new_line = []
      line += 2
      column = 0

  return new_img

def magnify(old_img: list) -> list:
  size_column = len(old_img[0])
  size_line = len(old_img)
  
  new_img = []
  current_new_line = []
  next_new_line = []

  line = 0
  column = 0
  
  for line in range (size_line):
    for column in range (size_column):
      current_new_line.append(old_img[line][column])

      if column + 1 < size_column:
        sum_values = sum_lists(old_img[line][column], old_img[line][column + 1])
        current_new_line.append(mean_list(sum_values, 2))
        
      if line + 1 < size_line:
        sum_values = sum_lists(old_img[line][column], old_img[line + 1][column])
        next_new_line.append(mean_list(sum_values, 2))
        
      if line + 1 < size_line and column + 1 < size_column:
        sum_values = sum_lists(old_img[line][column], old_img[line][column + 1])
        sum_values = sum_lists(sum_values, old_img[line + 1][column])
        sum_values = sum_lists(sum_values, old_img[line + 1][column + 1])
        next_new_line.append(mean_list(sum_values, 4))

    new_img.append(current_new_line)
    if next_new_line:
      new_img.append(next_new_line)

    current_new_line = []
    next_new_line = []

  return new_img