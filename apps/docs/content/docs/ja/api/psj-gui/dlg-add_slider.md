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

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the SliderBar.
- The default value is 60.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the SliderBar.
- The default value is 22.

<!-- @since:5.0.1 @optional -->
### min

- Specify the minimum value of the SliderBar.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### max

- Specify the maximum value of the SliderBar.
- The default value is 100.

<!-- @since:5.0.1 @optional -->
### pos

- Specify the initial position of the scroller.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### vertical

- Specify the direction of the SliderBar:
  - _True_: creating SliderBar will be put in the vertical direction.
  - _False_: creating SliderBar will be put in the horizontal direction.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### show\_ticks

- Specify the state of the slider's tick mark:
  - _True_: show all the tick mark.
  - _False_: hide all the tick mark.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### show\_border

- Specify the state of the slider's border:
  - _True_: show outside border of the creating SliderBar.
  - _False_: hide outside border of the creating SliderBar.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### show\_bothticks

- Specify the way to display tick mark:
  - _True_: show tick mark on both side of the SliderBar.
  - _False_: show tick mark on one side only of the SliderBar.
- The default value is _False_.

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
