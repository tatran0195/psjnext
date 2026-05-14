---
title: "dlg.add _combobox _option()"
description: "Add an option to the ComboBox component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add an option to the ComboBox component.

## Syntax

```psj
dlg.add _combobox _option(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ComboBox component.

<!-- @since:5.0.1 @type:String @required -->
### `option _text`

- The option added.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox2",options=["item1","item2","item3","item4"],layout="Layout1")
    dlg.add _combobox _option(name="ComboBox2",option _text="new _item")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")

    dlg.generate _window()
if __name__=='__main__':
    main()
```
