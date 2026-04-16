# Title:   dlg.add_table_right_menu()
# Desc:    Add options to the context menu (Right click event) of Table
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_table_right_menu
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_table_right_menu(name="Table1",  # [hl:start]
        menus=["Set Cell Color",
            "Set Text Color",
            "Set Column Width",
            "Custom Menu"])  # [hl:end]
    dlg.generate_window()

if __name__=='__main__':
    main()
