# Title:   dlg.enable_table_cell()
# Desc:    Set to enable/disable the cell in the table
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-enable_table_cell
# ---
from pyjdg import *

def on_menu(dlg,name,menu):
    table_cell = dlg.get_table_sel_cell(name)
    if menu == "Disable Cells":
        for cell in table_cell:
            dlg.enable_table_cell(name="Table1",cell=cell,enable=False)  # [hl]
    elif menu == "Enable Cells":
        for cell in table_cell:
            dlg.enable_table_cell(name="Table1",cell=cell,enable=True)  # [hl]

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
    dlg.add_table_right_menu(name="Table1",
        menus=["Disable Cells","Enable Cells"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
