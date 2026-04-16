# Title:   dlg.add_table_sel_option()
# Desc:    Set combobox cell in the Table
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_table_sel_option
# ---
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_table(name="Table2",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="Window")
    dlg.generate_window()
    dlg.add_table_cell_option(name="Table2",cell=TableCellID(0,0),options=["0","2"],index=1)  # [hl:start]
    dlg.add_table_cell_option(name="Table2",row=0,col=1,options=["0","2"],index=1)  # [hl:end]
if __name__=='__main__':
    main()
