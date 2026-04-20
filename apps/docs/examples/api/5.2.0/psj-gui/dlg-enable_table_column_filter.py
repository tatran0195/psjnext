# Title:   dlg.enable_table_column_filter()
# Desc:    Add filter option of column of Table
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-enable_table_column_filter
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table2",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.enable_table_column_filter(name="Table2",col=0,enable=True)  # [hl]
    dlg.generate_window()

if __name__=='__main__':
    main()
