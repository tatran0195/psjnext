---
title: "dlg.on _groupbox _checked()"
description: "Bind a created def function to a GroupBox's CheckBox"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Bind a created def function to a GroupBox's CheckBox.

## Syntax

```psj
dlg.on _groupbox _checked(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the GroupBox using for binding a created def function.

<!-- @since:5.1.0 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

````psj {14}
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
    main()```
````
