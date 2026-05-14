---
title: "dlg.set _table _cell _checkbox()"
description: "Set checkbox cell in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set checkbox cell in the Table.

## Syntax

```psj
dlg.set _table _cell _checkbox(...)
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

- The text which will be displayed next to the checkbox.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `checked`

- The state of checkbox.
  - _True_: the checkbox is checked.
  - _False_: the checkbox is unchecked.

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
    dlg.set _table _cell _checkbox(name="Table2",row=0,
        col=0,text="Checkbox",checked=True)

if __name__=='__main__':
    main()
```
