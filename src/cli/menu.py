import numpy
from ..helper.img import export_image, import_image

def home() -> int:
  print("┌───────────────────────────────────────────┐")
  print("│  Por favor, selecione uma opção abaixo:   │")
  print("├───────────────────────────────────────────┤")
  print("│ 1 - Recomeçar                             │")
  print("│ 2 - Exibir imagem atual                   │")
  print("│ 3 - Interpolação por vizinho mais próximo │")
  print("│ 4 - Interpolação bilinear                 │")
  print("│ 5 - Exportar resultado                    │")
  print("├───────────────────────────────────────────┤")
  print("│ 0 - Sair                                  │")
  print("└───────────────────────────────────────────┘")
  
  selection = 0
  try:
    selection = int(input('Seleção: '))
  except:
    pass

  if selection in [0, 1, 2, 5]:
    return selection

  print("┌───────────────────────────────────────────┐")
  print("│   Interpolação - Selecione um objetivo:   │")
  print("├───────────────────────────────────────────┤")
  print("│ 1 - Ampliar imagem                        │")
  print("│ 2 - Reduzir imagem                        │")
  print("├───────────────────────────────────────────┤")
  print("│ 0 - Sair                                  │")
  print("└───────────────────────────────────────────┘")

  interpolation = 0
  try:
    interpolation = int(input('Seleção: '))
  except:
    pass

  return selection * interpolation


def load() -> numpy.ndarray:
  print("┌───────────────────────────────────────────┐")
  print("│                Importação                 │")
  print("├───────────────────────────────────────────┤")
  print("│ Insira abaixo o endereço da imagem:       │")
  print("└───────────────────────────────────────────┘")
  path = input("Endereço: ")

  result = import_image(path)
  if result is None:
    ("┌───────────────────────────────────────────┐")
    print("│                 Fracasso                  │")
    print("├───────────────────────────────────────────┤")
    print("│ Não foi possível concluir a importação.   │")
    print("└───────────────────────────────────────────┘")
    return load()
  else:
    print("┌───────────────────────────────────────────┐")
    print("│                  Sucesso                  │")
    print("├───────────────────────────────────────────┤")
    print("│ Importação concluída com sucesso!         │")
    print("└───────────────────────────────────────────┘")
    return result


def export(img: list) -> None:
  print("┌───────────────────────────────────────────┐")
  print("│                Exportação                 │")
  print("├───────────────────────────────────────────┤")
  print("│ Insira abaixo o nome desejado:            │")
  print("└───────────────────────────────────────────┘")
  name = input("Nome do arquivo: ")

  if export_image(img, name):
    print("┌───────────────────────────────────────────┐")
    print("│                  Sucesso                  │")
    print("├───────────────────────────────────────────┤")
    print("│ Exportação concluída com sucesso!         │")
    print("└───────────────────────────────────────────┘")
  else:
    print("┌───────────────────────────────────────────┐")
    print("│                 Fracasso                  │")
    print("├───────────────────────────────────────────┤")
    print("│ Não foi possível concluir a exportação.   │")
    print("└───────────────────────────────────────────┘")
