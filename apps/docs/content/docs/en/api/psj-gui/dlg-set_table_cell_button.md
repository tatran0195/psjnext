---
title: "dlg.set _table _cell _button()"
description: "Set button cell in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set button cell in the Table.

## Syntax

```psj
dlg.set _table _cell _button(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the Table component.

<!-- @since:5.0.1 @type:Integer @required -->
### `row`

- The order of row (starts from 0).

<!-- @since:5.0.1 @type:Integer @required -->
### `col`

- The order of column (starts from 0).

<!-- @since:5.0.1 @type:String @required -->
### `text`

- The text which will be displayed on the button.

## Return Code

This function does not have output value.

## Sample Code

```psj {15-16}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table2",width=260,height=260,
        columns=["Heading1","Heading2"],
        rows=5,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",
        layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _table _cell _button(name="Table2",row=0,
        col=0,text="Button")

if __name__=='__main__':
    main()
```
