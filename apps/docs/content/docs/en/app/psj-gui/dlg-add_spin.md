---
title: "dlg.add_spin()"
description: "Add a Spin to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add a Spin to the creating dialog.

## Syntax

```psj
dlg.add_spin(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `min` @type(Double) @required

- The minimum value of the Spin range.
  If`type`i&#x73;_&#x73;pin.double_, the value will be rounded up.

### `max` @type(Double) @required

- The maximum value of the Spin range.
  If`type`i&#x73;_&#x73;pin.double_, the value will be rounded up.

### `pos` @type(Double) @required

- The initial value (starting position) of the Spin range.
  If`type`i&#x73;_&#x73;pin.double_, the value will be rounded up.

### `increment` @type(Double) @required

- The increment step of the Spin.
  If`type`i&#x73;_&#x73;pin.double_, the value will be rounded up.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `type` @type(Enum) @default(spin.integer)

- Type of Spin:
  - spin.integer: Integer type
  - spin.double: Double type

### `precision` @type(Integer) @default(1)

- The precision (number of digits after zero) of the input value.
  If`type`i&#x73;_&#x73;pin.integer_, this input will be ignored.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_spin(name="Spin2",min=1,max=100,pos=2,increment=2,layout="Window")
    dlg.add_spin(name="Spin3",type=spin.double,min=0.000000,max=50.000000,pos=1.500000,
        increment=1.500000,precision=3,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
