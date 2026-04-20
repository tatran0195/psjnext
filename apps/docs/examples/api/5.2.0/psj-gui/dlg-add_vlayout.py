# Title:   dlg.add_vlayout()
# Desc:    Add a vertical Layout to the creating dialog
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_vlayout
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_vertex_selector()
    dlg.add_vlayout(name="footer",margin=[0,0,0,20],layout="Window")  # [hl]
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
