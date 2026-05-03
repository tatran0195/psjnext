---
title: "dlg.set_cell_value()"
description: "Set a value for a specific cell"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'cell_row_id' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'cell_column_id' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Set value for a specific cell of Table.

## Syntax

```psj
dlg.set_cell_value(...)
```

## Inputs

### `name` @type(String) @required

- The name of the Table component.

### `row` @type(Integer) @required @since(5.1.0)

- The position in the horizontal direction of the cell (starts from 0).

### `col` @type(Integer) @required @since(5.1.0)

- The position in the vertical direction of the cell (starts from 0).

### `cell` @type(TableCellID) @required @since(5.1.0)

- Object specifying the location of cell in Table. This argument is only used whe&#x6E;_&#x72;o&#x77;_&#x61;n&#x64;_&#x63;o&#x6C;_&#x61;re not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

### `index` @type(Integer) @required @since(5.1.0)

- The default option to be displayed of the Combobox. The starting value is 0 (fist option > index = 0)

### `value` @type(String) @required

- O&#x72;_&#x4C;ist of Strin&#x67;_&#x6F;&#x72;_&#x4C;ist of Intege&#x72;_&#x6F;&#x72;_&#x4C;ist of Doubl&#x65;_&#x73;pecifying the content(s) which will be displayed on the selected cell.

### `cell_row_id` @type(Integer) @required @deprecated @until(5.1.0)

- The position in the horizontal direction of the cell (starts from 0).

### `cell_column_id` @type(Integer) @required @deprecated @until(5.1.0)

- The position in the vertical direction of the cell (starts from 0).

## Return Code

This function does not have output value.

## Sample Code

```psj {33-39}
from pyjdg import *

def get_table_cell_value(dlg,name,cell):
    cellvector=dlg.get_table_sel_cell(name="Table1")
    if cellvector.size()>0:
        value_cell=dlg.get_cell_value(name="Table1",
            row=cellvector[0].row_number,
            col=cellvector[0].col_number)
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
    dlg.set_cell_value(name="Table1",row=0,col=0,value="Option1")
    dlg.set_cell_value(name="Table1",
        row=1,col=0,value=["Option2","Option3"])
    dlg.set_cell_value(name="Table1",row=0,col=1,value="1")
    dlg.set_cell_value(name="Table1",row=1,col=1,value=[2,3])
    dlg.set_cell_value(name="Table1",row=0,col=2,value="1.5")
    dlg.set_cell_value(name="Table1",cell=TableCellID(1,2),value=[2.5,3.5,4.5], index=1) 

if __name__=='__main__':
    main()
```
