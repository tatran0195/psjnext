---
title: "dlg.on _listbox _sel()"
description: "Run a created function after a ListBox item is selected"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Run a created function after a ListBox item is selected.

## Syntax

```psj
dlg.on _listbox _sel(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the ListBox component using for binding a created def function.

<!-- @since:5.1.0 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {20}
from pyjdg import *

def on _listbox _item _changed(dlg):
    JPT.ClearLog()
    listBoxPos=dlg.get _listbox _sel(name="ListBox2")
    listBoxName=dlg.get _listbox _option(name="ListBox2", option _index=listBoxPos)
    dlg.set _item _text(name="TextBox5", text=listBoxName)
    print('The selected list box item is: ', str(listBoxName))

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],width=100,height=120,
        layout="Window")
    dlg.set _item _size _behavior(name="ListBox2",behavior=size _behavior.fixed)
    dlg.add _layout(name="Layout3",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label4",text="Selected Item",width=70,text _halign="left",text _valign="top",
        layout="Layout3")
    dlg.add _textbox(name="TextBox5",width=100,layout="Layout3")
    dlg.generate _window()
    dlg.on _listbox _sel(name="ListBox2", callfunc=on _listbox _item _changed)
if __name__=='__main__':
    main()
```
