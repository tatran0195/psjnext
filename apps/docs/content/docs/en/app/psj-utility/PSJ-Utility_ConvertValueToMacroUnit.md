---
title: "JPT.ConvertValueToMacroUnit()"
description: "Convert the inputted value from the SI\\[m\\] unit (Jupiter macro unit) to the specified unit"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert the inputted value from the SI\[m] unit (Jupiter macro unit) to the specified unit.
The return value will be the value after conversion.

## Syntax

```psj
JPT.ConvertValueToMacroUnit(inputValue, unitType, outputValueType)
```

## Inputs

### `inputValue` @type(Double) @required

- Which will be used for converting.

### `unitType` @type(Enum) @required

- Th&#x65;_[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_&#x77;hich will be used as the reference for converting.
- The type of unit can be found at:<menuselection>Home » Preference » Unit</menuselection>in Jupiter.

### `outputValueType` @type(String) @required

- The desired unit of the inputted value which will be got after converting from Jupiter macro unit.

## Return Code

A _Double_ specifying the converted value.

## Sample Code

```psj {2}
# Convert 1m from Jupiter macro unit system to mm
convertToMacro = JPT.ConvertValueToMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # 1m -> mm
JPT.Debugger(convertToMacro) # 1000
```
