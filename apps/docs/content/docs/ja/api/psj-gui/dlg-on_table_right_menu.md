---
title: "dlg.on _table _right _menu()"
description: "Set event when opening/executing context menu"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set event when opening/executing context menu.

## Syntax

```psj
dlg.on _table _right _menu(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {30}
from pyjdg import *

def on _menu(dlg,name,menu):
    print("Table name: "+ name)
    print("Clicked menu: "+ menu)
    table _cell = dlg.get _table _sel _cell(name)
    if menu == "Set Column Width":
        dlg.set _table _column _width(name,table _cell[0].col _number)
    elif menu == "Set Text Color":
        dlg.set _table _cell _text _color(name,table _cell[0])
    elif menu == "Set Cell Color":
        dlg.set _table _cell _fill _color(name)
    elif menu == "Custom Menu":
        print("You can put your function here")

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
        menus=["Set Cell Color","Set Text Color",
        "Set Column Width","Custom Menu"])
    dlg.generate _window()
    dlg.on _table _right _menu(name="Table1",callfunc=on _menu)

if __name__=='__main__':
    main()
```
