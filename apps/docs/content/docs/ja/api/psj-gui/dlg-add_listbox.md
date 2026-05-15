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

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### multisel

- Specify the permission that allow user to select multiple values at the same time:
  - _True_: user can select multiple values.
  - _False_: user can select only one value per time.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### options

- Specify all the options of the ListBox component.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the ListBox.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the ListBox.
- The default value is 0.

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
