# Title:   dlg.get_pagesctrl_page_name()
# Desc:    Get name of current selected PageItem of PagesCtrl
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-get_pagesctrl_page_name
# ---
from pyjdg import *

def on_pageitem_changed(dlg,name,oldpage):
    current_page=dlg.get_pagesctrl_current_page(name="PagesCtrl1")
    current_page_name=dlg.get_pagesctrl_page_name(name="PagesCtrl1",  # [hl:start]
        page_index=current_page)  # [hl:end]
    print("Selected page name:"+current_page_name)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_pagesctrl(name="PagesCtrl1",layout="Window")
    dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem2",
        page_header="PageItem1")
    dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem3",
        page_header="PageItem2")
    dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem4",
        page_header="PageItem3")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="Ok",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_pagesctrl_active_page(name="PagesCtrl1",callfunc=on_pageitem_changed)

if __name__=='__main__':
    main()
