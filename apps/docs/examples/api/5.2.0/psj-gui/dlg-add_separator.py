# Title:   dlg.add_separator()
# Desc:    Add a Separator to the creating dialog
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_separator
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout18",orientation=orientation.vertical,layout="Window")
    dlg.add_label(name="Label19",text="Label",text_valign="top",layout="Layout18")
    dlg.add_separator(name="Separator20",layout="Layout18")  # [hl]
    dlg.add_textbox(name="TextBox21",layout="Layout18")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
