"""Console script for custom_screen_resolution."""
import sys
import click

from custom_screen_resolution.custom_screen_resolution import  PPI, Scale, Height, Resolution,Screen_Info
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



@main.command("ppi")
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

@click.option("--port",
            type=str,
              default="HDMI1",
              help="Video Port Name such as HDMI1 or DP-1 or eDP and so on.")

@click.option("--rotate",
            type=str,
              default="normal",
              help="Screen rotation such as normal or right")

def screen_ppi(width, height, size, zoom,port, rotate, xrandr):
    """Calculate screen size base on screen size and dpi and zoom level.

    \b
    Example: custom-screen-resolution ppi 1920 1080 8 --zoom 2
    DPI:    137.68169813014364
    zoom:   2

    \b
    Example 2: custom-screen-resolution ppi 1920 1080 15.6
    DPI:    141.21

    \b
    Example 3: custom-screen-resolution ppi ppi 1080 8 --zoom 2  --xrandr --port eDP
    DPI:    137.68
    Effective Resolution:   960x540

    Step 1) Run the following to add the custom screen resolution
    xrandr --newmode "1920x1080_60.00" 173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
    xrandr --addmode eDP "1920x1080_60.00"

    Step 2) Run the following code to activate the new custom screen resolution
    xrandr --output eDP --mode "1920x1080_60.00" --scale 0.5x0.5 --filter nearest

    Note: Only latest xrandr from github support nearest filter option.

    """

    from custom_screen_resolution.custom_screen_resolution import PPI, Scale, Height, Resolution


    ppi = PPI(width, height, size, zoom)

    dpi_human = "%.2f" % ppi.get_ppi()

    effective_resolution = ppi.get_effective_resolution()

    click.echo("DPI:\t{}".format(dpi_human))
    click.echo("Effective Resolution:\t{}".format(effective_resolution))



    if xrandr==True:
        screen_info = Screen_Info(width, height, port, zoom,rotate)
        # w = screen_info.get_screen_width()
        # h = screen_info.get_screen_height()

        xrandr_new_mode = screen_info.get_xrandr_new_mode()
        xrandr_add_mode = screen_info.get_xrandr_add_mode()
        xrandr_activate_mode = screen_info.get_xrandr_activate_mode()

        click.echo()
        click.echo("Step 1) Run the following code to add the custom screen resolution to the system")
        click.echo(xrandr_new_mode)
        click.echo(xrandr_add_mode)

        click.echo()
        click.echo("Step 2) Run the following code to activate the new custom screen resolution")
        click.echo(xrandr_activate_mode)

        if zoom != 1:
            click.echo()
            click.echo("Note: Only latest xrandr from github support nearest filter option.")



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover


