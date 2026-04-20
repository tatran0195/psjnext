# Title:   dlg.add_space()
# Desc:    Add a space between the created components
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_space
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Field 1",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_space(orientation="vertical",size=2,layout="Window")  # [hl]
    dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label6",text="Field 2",layout="Layout5")
    dlg.add_textbox(name="TextBox7",layout="Layout5")
    dlg.add_layout(name="Layout8",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label9",text="Field 3",layout="Layout8")
    dlg.add_textbox(name="TextBox10",layout="Layout8")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")  # [hl]
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")  # [hl]
    dlg.generate_window()

if __name__=='__main__':
    main()
