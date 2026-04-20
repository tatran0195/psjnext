# Title:   dlg.add_slider()
# Desc:    Add a SliderBar to the creating dialog
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_slider
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_slider(name="Slider21",width=100,height=100,min=0,max=100,pos=4,  # [hl:start]
      vertical=True,show_bothticks=True,layout="Window")  # [hl:end]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
