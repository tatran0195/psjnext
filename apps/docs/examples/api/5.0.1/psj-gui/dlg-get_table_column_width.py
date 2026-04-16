# Title:   dlg.get_table_column_width()
# Desc:    Get the width of the specified column in the Table
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-get_table_column_width
# ---
from pyjdg import *

def on_menu(dlg,name,menu):
    cellvector=dlg.get_table_sel_cell(name="Table1")
    if menu=="Set Column Width using Dialog":
        dlg.set_table_column_width(name="Table1",
            col=cellvector[0].col_number)
    if menu=="Set Column Width equal 400":
        dlg.set_table_column_width(name="Table1",
            col=cellvector[0].col_number,width=400)
    elif menu=="Get Column Width":
        col_width = dlg.get_table_column_width(name="Table1",  # [hl:start]
            col=cellvector[0].col_number)  # [hl:end]
        print("Column "+str(cellvector[0].col_number)+
            " width is: "+str(col_width))

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
        menus=["Set Column Width using Dialog",
        "Set Column Width equal 400","Get Column Width"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
