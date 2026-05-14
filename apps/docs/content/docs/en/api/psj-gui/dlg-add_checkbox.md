---
title: "dlg.add _checkbox()"
description: "Add a CheckBox to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a CheckBox to the creating dialog.

## Syntax

```psj
dlg.add _checkbox(...)
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

- The text which will be displayed next to the CheckBox.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `checked`

- The default state of this component:
  - _True_: the default state of this component is checked.
  - _False_: the default state of this component is unchecked.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `lefttext`

- The text is on left side of CheckBox:
  - _True_: the text is on left side of the CheckBox.
  - _False_: the text is on right side of the CheckBox.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `width`

- The width of the CheckBox.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `height`

- The height of the CheckBox.

## Return Code

This function does not have output value.

## Sample Code

```psj {5,6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _checkbox(name="CheckBox2",text="CheckBox",lefttext=True,checked=True,layout="Window")
    dlg.add _checkbox(name="CheckBox3",text="CheckBox",lefttext=False,checked=True,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
