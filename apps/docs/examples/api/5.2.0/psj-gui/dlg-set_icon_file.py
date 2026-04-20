# Title:   dlg.set_icon_file()
# Desc:    Set icon for the creating GUI
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_icon_file
# ---
from pyjdg import *

def main():
    sel_ico = JPT.GetProgramPath() + \
        r"Lib\site-packages\win32\test\win32rcparser\python.ico"

    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.set_icon_file(file=sel_ico)  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
