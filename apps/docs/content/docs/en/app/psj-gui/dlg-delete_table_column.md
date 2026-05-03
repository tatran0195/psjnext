---
title: "dlg.delete_table_column()"
description: "Delete column at a specific position in the Table"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Delete column at a specific position in the Table.

## Syntax

```psj
dlg.delete_table_column(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `position` @type(Integer) @required

- The position of column to be deleted.

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def on_menu(dlg,name,menu):
    sel_ranges=dlg.get_table_sel_range(name="Table1")
    if sel_ranges.size()>0:
        position=sel_ranges[0].left
    dlg.delete_table_column(name="Table1",position=position)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["Heading1","Heading2","Heading3"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_table_right_menu(name="Table1",menus=["Delete Column"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
```
