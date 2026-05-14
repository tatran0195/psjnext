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

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `text`

- The text which will be displayed.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `width`

- The width of the RadioButton.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `height`

- The height of the RadioButton.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `checked`

- The default state of this component:
  - _True_: the default state of this component is checked.
  - _False_: the default state of this component is unchecked.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `group`

- The group in which this RadioButton will be added to:
  - _True_: creating RadioButton will be added separately from the previous RadioButton (different group of button). So, at the time selecting the creating RadioButton, the selected RadioButton will not be deselected.
  - _False_: creating RadioButton will be added to the same group with previous RadioButton. So, at the time selecting the creating RadioButton, the selected RadioButton will be deselected.

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
