# Title:   dlg.is_table_cell_checked()
# Desc:    Check the state of checkbox cell
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-is_table_cell_checked
# ---
from pyjdg import *

def on_cell_button_clicked(dlg,name,cell):
    JPT.ClearLog()
    cellvector=dlg.get_table_sel_cell(name="Table2")
    if cellvector.size() > 0:
       check_cell_checkbox = \
            dlg.is_table_cell_checkbox(name="Table2",
                cell=cellvector[0])
       check_state_checkbox = \  # [hl:start]
            dlg.is_table_cell_checked(name="Table2",
                cell=cellvector[0])  # [hl:end]
       print("Is checkbox cell: " + str(check_cell_checkbox))
       print("State of checkbox cell: " + \
           str(check_state_checkbox))

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
    dlg.set_table_cell_checkbox(name="Table2",row=0,
        col=0,text="Checkbox",checked=True)
    dlg.on_table_sel_changed(name="Table2",
        callfunc=on_cell_button_clicked)

if __name__=='__main__':
    main()
