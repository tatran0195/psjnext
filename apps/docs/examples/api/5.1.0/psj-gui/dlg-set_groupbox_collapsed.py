# Title:   dlg.set_groupbox_collapsed()
# Desc:    Set the initial state of the GroupBox's collapse to show/hide GroupBox's components
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_groupbox_collapsed
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set_groupbox_collapsed(name="GroupBox1",collapsed=True)  # [hl]
    dlg.set_groupbox_orientation(name="GroupBox1",orientation="horizontal")
    dlg.add_label(name="Label2",text="Label",layout="GroupBox1")
    dlg.add_textbox(name="TextBox3",layout="GroupBox1")
    dlg.add_label(name="Label4",text="Label",layout="GroupBox1")
    dlg.add_textbox(name="TextBox5",layout="GroupBox1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
