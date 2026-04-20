# Title:   dlg.add_pageitem()
# Desc:    Add a new PageItem to the created/selected PagesCtrl
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_pageitem
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_pagesctrl(name="PagesCtrl4",layout="Window")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="Page header 1")  # [hl]
    dlg.add_node_selector()
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
