---
title: "dlg.get _combobox _sel()"
description: "Get the index of the being selected ComboBox option"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the index of the being selected ComboBox option.

## Syntax

```psj
dlg.get _combobox _sel(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ComboBox component.

## Return Code

An _Integer_ specifying the index of the being selected ComboBox option.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _combobox(name="ComboBox1",options=["item1","item2","item3","item4","item5","item6"],layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _combobox _sel(name="ComboBox1",option=3)
    print(dlg.get _combobox _sel(name="ComboBox1"))

if __name__=='__main__':
    main()
```
