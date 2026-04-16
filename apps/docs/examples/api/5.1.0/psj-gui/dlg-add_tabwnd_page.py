# Title:   dlg.add_tabwnd_page()
# Desc:    Add a TabItem (page) to the TabWnd component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_tabwnd_page
# ---

from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_tabwnd(name="TabWnd2",width=200,height=200,layout="Window")  # [hl]
    dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem3",page_text="TabItem",page_orientation="vertical")
    dlg.add_label(name="Label5",text="Label",text_halign="left",text_valign="top",layout="TabItem3")
    dlg.add_textbox(name="TextBox6",layout="TabItem3")  # [hl]
    dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem4",page_text="TabItem",page_orientation="horizontal")
    dlg.add_label(name="Label7",text="Label",text_halign="left",text_valign="top",layout="TabItem4")
    dlg.add_textbox(name="TextBox8",layout="TabItem4")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
