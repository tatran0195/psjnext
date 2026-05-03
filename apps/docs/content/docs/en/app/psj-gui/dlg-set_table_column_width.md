---
title: "dlg.set_table_column_width()"
description: "Set the width of the specified column in the Table"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set the width of the specified column in the Table.

## Syntax

```psj
dlg.set_table_column_width(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `col` @type(Integer) @required

- The order of the column where its width will be changed (starts from 0).

### `width` @type(Integer)

- The column width.
- If not specified, a dialog is opened for user to enter a value.

## Return Code

This function does not have output value.

## Sample Code

```psj {6-7,9-10}
from pyjdg import *

def on_menu(dlg,name,menu):
    cellvector=dlg.get_table_sel_cell(name)
    if menu=="Set Column Width using Dialog":
        dlg.set_table_column_width(name="Table1",
            col=cellvector[0].col_number)
    if menu=="Set Column Width equal 400":
        dlg.set_table_column_width(name="Table1",
            col=cellvector[0].col_number,width=400)
    elif menu=="Get Column Width":
        col_width = dlg.get_table_column_width(name="Table1",
            col=cellvector[0].col_number)
        print("Column "+str(cellvector[0].col_number)+
            " width is: "+str(col_width))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_table_right_menu(name="Table1",
        menus=["Set Column Width using Dialog",
        "Set Column Width equal 400","Get Column Width"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
```
