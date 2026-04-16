# Title:   dlg.add_node_selector()
# Desc:    Add "Node" to the selection list, allowing user to select nodes and store the selected nodes to the selection list
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_node_selector
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_listbox(name="ListBox3",multisel=True,options=["item1","item2","item3"],width=100,height=100,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_node_selector()  # [hl]
    dlg.generate_window()
    
if __name__=='__main__':
    main()
