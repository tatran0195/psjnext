# Title:   dlg.set_table_cell_button()
# Desc:    Set button cell in the Table
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_table_cell_button
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table2",width=260,height=260,
        columns=["Heading1","Heading2"],
        rows=5,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",
        layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_table_cell_button(name="Table2",row=0,  # [hl:start]
        col=0,text="Button")  # [hl:end]

if __name__=='__main__':
    main()
