# Title:   dlg.add_table()
# Desc:    Add a Table to the creating dialog
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_table
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table2",rows=6,  # [hl:start]
        columns=["Heading1","Heading2","Heading3"],layout="Window",
        menus=["clear","cut","copy",
                "paste","insert row",
                "delete row","from file","to file"],
        width=200,height=200,
        show_grid_line=False,show_row_number=True,show_col_header=True)  # [hl:end]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
