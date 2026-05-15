---
title: "dlg.add _combobox()"
description: "Add a ComboBox component to the dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a ComboBox component to the dialog.

## Syntax

```psj
dlg.add _combobox(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the ComboBox component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @required -->
### index

- Specify the default option to be displayed of the ComboBox.
- The starting value is 0 (first option -> index=0).

<!-- @since:5.0.1 @optional -->
### options

- Specify the options of the ComboBox.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the ComboBox.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the ComboBox.
- The default value is 0.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox2",options=["item1","item2","item3","item4"],index=1,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
