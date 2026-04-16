# Title:   dlg.on_active_tab_page()
# Desc:    Bind a created function after a TabItem is selected
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-on_active_tab_page
# ---
from pyjdg import *

def captureTabWndPageChangeMessage(dlg,tabName,newTabPage):
    curPage=dlg.get_tabwnd_current_page(tabName)
    print("TabWnd:  "+ tabName +" changed page to "+ str(newTabPage))

def changeTabPage(dlg):
    dlg.set_tabwnd_current_page(name="TabWnd1",page_index=1)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
    dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem2",page_text="TabItem")
    dlg.add_combobox(name="ComboBox4",layout="TabItem2")
    dlg.add_combobox(name="ComboBox5",layout="TabItem2")
    dlg.add_button(name="Button6",text="Button",width=60,height=22,layout="TabItem2")
    dlg.add_button(name="Button7",text="Button",width=60,height=22,layout="TabItem2")
    dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem3",page_text="TabItem")
    dlg.add_checkbox(name="CheckBox8",text="CheckBox",layout="TabItem3")
    dlg.add_checkbox(name="CheckBox9",text="CheckBox",layout="TabItem3")
    dlg.add_button(name="Button10",text="Click Me to change TabPage",width=260,height=22,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_active_tab_page(name="TabWnd1",callfunc=captureTabWndPageChangeMessage)  # [hl]
    dlg.on_button_clicked(name="Button10",callfunc=changeTabPage)

if __name__=='__main__':
    main()
