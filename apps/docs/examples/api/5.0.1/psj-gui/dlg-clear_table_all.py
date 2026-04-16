# Title:   dlg.clear_table_all()
# Desc:    Clear all content of the Table
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-clear_table_all
# ---
from pyjdg import *

def on_click_clear_all(dlg):
    dlg.clear_table_all(name="Table1")  # [hl]

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=14,
        columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
        layout="Window",width=560,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="Clear",text="Clear Value",
        width=80,height=30,layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    for i in range(14):
        for j in range(5):
            dlg.set_cell_value(name="Table1",cell_row_id=i,
                cell_column_id=j,value=str(i+j))
    dlg.on_command(name="Clear",callfunc=on_click_clear_all)

if __name__=='__main__':
    main()
