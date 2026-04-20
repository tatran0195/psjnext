# Title:   dlg.set_table_column_data_type()
# Desc:    Set data type validation of cell of Table
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_table_column_data_type
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["String","Integer","Double"],
        layout="Window",width=260,height=260)    
    dlg.set_table_column_data_type(name="Table1",  # [hl:start]
        col=0,data_type="String")
    dlg.set_table_column_data_type(name="Table1",
        col=1,data_type="Integer")
    dlg.set_table_column_data_type(name="Table1",
        col=2,data_type="Double",precision=5)  # [hl:end]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="Ok",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
