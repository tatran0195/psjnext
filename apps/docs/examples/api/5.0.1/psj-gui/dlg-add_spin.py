# Title:   dlg.add_spin()
# Desc:    Add a Spin to the creating dialog
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_spin
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_spin(name="Spin2",min=1,max=100,pos=2,increment=2,layout="Window")  # [hl:start]
    dlg.add_spin(name="Spin3",type=spin.double,min=0.000000,max=50.000000,pos=1.500000,increment=1.500000,precision=3,layout="Window")  # [hl:end]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
