---
title: "dlg.set _table _cell _alignment()"
description: "Set text alignment of cell"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set text alignment of cell.

## Syntax

```psj
dlg.set _table _cell _alignment(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### row

- Specify the order of row (starts from 0).

<!-- @since:5.0.1 @required -->
### col

- Specify the order of column (starts from 0).

<!-- @since:5.0.1 @required -->
### alignment

- Specify alignment position of content inside a cell.
  - "Left": Align content to the left
  - "Center": Center the content
  - "Right": Align content to the right

## Return Code

This function does not have output value.

## Sample Code

```psj {4-9}
from pyjdg import *

def on _click _set _alignment(dlg):
    dlg.set _table _cell _alignment(name="Table1",row=0,col=0,
        alignment="Left")
    dlg.set _table _cell _alignment(name="Table1",row=1,col=0,
        alignment="Center")
    dlg.set _table _cell _alignment(name="Table1",row=2,col=0,
        alignment="Right")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=360,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonSetAlignment",width=70,height=30,
        text="Set Alignment",layout="footer")
    dlg.add _button(name="Ok",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _table _column _width(name="Table1",col=0,width=200)
    dlg.set _cell _value(name="Table1",row=0,col=0,
        value="Left Alignment")
    dlg.set _cell _value(name="Table1",row=1,col=0,
        value="Center Alignment")
    dlg.set _cell _value(name="Table1",row=2,col=0,
        value="Right Alignment")
    dlg.on _command(name="ButtonSetAlignment",callfunc=on _click _set _alignment)

if __name__=='__main__':
    main()
```
