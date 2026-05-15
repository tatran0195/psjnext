---
title: "dlg.get _table _cell _fill _color()"
description: "Get the fill color of the selected/specified cell"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get the fill color of the selected/specified cell.

## Syntax

```psj
dlg.get _table _cell _fill _color(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of Table.

<!-- @since:5.1.0 @required -->
### row

- Specify the position in the horizontal direction of the cell  (starts from 0).

<!-- @since:5.1.0 @required -->
### col

- Specify the position in the vertical direction of the cell (starts from 0).

## Return Code

An _Integer_ specifying color code in Jupiter.

## Sample Code

```psj {6-8}
from pyjdg import *

def on _menu(dlg,name,menu):
    cellvector=dlg.get _table _sel _cell(name="Table1")
    if menu=="Get cell color":
        colorCell = dlg.get _table _cell _fill _color(name="Table1", 
            row=cellvector[0].row _number,
            col=cellvector[0].col _number)
        print("The selected cell has the fill color is: " + str(colorCell))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2","Heading3"],
        layout="Window",show _row _number=True,width=350,height=160)
    dlg.add _label(name="Labe2",text="Right-click on the seleted cell then select Get cell color",
        width=350,layout="Window")
    for i in range(3):
        dlg.set _table _column _width("Table2", i, 100)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _table _right _menu(name="Table1",
        menus=["Get cell color"])
    dlg.generate _window()
    dlg.set _table _cell _fill _color(name="Table1",
            cell=TableCellID(row=0,col=0),color=7105764)
    dlg.set _table _cell _fill _color(name="Table1",
            cell=TableCellID(row=0,col=1),color=255)
    dlg.set _table _cell _fill _color(name="Table1",
            cell=TableCellID(row=0,col=2),color=0)
    colorValue=JPT.ConvertRGBToJPTColor(255,255,0)
    for i in range(1,3):
        for j in range(0,3):
            dlg.set _table _cell _fill _color(name="Table1",
                cell=TableCellID(row=i,col=j),color=colorValue)
            colorValue+=100000
    dlg.on _table _right _menu(name="Table1",callfunc=on _menu)

if __name__=='__main__':
    main()
```
