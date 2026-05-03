---
title: "dlg.set_table_column_data_type()"
description: "Set data type validation of cell of Table"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set data type validation of cell of Table.

## Syntax

```psj
dlg.set_table_column_data_type(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `col` @type(Integer) @required

- The order of column (starts from 0).

### `data_type` @type(String) @required

- The data type validation for the column of Table.
- Support 3 types: "String", "Integer" and "Double"

### `precision` @type(Integer) @default(2)

- Number of digits after floating point displayed inside a Double column.

## Return Code

This function does not have output value.

## Sample Code

```psj {8-13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["String","Integer","Double"],
        layout="Window",width=260,height=260)    
    dlg.set_table_column_data_type(name="Table1",
        col=0,data_type="String")
    dlg.set_table_column_data_type(name="Table1",
        col=1,data_type="Integer")
    dlg.set_table_column_data_type(name="Table1",
        col=2,data_type="Double",precision=5)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="Ok",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
