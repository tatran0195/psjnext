# Title:   dlg.set_table_cell_fill_color()
# Desc:    Set color to the selected/specified cells
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_table_cell_fill_color
# ---
from pyjdg import *

def on_menu(dlg,name,menu):
    cellvector=dlg.get_table_sel_cell(name="Table1")
    if menu=="Set Fill Color for all selected cells using color picker":
        dlg.set_table_cell_fill_color(name="Table1")  # [hl]
    elif menu=="Set Fill Color only for a selected cell using color picker":
         dlg.set_table_cell_fill_color(name="Table1",  # [hl:start]
            cell=cellvector[0])  # [hl:end]
    elif menu=="Set Fill Color only for a selected cell with red color":
        dlg.set_table_cell_fill_color(name="Table1",  # [hl:start]
            cell=cellvector[0],color=7105764)  # [hl:end]
    elif menu=="Set Fill Color only for the first cell with red color":
        dlg.set_table_cell_fill_color(name="Table1",  # [hl:start]
            cell=TableCellID(row=0,col=0),color=7105764)  # [hl:end]
    elif menu=="Set Fill Color only for the first 2x2 cells with red color":
        [[dlg.set_table_cell_fill_color(name="Table1",  # [hl:start]
            cell=TableCellID(row=i,col=j),color=7105764)
            for i in (0,1)] for j in (0,1)]  # [hl:end]

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
        menus=["Set Fill Color for all selected cells using color picker",
        "Set Fill Color only for a selected cell using color picker",
        "Set Fill Color only for a selected cell with red color",
        "Set Fill Color only for the first cell with red color",
        "Set Fill Color only for the first 2x2 cells with red color"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
