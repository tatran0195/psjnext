---
title: "dlg.add _slider()"
description: "Add a SliderBar to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a SliderBar to the creating dialog.

## Syntax

```psj
dlg.add _slider(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Integer @optional @default:60 -->
### `width`

- The width of the SliderBar.

<!-- @since:5.0.1 @type:Integer @optional @default:22 -->
### `height`

- The height of the SliderBar.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `min`

- The minimum value of the SliderBar.

<!-- @since:5.0.1 @type:Integer @optional @default:100 -->
### `max`

- The maximum value of the SliderBar.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `pos`

- The initial position of the scroller.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `vertical`

- The direction of the SliderBar:
  - _True_: creating SliderBar will be put in the vertical direction.
  - _False_: creating SliderBar will be put in the horizontal direction.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `show _ticks`

- The state of the slider's tick mark:
  - _True_: show all the tick mark.
  - _False_: hide all the tick mark.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `show _border`

- The state of the slider's border:
  - _True_: show outside border of the creating SliderBar.
  - _False_: hide outside border of the creating SliderBar.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `show _bothticks`

- The way to display tick mark:
  - _True_: show tick mark on both side of the SliderBar.
  - _False_: show tick mark on one side only of the SliderBar.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _slider(name="Slider21",width=100,height=100,min=0,max=100,pos=4,
      vertical=True,show _bothticks=True,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
