---
title: "dlg.get _total _row()"
description: "Get the total number of rows of the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the total number of rows of the Table.

## Syntax

```psj
dlg.get _total _row(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the Table component.

## Return Code

An _Integer_ specifying the total number of rows of the Table.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=14,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    total _rows = dlg.get _total _row(name="Table1")
    JPT.Debugger(total _rows)

if __name__=='__main__':
    main()
```
