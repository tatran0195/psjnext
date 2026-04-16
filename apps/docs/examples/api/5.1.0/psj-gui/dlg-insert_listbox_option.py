# Title:   dlg.insert_listbox_option()
# Desc:    Insert an option to a specific position of the inputted ListBox
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-insert_listbox_option
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
        width=100,height=150,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.insert_listbox_option(name="ListBox2",position=2,option="item_New")  # [hl]

if __name__=='__main__':
    main()
