# Title:   dlg.add_pagesctrl()
# Desc:    Add a PagesCtrl (wizard type) to the creating dialog
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_pagesctrl
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_pagesctrl(name="PagesCtrl4",current_page=2,width=300,height=300,text_align="right",layout="Window")  # [hl]
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="PageItem 1")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem6",page_header="PageItem 2")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem7",page_header="PageItem 3")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem8",page_header="PageItem 4")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
