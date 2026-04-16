# Title:   dlg.set_slider_vertical()
# Desc:    Show the SliderBar in the vertical or horizontal direction
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_slider_vertical
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_slider(name="Slider3",width=100,height=100,min=0,max=100,pos=0,layout="Layout1")
    dlg.set_slider_vertical(name="Slider3",enabled=True)  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
