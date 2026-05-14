---
title: "dlg.set _table _column _width()"
description: "Set the width of the specified column in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the width of the specified column in the Table.

## Syntax

```psj
dlg.set _table _column _width(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

<!-- @since:5.0.1 @type:Integer @required -->
### `col`

- The order of the column where its width will be changed (starts from 0).

<!-- @since:5.0.1 @type:Integer @optional -->
### `width`

- The column width.
- If not specified, a dialog is opened for user to enter a value.

## Return Code

This function does not have output value.

## Sample Code

```psj {6-7,9-10}
from pyjdg import *

def on _menu(dlg,name,menu):
    cellvector=dlg.get _table _sel _cell(name)
    if menu=="Set Column Width using Dialog":
        dlg.set _table _column _width(name="Table1",
            col=cellvector[0].col _number)
    if menu=="Set Column Width equal 400":
        dlg.set _table _column _width(name="Table1",
            col=cellvector[0].col _number,width=400)
    elif menu=="Get Column Width":
        col _width = dlg.get _table _column _width(name="Table1",
            col=cellvector[0].col _number)
        print("Column "+str(cellvector[0].col _number)+
            " width is: "+str(col _width))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _table _right _menu(name="Table1",
        menus=["Set Column Width using Dialog",
        "Set Column Width equal 400","Get Column Width"])
    dlg.generate _window()
    dlg.on _table _right _menu(name="Table1",callfunc=on _menu)

if __name__=='__main__':
    main()
```
