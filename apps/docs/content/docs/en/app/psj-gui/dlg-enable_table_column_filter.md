---
title: "dlg.enable_table_column_filter()"
description: "Add filter option of column of Table"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add filter option of column of Table.

## Syntax

```psj
dlg.enable_table_column_filter(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `col` @type(Integer) @required

- The order of the column (starts from 0).

### `enable` @type(Boolean) @required

- The state of filter mode of column of Table.
  - _True_: filter mode will be shown
  - _False_: filter mode will be hidden

## Return Code

This function does not have output value.

## Sample Code

```psj {14}
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
    dlg.enable_table_column_filter(name="Table2",col=0,enable=True)
    dlg.generate_window()

if __name__=='__main__':
    main()
```
