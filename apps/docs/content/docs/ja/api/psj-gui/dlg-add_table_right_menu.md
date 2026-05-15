---
title: "dlg.add _table _right _menu()"
description: "Add options to the context menu (Right click event) of Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add options to the context menu (Right click event) of Table.

## Syntax

```psj
dlg.add _table _right _menu(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### menus

- Specify the menus which will be appeared after executing the right click button event on the Table.

## Return Code

This function does not have output value.

## Sample Code

```psj {13-17}
from pyjdg import *

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
        menus=["Set Cell Color",
            "Set Text Color",
            "Set Column Width",
            "Custom Menu"])
    dlg.generate _window()

if __name__=='__main__':
    main()
```
