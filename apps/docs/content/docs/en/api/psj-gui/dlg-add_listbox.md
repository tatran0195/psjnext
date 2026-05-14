---
title: "dlg.add _listbox()"
description: "Add a ListBox to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a ListBox to the creating dialog.

## Syntax

```psj
dlg.add _listbox(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `multisel`

- The permission that allow user to select multiple values at the same time:
  - _True_: user can select multiple values.
  - _False_: user can select only one value per time.

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `options`

- The all the options of the ListBox component.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `width`

- The width of the ListBox.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `height`

- The height of the ListBox.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox3",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")

    dlg.generate _window()
if __name__=='__main__':
    main()
```
