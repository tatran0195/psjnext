---
title: "dlg.add _radiobutton()"
description: "Add a RadioButton to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a RadioButton to the creating dialog.

## Syntax

```psj
dlg.add _radiobutton(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### text

- Specify text which will be displayed.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the RadioButton.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the RadioButton.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### checked

- Specify the default state of this component:
  - _True_: the default state of this component is checked.
  - _False_: the default state of this component is unchecked.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### group

- Specify the group in which this RadioButton will be added to:
  - _True_: creating RadioButton will be added separately from the previous RadioButton (different group of button). So, at the time selecting the creating RadioButton, the selected RadioButton will not be deselected.
  - _False_: creating RadioButton will be added to the same group with previous RadioButton. So, at the time selecting the creating RadioButton, the selected RadioButton will be deselected.
- The default value is False.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _radiobutton(name="RadioButton16",text="RadioButton",layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    
if __name__=='__main__':
    main()
```
