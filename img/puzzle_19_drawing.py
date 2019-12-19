from random import randint

from PIL import Image, ImageDraw

if __name__ == '__main__':
    img = Image.new('P', (1330, 1570))
    img.putpalette([0, 0, 0,
                    64, 80, 112,
                    128, 32, 64,
                    224, 224, 224])
    draw = ImageDraw.Draw(img)

    with open('puzzle_19_image_raw', 'rb') as f:
        img.frombytes(f.read())

    for __ in range(1000):
        draw.point((randint(1, 1330), randint(1, 1570)), fill=3)

    draw.rectangle((1220, 1460, 1220 + 99, 1460 + 99), fill=2)

    img.save('puzzle_19_image.png')
