---
title: "dlg.get_total_row()"
description: "Get the total number of rows of the Table"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the total number of rows of the Table.

## Syntax

```psj
dlg.get_total_row(...)
```

## Inputs

### `name` @type(String) @required

- The name of the Table component.

## Return Code

An _Integer_ specifying the total number of rows of the Table.

## Sample Code

```psj {14}
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
    total_rows = dlg.get_total_row(name="Table1")
    JPT.Debugger(total_rows)

if __name__=='__main__':
    main()
```
