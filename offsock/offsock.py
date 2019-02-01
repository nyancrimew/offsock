import click
from PIL import Image, ImageDraw

@click.command()
@click.option('--offset/--no-offset', '-o/-O', default=True, help='Wether or not the grid should be offset by one.')
@click.option('--rows', '-r', default=5, help='The height of the grid.')
@click.option('--columns', '-c', default=5, help='The width of the grid.')
@click.option('--padding', '-p', default=0, help='Additional padding to apply to the image.')
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def create(input, output, offset, rows, columns, padding):
    """
    Print an image a grid offset pattern. Inspired by your favorite socks.
    """
    in_image = Image.open(input)
    in_width = in_image.width
    in_height = in_image.height
    out_image = Image.new('RGBA', ((in_width + 2 * padding) * columns, (in_height + 2 * padding) * rows))
    d = ImageDraw.Draw(out_image)
    skip = False
    step = 2 if offset else 1
    for r in range(rows):
        start = 1 if skip and offset else 0
        skip = not skip
        for c in range(start, columns, step):
            out_image.paste(in_image, (c * in_width + padding, r * in_height + padding))
    out_image.save(output, optimize=True)

if __name__ == '__main__':
    create()