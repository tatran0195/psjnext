# Title:   dlg.on_table_sel_changed()
# Desc:    Set event when selecting a cell
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-on_table_sel_changed
# ---
from pyjdg import *

def on_sel_change(dlg,name,cell):
    cellvector=dlg.get_table_sel_cell(name="Table1")
    if cellvector.size() > 0:
       print("Cell's position (row) = "+str(cellvector[0].row_number))
       print("Cell's position (column) = "+str(cellvector[0].col_number))
       print("---------------------------")

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
    dlg.add_table_right_menu(name="Table1",menus=["Check cell info"])
    dlg.generate_window()
    dlg.on_table_sel_changed(name="Table1",callfunc=on_sel_change)  # [hl]

if __name__=='__main__':
    main()
