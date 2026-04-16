# Title:   dlg.set_listbox_sel()
# Desc:    Set current selection to the ListBox component
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_listbox_sel
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
    dlg.set_listbox_sel(name="ListBox2",option=3)  # [hl]

if __name__=='__main__':
    main()
