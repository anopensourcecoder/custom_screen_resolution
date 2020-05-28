"""Console script for custom_screen_resolution."""
import sys
import click

from custom_screen_resolution.custom_screen_resolution import  PPI, Scale, Height, Resolution
@click.group()
@click.version_option()
#@click.command()
def main():
    """Welcome custom-screen-resolution console version.
    """
    #click.echo("Enjoy!")
    return 0


@main.command("side")
@click.argument("size", type=float)
@click.argument("dpi" ,type=float)
@click.argument("ratiox",type=float)
@click.argument("ratioy",type=float)
def screen_side(size, dpi, ratiox, ratioy):
    """Calculate Width and height base on screen size dpi and aspect ratio.

    \b
    Example: screen side 15.6 141.2 16 9
    Width: 1920
    Height: 1080
    """

    from custom_screen_resolution.custom_screen_resolution import PPI, Scale, Height, Resolution
    screen = Resolution(size, dpi, ratiox, ratioy)
    width = screen.get_width_pixels()
    click.echo("Width: \t{}".format(width))

    height =  screen.get_height_pixels()
    click.echo("Height:\t{}".format(height))


@main.command("size")
@click.argument("width", type=float)
@click.argument("height" ,type=float)
@click.argument("dpi",type=float)
def screen_dpi(width, height, dpi):
    """Calculate screen size base on resolution and dpi.

    \b
    Example: size 1920 1080 141.21
    Size:   15.6
    """

    from custom_screen_resolution.custom_screen_resolution import PPI, Scale, Height, Resolution
    size_float =  PPI(width,height,dpi).get()
    size_human= "%.1f" % size_float
    click.echo("Size:\t{}".format(size_human))



@main.command("dpi")
@click.argument("width", type=float)
@click.argument("height" ,type=float)
@click.argument("size",type=float)
@click.option("--zoom",
            type=float,
              default=1,
              help="Optional if you want to ser screen zoom level.")

@click.option(  "--xrandr",
                default=False,
                is_flag=True,
                help="Display xrandr command to generate the resolution.")

def screen_dpi(width, height, size, zoom,xrandr):
    """Calculate screen size base on screen size and dpi and zoom level.

    \b
    Example: dpi 1920 1080 8 --zoom 2
    DPI:    137.68169813014364
    zoom:   2

    \b
    Example 2: dpi 1920 1080 15.6
    DPI:    141.21
    """

    from custom_screen_resolution.custom_screen_resolution import PPI, Scale, Height, Resolution


    ppi = PPI(width, height, size, zoom)

    dpi_human = "%.2f" % ppi.get_ppi()

    effective_resolution = ppi.get_effective_resolution()

    click.echo("DPI:\t{}".format(dpi_human))
    click.echo("Effective Resolution:\t{}".format(effective_resolution))



    if xrandr==True:
        click.echo("xrandr section is under development")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover


