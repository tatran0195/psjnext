# Title:   dlg.get_len_listbox()
# Desc:    Get the size (number of items) of the ListBox
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-get_len_listbox
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
    listBoxLen=dlg.get_len_listbox(name="ListBox2")  # [hl]
    print(listBoxLen)

if __name__=='__main__':
    main()
