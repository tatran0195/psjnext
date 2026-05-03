---
title: "JPT.ConvertValueToDocUnit()"
description: "Convert the inputted value from SI\\[m\\] units (Jupiter macro units) to the current Jupiter unit system"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert the inputted value from SI\[m] units (Jupiter macro units) to the current Jupiter unit system.

## Syntax

```psj
JPT.ConvertValueToDocUnit(inputValue, unitType)
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
# Convert 1m in Jupiter macro unit system to the current unit system of Jupiter
convertToDoc = JPT.ConvertValueToDocUnit(1, JPT.UnitType.Unit_Length)
JPT.Debugger(convertToDoc)
```
