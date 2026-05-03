---
title: "dlg.is_groupbox_checked()"
description: "Check the state of a GroupBox's checkbox"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Check the state of a GroupBox's checkbox.

## Syntax

```psj
dlg.is_groupbox_checked(...)
```

## Inputs

### `name` @type(String) @required

- The name of GroupBox.

## Return Code

A _Boolean_ specifying the state of groupbox checkbox:

- _True_: The groupbox checkbox is checked.
- _False_: The groupbox checkbox is unchecked.

## Sample Code

```psj {7}
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
    main()
```
