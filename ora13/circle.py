import math
import easygui

try:
    diameter_str = easygui.enterbox("diameter:", title="adatbekeres")
    diameter = float(diameter_str)
    if diameter > 0:
        radius = diameter/2
        kerulet = 2*radius*math.pi
        terulet = radius**2*math.pi
        easygui.msgbox("a {} cm atmeroju kor {:.3f} cm keruletu és {:.3f} cm^2 teruletu".format(diameter, kerulet, terulet))
    else:
        easygui.msgbox("nem jo ertek", title="hiba")
except:
    easygui.msgbox("nem jo ertek", title="hiba")