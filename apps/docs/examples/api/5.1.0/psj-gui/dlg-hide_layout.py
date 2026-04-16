# Title:   dlg.hide_layout()
# Desc:    Hide the Layout and all of its children components inside
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-hide_layout
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Label",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_layout(name="Layout4",orientation=orientation.horizontal,layout="Window")
    dlg.add_richeditbox(name="RichEditBox8",text="RichEditBox",width=200,height=200,layout="Layout4")
    dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
    dlg.add_textbox(name="TextBox7",layout="Layout5")
    dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add_combobox(name="ComboBox9",layout="Layout6")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.hide_layout(name="Layout5")  # [hl]

if __name__=='__main__':
    main()
