---
title: "dlg.set _listbox _sel()"
description: "Set current selection to the ListBox component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set current selection to the ListBox component.

## Syntax

```psj
dlg.set _listbox _sel(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ListBox component.

<!-- @since:5.0.1 @type:Integer @required -->
### `option`

- The or _String_ specifying the order of the ListBox component's values or the name of selected item.

## Return Code

This function does not have output value.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
    dlg.add _listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
        width=100,height=150,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _listbox _sel(name="ListBox2",option=3)

if __name__=='__main__':
    main()
```
