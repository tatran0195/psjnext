---
title: "dlg.enable _table _column _filter()"
description: "Add filter option of column of Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add filter option of column of Table.

## Syntax

```psj
dlg.enable _table _column _filter(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### col

- Specify the order of the column (starts from 0).

<!-- @since:5.0.1 @required -->
### enable

- Specify the state of filter mode of column of Table.
  - _True_: filter mode will be shown
  - _False_: filter mode will be hidden

## Return Code

This function does not have output value.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table2",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.enable _table _column _filter(name="Table2",col=0,enable=True)
    dlg.generate _window()

if __name__=='__main__':
    main()
```
