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

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ComboBox component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Integer @required -->
### `index`

- The default option to be displayed of the ComboBox.
- The starting value is 0 (first option -> index=0).

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `options`

- The options of the ComboBox.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `width`

- The width of the ComboBox.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `height`

- The height of the ComboBox.

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
