# Title:   dlg.add_combobox_option()
# Desc:    Add an option to the ComboBox component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_combobox_option
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4"],layout="Layout1")
    dlg.add_combobox_option(name="ComboBox2",option_text="new_item")  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")

    dlg.generate_window()
if __name__=='__main__':
    main()
