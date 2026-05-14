---
title: "dlg.add _listbox _option()"
description: "Add an option to the ListBox component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add an option to the ListBox component.

## Syntax

```psj
dlg.add _listbox _option(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ListBox component.

<!-- @since:5.0.1 @type:String @required -->
### `option _text`

- The option added.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox3",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add _listbox _option(name="ListBox3",option _text="new _item")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
