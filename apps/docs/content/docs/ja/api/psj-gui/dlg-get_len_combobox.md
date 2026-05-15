---
title: "dlg.get _len _combobox()"
description: "Get the size (number of items) of the ComboBox"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the size (number of items) of the ComboBox.

## Syntax

```psj
dlg.get _len _combobox(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the ComboBox component.

## Return Code

An _Integer_ specifying the size of the ComboBox component.

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
    comboBoxLen=dlg.get _len _combobox(name="ComboBox2")
    print(comboBoxLen)

if __name__=='__main__':
    main()
```
