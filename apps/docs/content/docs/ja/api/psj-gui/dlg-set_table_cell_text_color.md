---
title: "dlg.set _table _cell _text _color()"
description: "Set text's color to the selected/specified cells"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set color to text in the selected/specified cells.

## Syntax

```psj
dlg.set _table _cell _text _color(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @optional -->
### cell

- Specify the location of cell in Table.
- If not specified, all the selected cells will be used.

<!-- @since:5.0.1 @optional -->
### color

- Specify the color.
- If not specified, a color picker dialog is opened for user to select.

## Return Code

This function does not have output value.

## Sample Code

```psj {6,8-9,11-12,14-15,17-19}
from pyjdg import *

def on _menu(dlg,name,menu):
    cellvector=dlg.get _table _sel _cell(name)
    if menu=="Set Text Color for all selected cells using color picker":
        dlg.set _table _cell _text _color(name="Table1")
    elif menu=="Set Text Color only for a selected cell using color picker":
         dlg.set _table _cell _text _color(name="Table1",
            cell=cellvector[0])
    elif menu=="Set Text Color only for a selected cell with red color":
        dlg.set _table _cell _text _color(name="Table1",
            cell=cellvector[0],color=7105764)
    elif menu=="Set Text Color only for the first cell with red color":
        dlg.set _table _cell _text _color(name="Table1",
            cell=TableCellID(row=0,col=0),color=7105764)
    elif menu=="Set Text Color only for the first 2x2 cells with red color":
        [[dlg.set _table _cell _text _color(name="Table1",
            cell=TableCellID(row=i,col=j),color=7105764)
            for i in (0,1)] for j in (0,1)]

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
        menus=["Set Text Color for all selected cells using color picker",
        "Set Text Color only for a selected cell using color picker",
        "Set Text Color only for a selected cell with red color",
        "Set Text Color only for the first cell with red color",
        "Set Text Color only for the first 2x2 cells with red color"])
    dlg.generate _window()
    dlg.on _table _right _menu(name="Table1",callfunc=on _menu)

if __name__=='__main__':
    main()
```
