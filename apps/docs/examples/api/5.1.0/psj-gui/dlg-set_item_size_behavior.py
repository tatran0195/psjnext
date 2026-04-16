# Title:   dlg.set_item_size_behavior()
# Desc:    Set display behavior of TabWnd, ImageCtrl, Table, PagesCtrl
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_item_size_behavior
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add_tabwnd(name="TabWnd2",width=400,height=300,layout="Window")
    dlg.set_item_size_behavior(name="TabWnd2",behavior=size_behavior.greedy)  # [hl]
    dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem3",page_text="TabItem")
    dlg.add_label(name="Label4",text="Label",text_halign="left",text_valign="top",layout="TabItem3")
    dlg.add_textbox(name="TextBox5",layout="TabItem3")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
