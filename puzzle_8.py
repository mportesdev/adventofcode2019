import io

from PIL import Image


def get_layers(image_data, width, height):
    stream = io.StringIO(image_data)

    while chunk := stream.read(width * height):
        yield chunk


def get_visible_pixel(sequence):
    for value in sequence:
        if value != '2':
            return int(value)
    return 2


if __name__ == '__main__':
    with open('puzzle_8_input') as f:
        image_data = f.read().strip()

    width = 25
    height = 6
    layers = get_layers(image_data, width, height)
    counts = ((layer.count('0'), layer.count('1'), layer.count('2'))
              for layer in layers)

    # Part 1
    least_zeros = min(counts)
    print(f'Solution: {least_zeros[1] * least_zeros[2]}')

    # the same generator once more
    layers = get_layers(image_data, width, height)
    pixels = bytes(get_visible_pixel(pixel_info) for pixel_info in zip(*layers))

    assert len(pixels) == width * height

    img = Image.new('P', (width, height))
    img.putpalette([0, 0, 0, 255, 255, 255, 128, 128, 128])
    img.frombytes(pixels)
    img = img.resize((8 * width, 8 * height))

    # Part 2
    img.show()
