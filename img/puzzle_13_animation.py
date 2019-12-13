from pathlib import Path

from PIL import Image, ImageDraw


def draw_wall(draw_obj, x, y):
    draw_obj.rectangle((10 * x, 10 * y, 10 * x + 9, 10 * y + 9), fill=3)


def draw_block(draw_obj, x, y):
    draw_obj.rectangle((10 * x, 10 * y, 10 * x + 8, 10 * y + 8), fill=4)


def draw_paddle(draw_obj, x, y):
    draw_obj.rectangle((10 * x, 10 * y + 1, 10 * x + 9, 10 * y + 5), fill=5)


def draw_ball(draw_obj, x, y):
    draw_obj.ellipse((10 * x + 3, 10 * y + 3, 10 * x + 7, 10 * y + 7), fill=2)


if __name__ == '__main__':
    draw_dispatch = {
        '*': draw_wall,
        '#': draw_block,
        '=': draw_paddle,
        'o': draw_ball,
    }

    frames = []

    for txt_path in Path('tmp/').glob('*.txt'):
        img = Image.new('P', (10 * 38, 10 * 22))
        img.putpalette([0, 0, 0,
                        255, 0, 0,
                        0, 255, 0,
                        96, 96, 96,
                        96, 0, 96,
                        0, 96, 96])
        draw = ImageDraw.Draw(img)

        with txt_path.open(encoding='utf-8') as f:
            for y, line in enumerate(f.read().splitlines()):
                if y == 0:
                    # write score
                    draw.text((330, 0), f'{int(line):8}', fill=1)
                    continue
                for x, char in enumerate(line):
                    draw_dispatch.get(char, lambda *args: None)(draw, x, y)

        frames.append(img)

    frames[0].save('puzzle_13.gif', format='GIF',
                   append_images=frames[1:], save_all=True,
                   duration=[2000] + [20]*len(frames[1:-1]) + [2000], loop=0)
