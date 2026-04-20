# Title:   dlg.enable_tabwnd_swap_tab()
# Desc:    Set to enable/disable swap the tab items in a tabwnd
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-enable_tabwnd_swap_tab
# ---
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_tabwnd(name="TabWnd10",width=200,height=200,layout="Window")
    dlg.enable_tabwnd_swap_tab(name="TabWnd10", enable=False)  # [hl]
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem11",page_text="TabItem1")
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem12",page_text="TabItem2")
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem13",page_text="TabItem3")
    dlg.generate_window()
if __name__=='__main__':
    main()
