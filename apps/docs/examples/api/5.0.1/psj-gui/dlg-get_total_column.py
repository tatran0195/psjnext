# Title:   dlg.get_total_column()
# Desc:    Get the total number of columns of the Table
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-get_total_column
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=14,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    total_cols = dlg.get_total_column(name="Table1")  # [hl]
    JPT.Debugger(total_cols)

if __name__=='__main__':
    main()
