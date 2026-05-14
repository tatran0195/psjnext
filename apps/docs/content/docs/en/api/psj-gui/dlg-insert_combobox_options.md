---
title: "dlg.insert _combobox _options()"
description: "Insert multiple options to a specific position of the inputted ComboBox component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Insert multiple options to a specific position of the ComboBox component.

## Syntax

```psj
dlg.insert _combobox _options(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ComboBox component.

<!-- @since:5.0.1 @type:Integer @required -->
### `position`

- The position in ComboBox to put the new options.

<!-- @since:5.0.1 @type:List[String] @required -->
### `options`

- The new options.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox2",options=["item1","item2","item3","item4","item5"],width=70,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.insert _combobox _options(name="ComboBox2",position=2,options=["item _New _2","item _New _1"])

if __name__=='__main__':
    main()
```
