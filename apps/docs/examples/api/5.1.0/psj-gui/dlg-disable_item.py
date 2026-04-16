# Title:   dlg.disable_item()
# Desc:    Change the "Enable" option of an inputted component to off (Disabled)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-disable_item
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_label(name="Label1",text="Label",layout="Window")
    dlg.add_textbox(name="TextBox2",layout="Window")
    dlg.add_textbox(name="TextBox3",layout="Window")
    dlg.add_textbox(name="TextBox4",layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.disable_item(name="TextBox3")  # [hl]
    dlg.generate_window()
    
if __name__=='__main__':
    main()
