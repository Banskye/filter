from filters import *

filename = "panther.png"
filename2 = "panther_filtered.png"

original = load_img(filename)

newImg = viv(original)
save_img(newImg, filename2)
show_img(newImg)
