---
title: "JPT.ConvertFromMacroUnit()"
description: "Convert the inputted value with the specified unit to the SI\\[m\\] unit (Jupiter macro unit)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert the inputted value with the specified unit to the SI\[m] unit (Jupiter macro unit).
The return value will be the value after the conversion.

## Syntax

```psj
JPT.ConvertFromMacroUnit(inputValue, unitType, outputValueType)
```

## Inputs

### `inputValue`

- A _Double_ which will be used for converting.

<!-- @since:5.0.1 @required -->
### unitType

- Specify the_[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
- The type of unit can be found at: <menuselection>Home » Preference » Unit</menuselection> in Jupiter.

<!-- @since:5.0.1 @required -->
### outputValueType

- Specify the indicated unit of the inputted value which will be used for converting to Jupiter macro unit.

## Return Code

A _Double_ specifying the converted value.

## Sample Code

```psj {2}
# Convert 1mm to the Jupiter macro unit system
convertFromMacro = JPT.ConvertFromMacroUnit(1, JPT.UnitType.Unit _Length, 'mm') # mm -> m
JPT.Debugger(convertFromMacro) # 0.001 m
```
