---
title: "dlg.insert _listbox _option()"
description: "Insert an option to a specific position of the inputted ListBox"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Insert an option to a specific position of the ListBox component.

## Syntax

```psj
dlg.insert _listbox _option(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ListBox component.

<!-- @since:5.0.1 @type:Integer @required -->
### `position`

- The position in ListBox to put the new option.

<!-- @since:5.0.1 @type:String @required -->
### `option`

- The text which will be used as a ListBox option.

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
    dlg.insert _listbox _option(name="ListBox2",position=2,option="item _New")

if __name__=='__main__':
    main()
```
