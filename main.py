#==========[Local Libraries]==========
#-----[Functionality]-----
import src.interp.neighborhood as nb
import src.interp.bilinear as bl
from src.helper.img import get_pixeis
from src.helper.matrix import print_matrix

#-----[Terminal Interface]-----
import src.cli.menu as menu

#==========[Main Function]==========
def main():
  img_original = menu.load()
  img_matrix = get_pixeis(img_original)

  while True:
    selection = menu.home()

    if selection == 0:
      break
    elif selection == 1:
      img_matrix = get_pixeis(img_original)
    elif selection == 2:
      print_matrix(img_matrix)
    elif selection == 3:
      img_matrix = nb.magnify(img_matrix)
    elif selection == 6:
      img_matrix = nb.reduce(img_matrix)
    elif selection == 4:
      img_matrix = bl.magnify(img_matrix)
    elif selection == 8:
      img_matrix = bl.reduce(img_matrix)
    elif selection == 5:
      menu.export(img_matrix)

#==========[Script Initializer]==========
if __name__ == "__main__":
  main()