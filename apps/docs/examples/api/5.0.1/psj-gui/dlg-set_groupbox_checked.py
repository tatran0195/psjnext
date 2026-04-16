# Title:   dlg.set_groupbox_checked()
# Desc:    Set the initial state of the GroupBox's checkbox to show/hide. In case of showing, the initial state of the checkbox is checked
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_groupbox_checked
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set_groupbox_checked(name="GroupBox1",checked=True)  # [hl]
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
    dlg.add_label(name="Label3",text="Label",layout="Layout2")
    dlg.add_textbox(name="TextBox4",layout="Layout2")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
