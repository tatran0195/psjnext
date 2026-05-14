---
title: "dlg.get _listbox _option()"
description: "Get the string value of the being selected ListBox option"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the string value of the being selected ListBox option.

## Syntax

```psj
dlg.get _listbox _option(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ListBox component.

<!-- @since:5.0.1 @type:Integer @required -->
### `option _index`

- The order of the ListBox component's values.

## Return Code

A _String_ specifying the being selected ListBox option.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox1",options=["item1","item2","item3","item4","item5","item6"],
        width=100,height=150,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    print(dlg.get _listbox _option(name="ListBox1",option _index=2))

if __name__=='__main__':
    main()
```
