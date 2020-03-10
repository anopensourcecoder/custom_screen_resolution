"""Console script for custom_screen_resolution."""
import sys
import click

from custom_screen_resolution.resolutions import  PPI, Scale, Height, Resolution

@click.command()
#@click.option('--name', default='FullHD 15.6', prompt='Display name', help='The display name ')
@click.option('--size', default='15.6', prompt='Display size', help='Display size in inch ')
@click.option('--ppi', default='141.2', prompt='Ppi or dpi', help='Sisplay ppi or dpi')
@click.option('--ratiox', default='16', prompt='Aspect ratio x', help='Display aspect ratio x')
@click.option('--ratioy', default='9', prompt='Aspect ratio y', help='Display aspect ratio y')


def main(size='15.6', ppi='141.2', ratiox='16', ratioy='9'):
    """Console script for custom_screen_resolution."""
    #click.echo("Replace this message by putting your code into "custom_screen_resolution.cli.main")
    #click.echo("See click documentation at https://click.palletsprojects.com/")
    demo = Resolution(size, ppi, ratiox, ratioy)
    result = "Width: " + str(demo.get_width_pixels()) + " Pixels\t Height: " + str(
        demo.get_height_pixels()) + " Pixels."
    click.echo('%s' % result)

if __name__ == "__main__":
    main()
    #sys.exit(main())  # pragma: no cover


#link https://click.palletsprojects.com/en/7.x/
