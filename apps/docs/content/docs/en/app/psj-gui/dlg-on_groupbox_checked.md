---
title: "dlg.on_groupbox_checked()"
description: "Bind a created def function to a GroupBox's CheckBox"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Bind a created def function to a GroupBox's CheckBox.

## Syntax

```psj
dlg.on_groupbox_checked(...)
```

## Inputs

### `name` @type(String) @required

- The name of the GroupBox using for binding a created def function.

### `callfunc` @type(PSJCallable) @required

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

````psj {14}
from pyjdg import *
def on_group_checked(dlg,checked):
    if checked :
        print("checked")
    else:
        print("unchecked")
    print("get checked status==", str(dlg.is_groupbox_checked("GroupBox2")))

def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
    dlg.set_groupbox_checked(name="GroupBox2",checked=False)
    dlg.add_button(name="Button3",text="Button",width=60,height=22,bk_color=15790320,layout="GroupBox2")
    dlg.generate_window()
    dlg.on_groupbox_checked("GroupBox2",on_group_checked)
if __name__=='__main__':
    main()```
````
