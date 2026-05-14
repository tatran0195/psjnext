---
title: "dlg.on _combobox _sel()"
description: "Run a created function after a ComboBox item is selected"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Run a created function after a ComboBox item is selected.

## Syntax

```psj
dlg.on _combobox _sel(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ComboBox component using for binding a created def function.

<!-- @since:5.0.1 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {21}
from pyjdg import *

def on _combobox _select(dlg):
    print("Index of selected combobox: {}"
        .format(dlg.get _combobox _sel(name="ComboBox1")))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,100,0],
        orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox1",
        options=["item1","item2","item3","item4","item5"],
        width=70,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _combobox _sel(name="ComboBox1",callfunc=on _combobox _select)

if __name__=='__main__':
    main()
```
