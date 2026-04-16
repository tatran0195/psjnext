# Title:   dlg.add_listbox_option()
# Desc:    Add an option to the ListBox component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_listbox_option
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_listbox(name="ListBox3",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add_listbox_option(name="ListBox3",option_text="new_item")  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
