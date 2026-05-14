---
title: "dlg.add _spin()"
description: "Add a Spin to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Spin to the creating dialog.

## Syntax

```psj
dlg.add _spin(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:Double @required -->
### `min`

- The minimum value of the Spin range.
  If`type` is _spin.double_, the value will be rounded up.

<!-- @since:5.0.1 @type:Double @required -->
### `max`

- The maximum value of the Spin range.
  If`type` is _spin.double_, the value will be rounded up.

<!-- @since:5.0.1 @type:Double @required -->
### `pos`

- The initial value (starting position) of the Spin range.
  If`type` is _spin.double_, the value will be rounded up.

<!-- @since:5.0.1 @type:Double @required -->
### `increment`

- The increment step of the Spin.
  If`type` is _spin.double_, the value will be rounded up.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Enum @optional @default:spin.integer -->
### `type`

- The type of Spin:
  - spin.integer: Integer type
  - spin.double: Double type

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `precision`

- The precision (number of digits after zero) of the input value.
  If`type` is _spin.integer_, this input will be ignored.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _spin(name="Spin2",min=1,max=100,pos=2,increment=2,layout="Window")
    dlg.add _spin(name="Spin3",type=spin.double,min=0.000000,max=50.000000,pos=1.500000,
        increment=1.500000,precision=3,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
