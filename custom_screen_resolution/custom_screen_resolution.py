import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from subprocess import call,check_output
#import screeninfo
#from screeninfo import get_monitors

class PPI():
    def __init__(self,x,y,size,scale=1):
        self.x=x
        self.y=y
        self.size=size
        self.scale=scale

    def get_ppi(self):
        dpx2 =  self.x**2  + self.y**2
        dpx =  math.sqrt(dpx2)
        ppi = (  dpx / self.size ) / self.scale
        return ppi

    def get_effective_resolution(self):
        dpx2 =  self.x**2  + self.y**2
        dpx =  math.sqrt(dpx2)
        resolution = (  str( int( self.x / self.scale) )  + "x" +  str( int( self.y / self.scale)) )
        return resolution

    def display(self):
        print( str(self.x)+"x"+ str(self.y)+"\t*"+str(self.size)+"\t/"+str(self.scale) + "\t%.2f" % self.get())

class Scale():
    def __init__(self,x,y,size,ppi):
        self.x=x
        self.y=y
        self.size=size
        self.ppi=ppi

    def get(self):
        dpx2 =  self.x**2  + self.y**2
        dpx =  math.sqrt(dpx2)
        scale = self.ppi /(  dpx / self.size )
        return scale

    def display(self):
        print( str(self.x)+"x"+ str(self.y)+"\t*"+str(self.size)+"\t/"+str(self.ppi) + "\t%.2f" % self.get())


class Height( ):
    def __init__(self, ratio_x, ratio_y, width_pixels ):
        self.ratio_x = ratio_x
        self.ratio_y= ratio_y
        self.ratio = self.ratio_x / self.ratio_y
        self.width_pixels = width_pixels
        self.get()
    def get(self):
        self.height_pixels = self.width_pixels / self.ratio
        self.height_pixels = self.width_pixels / self.ratio


    def display(self):
        #print( "width_inches", self.width_inches, "height_inches", self.height_inches )
        print( "width_pixels=",self.width_pixels, "height_pixels=",self.height_pixels )


class Resolution( ):
    def __init__(self,diagonal_size , ppi , ratio_x, ratio_y ):
        self.diagonal_size = float( diagonal_size)
        self.ppi = float(ppi)
        self.ratio_x = float(ratio_x)
        self.ratio_y= float(ratio_y)
        self.ratio = self.ratio_x / self.ratio_y
        self.width_pixels = 0
        self.height_pixels = 0
        self.get()


    def get(self):
        self.width_inches = self.ratio * math.sqrt( (self.diagonal_size**2) / (self.ratio**2 + 1) )
        self.height_inches = math.sqrt( (self.diagonal_size**2 ) / (self.ratio**2 + 1) )

        #Physical Size = Pixels / Density
        #Pixels = Physical Size / Density


        width_pixels = self.width_inches * self.ppi
        height_pixels = self.height_inches * self.ppi

        self.width_pixels = width_pixels + 8 - (width_pixels % 8)
        self.height_pixels = height_pixels + 8 - (height_pixels % 8)

    def get_width_pixels(self):
        return int(self.width_pixels)

    def get_height_pixels(self):
        return int(self.height_pixels)

    def get_ratio_x(self):
        return self.ratio_x

    def get_ratio_y(self):
        return self.ratio_y

    def get_ratio(self):
        return self.ratio

    def get_diagonal_size(self):
        return self.diagonal_size

    def display(self):
        print("\t%.2f" %self.diagonal_size  + "\t%.2f" % self.ppi
              + "\t%.0f" % self.width_pixels + "x%.0f" % self.height_pixels )


class Screen_Info():
    def  __init__(self,width,height,video_port="HDMI1",zoom=1,rotate="normal"):
        self.width = width
        self.height = height
        self.video_port = video_port
        self.zoom = zoom
        self.rotate = str( rotate)
        self.generate()

    def generate(self):

        #if self.monitors is not None:
        #    monitor=self.monitors[0]
        #    x = monitor.x
        #    x = monitor.x
        #    width = monitor.width
        #    height = monitor.height
        #    # width_mm = monitor.width_mm
        #    # height_mm = monitor.height_mm
        #    name = monitor.name

        #    print(name)
        #ROOT_DIR = os.path.dirname(__file__)

        cvt_output= check_output(["cvt", str( self.width), str(self.height) ])
        cvt_str = cvt_output.decode('UTF-8').splitlines()[1]
        cvt_split = cvt_str.split(" ", 2)
        # example ['Modeline', '"1928x1080_60.00"', ' 173.50  1928 2056 2256 2584  1080 1083 1093 1120 -hsync +vsync']
        self.Modeline = cvt_split[0]
        self.name = cvt_split[1]
        self.cvt = cvt_split[2]
        self.xrandr_new_mode = 'xrandr --newmode '+self.name  + self.cvt
        self.xrandr_add_mode = 'xrandr --addmode '+self.video_port+ ' ' +self.name

        self.xrandr_activate_mode = 'xrandr --output ' + str(self.video_port) + ' --mode ' + self.name + ' --rotate ' + self.rotate

        if self.zoom!=1:
            scale = round ( 1/self.zoom ,1)
            self.xrandr_activate_mode = self.xrandr_activate_mode + ' --scale '+str(scale)+'x'+str(scale)+' --filter nearest'


        #print( self.Modeline,self.name,self.cvt )
        #print( self.xrandr_new_mode )
        #print(self.xrandr_add_mode)
        #print(self.xrandr_activate_mode)

        return (self.xrandr_new_mode,)

    def get_xrandr_new_mode(self):
        return self.xrandr_new_mode

    def get_xrandr_add_mode(self):
        return self.xrandr_add_mode

    def get_xrandr_activate_mode(self):
        return self.xrandr_activate_mode
