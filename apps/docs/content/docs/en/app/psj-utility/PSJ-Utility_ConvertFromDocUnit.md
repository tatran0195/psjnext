---
title: "JPT.ConvertFromDocUnit()"
description: "Convert the inputted value from the current using Jupiter unit system to SI\\[m\\] units (Jupiter macro units)"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert the inputted value from the current using Jupiter unit system to SI\[m] unit (Jupiter macro unit).
The return value will be the value after the conversion.

## Syntax

```psj
JPT.ConvertFromDocUnit(inputValue, unitType)
```

## Inputs

### `inputValue` @type(Double) @required

- Which will be used for converting.

### `unitType` @type(Enum) @required

- Th&#x65;_[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_&#x77;hich will be used as the reference for converting.
- The type of unit can be found at:<menuselection>Home » Preference » Unit</menuselection>in Jupiter.

## Return Code

A _Double_ specifying the converted value.

## Sample Code

```psj {2}
# Convert the value = 1 from the current Jupiter Unit system to Jupiter macro unit system
convertFromDoc = JPT.ConvertFromDocUnit(1, JPT.UnitType.Unit_Length)
JPT.Debugger(convertFromDoc)
```
