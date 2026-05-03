---
title: "dlg.set_radiobutton_state()"
description: "Set the state of the RadioButton to checked or unchecked"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set the state of the RadioButton to checked or unchecked.

## Syntax

```psj
dlg.set_radiobutton_state(...)
```

## Inputs

### `name` @type(String) @required

- The name of the component in which will be used for setting the state to selected/unselected.

### `checked` @type(Boolean) @required

- The state of the checkbox:
  - _True_: The initial state of the checkbox component is checked.
  - _False_: The initial state of the checkbox component is unchecked.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_radiobutton(name="RadioButton2",text="Jupiter",checked=True,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_radiobutton_state(name="RadioButton2",checked=False)
    isChecked = dlg.isbutton_checked(name="RadioButton2")
    print(isChecked)

if __name__=='__main__':
    main()
```
