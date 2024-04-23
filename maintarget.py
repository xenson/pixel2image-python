from tkinter.filedialog import askopenfilename
from PIL import Image
import numpy as np
import sys

NEW_IMG_HEIGHT = 70
NEW_IMG_NAME = "DiceImage.jpg"
TEXT_FILE_NAME = "DiceArrangement.txt"

dice = []
for x in range(0, 6):
    dice.append(Image.open(sys.path[0] + "/Images/dice" + str(x+1) + ".png").resize((32, 32)))


def convert_to_dice_image(filename):
    img = Image.open(filename)
    gray_image = img.convert('L')
    width, height = img.size
    relative_size = width / height
    small_img = gray_image.resize((int(NEW_IMG_HEIGHT * relative_size), NEW_IMG_HEIGHT))

    pixel_matrix = np.array(small_img)
    new_size = (int(NEW_IMG_HEIGHT * relative_size * 32) - 32, NEW_IMG_HEIGHT * 32)
    dice_img = Image.new('L', new_size, color='white')

    with open(TEXT_FILE_NAME, "w") as f:
        for row in range(0, NEW_IMG_HEIGHT):
            last_dice = 0
            dice_counter = 0
            line = ""
            for column in range(0, int(NEW_IMG_HEIGHT * relative_size)):
                grey_val = pixel_matrix[row][column]
                dice_number = assign_dice_to_color(grey_val)
                dice_img.paste(dice[dice_number], (column*32, row*32))

                current_dice = dice_number + 1
                if (current_dice != last_dice) and (dice_counter != 0):
                    line += f"d{last_dice} x {dice_counter}, "
                    dice_counter = 1
                else:
                    dice_counter += 1
                last_dice = current_dice
            line += f"d{last_dice} x {dice_counter}"
            f.write(line + "\n")

    dice_img.save(NEW_IMG_NAME, quality=100)
    print("Done!")
    print("In real life this image would measure:"
          f" {int((1.6*NEW_IMG_HEIGHT*relative_size))}cm x {int((1.6*NEW_IMG_HEIGHT))}cm.")


def assign_dice_to_color(grey_value):
    return 5-int(grey_value/45)




def pixToNum()
    # Open an image
    image = Image.open("your_generated_image.png")
    draw = ImageDraw.Draw(image)

    # Define font and text color
    font = ImageFont.truetype("arial.ttf", 20)
    text_color = (255, 255, 255)  # White color

    # Get image dimensions
    width, height = image.size

    # Define number of rows and columns
    rows = 5
    columns = 5

    # Add text labels for rows and columns
    for row in range(rows):
        draw.text((10, row * height // rows), f"Row {row+1}", fill=text_color, font=font)

    for col in range(columns):
        draw.text((col * width // columns, 10), f"Column {col+1}", fill=text_color, font=font)

    # Save or display the modified image
    image.save("labeled_image.png")
    image.show()

if __name__ == "__main__":
    image_name = askopenfilename()
    convert_to_dice_image(image_name)
