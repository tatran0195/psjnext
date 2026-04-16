# Title:   dlg.add_tabwnd_page()
# Desc:    Add a TabItem (page) to the TabWnd component
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_tabwnd_page
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
    dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem2",page_text="TabItem",page_orientation="horizontal")  # [hl]
    dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem3",page_text="TabItem")  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
