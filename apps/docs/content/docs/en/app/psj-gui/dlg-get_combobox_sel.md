---
title: "dlg.get_combobox_sel()"
description: "Get the index of the being selected ComboBox option"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the index of the being selected ComboBox option.

## Syntax

```psj
dlg.get_combobox_sel(...)
```

## Inputs

### `name` @type(String) @required

- The name of the ComboBox component.

## Return Code

An _Integer_ specifying the index of the being selected ComboBox option.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_combobox(name="ComboBox1",options=["item1","item2","item3","item4","item5","item6"],layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_combobox_sel(name="ComboBox1",option=3)
    print(dlg.get_combobox_sel(name="ComboBox1"))

if __name__=='__main__':
    main()
```
