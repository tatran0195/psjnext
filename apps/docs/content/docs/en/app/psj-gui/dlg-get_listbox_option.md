---
title: "dlg.get_listbox_option()"
description: "Get the string value of the being selected ListBox option"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the string value of the being selected ListBox option.

## Syntax

```psj
dlg.get_listbox_option(...)
```

## Inputs

### `name` @type(String) @required

- The name of the ListBox component.

### `option_index` @type(Integer) @required

- The order of the ListBox component's values.

## Return Code

A _String_ specifying the being selected ListBox option.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_listbox(name="ListBox1",options=["item1","item2","item3","item4","item5","item6"],
        width=100,height=150,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    print(dlg.get_listbox_option(name="ListBox1",option_index=2))

if __name__=='__main__':
    main()
```
