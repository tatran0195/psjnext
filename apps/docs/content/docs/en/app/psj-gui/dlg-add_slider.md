---
title: "dlg.add_slider()"
description: "Add a SliderBar to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a SliderBar to the creating dialog.

## Syntax

```psj
dlg.add_slider(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `width` @type(Integer) @default(60)

- The width of the SliderBar.

### `height` @type(Integer) @default(22)

- The height of the SliderBar.

### `min` @type(Integer) @default(0)

- The minimum value of the SliderBar.

### `max` @type(Integer) @default(100)

- The maximum value of the SliderBar.

### `pos` @type(Integer) @default(0)

- The initial position of the scroller.

### `vertical` @type(Boolean) @default(False)

- The direction of the SliderBar:
  - _True_: creating SliderBar will be put in the vertical direction.
  - _False_: creating SliderBar will be put in the horizontal direction.

### `show_ticks` @type(Boolean) @default(True)

- The state of the slider's tick mark:
  - _True_: show all the tick mark.
  - _False_: hide all the tick mark.

### `show_border` @type(Boolean) @default(False)

- The state of the slider's border:
  - _True_: show outside border of the creating SliderBar.
  - _False_: hide outside border of the creating SliderBar.

### `show_bothticks` @type(Boolean) @default(False)

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
    dlg.add_slider(name="Slider21",width=100,height=100,min=0,max=100,pos=4,
      vertical=True,show_bothticks=True,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
