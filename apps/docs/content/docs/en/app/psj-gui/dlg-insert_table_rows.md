---
title: "dlg.insert_table_rows()"
description: "Insert row(s) at a specific position in the Table"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Insert row(s) at a specific position in the Table.

## Syntax

```psj
dlg.insert_table_rows(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `row_num` @type(Integer) @required

- The number of rows to be inserted.

### `position` @type(Integer)

- The position of row to be inserted.
  - If specified, the row will be inserted in front of the inputted position (position-1).
  - If not specified,the row will be inserted at the end of the table.
- This is a default input.

## Return Code

This function does not have output value.

## Sample Code

```psj {10-11,14-15,17}
from pyjdg import *

def on_click_insert_row(dlg):
    num_row=int(dlg.get_item_text(name="Row"))
    sel_ranges=dlg.get_table_sel_range(name="Table1")
    position=int(dlg.get_total_row(name="Table1"))
    if sel_ranges.size()>0:
        if sel_ranges[0].top == 0:
            position=sel_ranges[0].top
            dlg.insert_table_rows(name="Table1",
                row_num=num_row,position=position)
        elif sel_ranges[0].top > 0:
            position=sel_ranges[0].top
            dlg.insert_table_rows(name="Table1",
                row_num=num_row,position=position)
    else:
        dlg.insert_table_rows(name="Table1",row_num=num_row)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="Insert Rows",layout="Window")
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,
        layout="GroupBox1")
    dlg.add_label(name="Label1",text="Number of Rows",layout="Layout2")
    dlg.add_textbox(name="Row",layout="Layout2")
    dlg.add_button(name="InsertRow",text="Insert Row",
        width=100,height=22,layout="GroupBox1")
    dlg.add_table(name="Table1",rows=5,
        columns=["Heading1","Heading2","Heading3"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    for i in range(5):
        for j in range(3):
            dlg.set_cell_value(name="Table1",row=i,col=j,value=str(i+j))
    dlg.on_command(name="InsertRow",callfunc=on_click_insert_row)
if __name__=='__main__':
    main()
```
