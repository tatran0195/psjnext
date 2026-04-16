# Title:   dlg.add_checkbox()
# Desc:    Add a CheckBox to the creating dialog
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_checkbox
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_checkbox(name="CheckBox2",text="CheckBox",lefttext=True,checked=True,layout="Window")  # [hl]
    dlg.add_checkbox(name="CheckBox3",text="CheckBox",lefttext=False,checked=True,layout="Window")  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
