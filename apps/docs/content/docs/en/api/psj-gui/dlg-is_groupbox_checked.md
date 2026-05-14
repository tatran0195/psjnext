---
title: "dlg.is _groupbox _checked()"
description: "Check the state of a GroupBox's checkbox"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Check the state of a GroupBox's checkbox.

## Syntax

```psj
dlg.is _groupbox _checked(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of GroupBox.

## Return Code

A _Boolean_ specifying the state of groupbox checkbox:

- _True_: The groupbox checkbox is checked.
- _False_: The groupbox checkbox is unchecked.

## Sample Code

```psj {7}
from pyjdg import *
def on _group _checked(dlg,checked):
    if checked :
        print("checked")
    else:
        print("unchecked")
    print("get checked status==", str(dlg.is _groupbox _checked("GroupBox2")))
def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _groupbox(name="GroupBox2",text="GroupBox",layout="Window")
    dlg.set _groupbox _checked(name="GroupBox2",checked=False)
    dlg.add _button(name="Button3",text="Button",width=60,height=22,bk _color=15790320,layout="GroupBox2")
    dlg.generate _window()
    dlg.on _groupbox _checked("GroupBox2",on _group _checked)
if __name__=='__main__':
    main()
```
