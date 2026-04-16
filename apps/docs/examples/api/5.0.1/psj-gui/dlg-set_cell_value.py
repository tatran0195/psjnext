# Title:   dlg.set_cell_value()
# Desc:    Set a value for a specific cell
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_cell_value
# ---
from pyjdg import *

def get_table_cell_value(dlg,name,cell):
    cellvector=dlg.get_table_sel_cell(name="Table1")
    if cellvector.size()>0:
        value_cell=dlg.get_cell_value(name="Table1",
            cell_row_id=cellvector[0].row_number,
            cell_column_id=cellvector[0].col_number)
        dlg.set_item_text(name="Textbox4",text=value_cell)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",
        orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label3",text="Get Value",layout="Layout1")
    dlg.add_textbox(name="Textbox4",layout="Layout1")
    dlg.add_table(name="Table1",rows=5,
        columns=["String","Integer","Double"],
        layout="Window",width=360,height=260)
    dlg.set_table_column_data_type(name="Table1",
        col=0,data_type="String")
    dlg.set_table_column_data_type(name="Table1",
        col=1,data_type="Integer")
    dlg.set_table_column_data_type(name="Table1",
        col=2,data_type="Double",precision=5)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")   
    dlg.generate_window()
    dlg.on_table_sel_changed(name="Table1",callfunc=get_table_cell_value)
    dlg.set_cell_value(name="Table1",  # [hl:start]
        cell_row_id=0,cell_column_id=0,value="Option1")
    dlg.set_cell_value(name="Table1",
        cell_row_id=1,cell_column_id=0,value=["Option2","Option3"])
    dlg.set_cell_value(name="Table1",
        cell_row_id=0,cell_column_id=1,value="1")
    dlg.set_cell_value(name="Table1",
        cell_row_id=1,cell_column_id=1,value=[2,3])
    dlg.set_cell_value(name="Table1",
        cell_row_id=0,cell_column_id=2,value="1.5")
    dlg.set_cell_value(name="Table1",
        cell_row_id=1,cell_column_id=2,value=[2.5,3.5])   # [hl:end]

if __name__=='__main__':
    main()
