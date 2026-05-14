---
title: "dlg.set _table _column _data _type()"
description: "Set data type validation of cell of Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set data type validation of cell of Table.

## Syntax

```psj
dlg.set _table _column _data _type(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

<!-- @since:5.0.1 @type:Integer @required -->
### `col`

- The order of column (starts from 0).

<!-- @since:5.0.1 @type:String @required -->
### `data _type`

- The data type validation for the column of Table.
- Support 3 types: "String", "Integer" and "Double"

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `precision`

- The number of digits after floating point displayed inside a Double column.

## Return Code

This function does not have output value.

## Sample Code

```psj {8-13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,
        columns=["String","Integer","Double"],
        layout="Window",width=260,height=260)    
    dlg.set _table _column _data _type(name="Table1",
        col=0,data _type="String")
    dlg.set _table _column _data _type(name="Table1",
        col=1,data _type="Integer")
    dlg.set _table _column _data _type(name="Table1",
        col=2,data _type="Double",precision=5)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="Ok",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
