---
title: "JPT.HighlightByID()"
description: "Highlight an item in Assembly tree by using its DItem type and its ID"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Highlight an item in Assembly tree by using its _[DItemType](../data-type/psj-command/DItem-types)_ and its ID.

## Syntax

```psj
JPT.HighlightByID(DItemType, entityID, BoolType)
```

## Inputs

### `DItemType` @type(Enum) @required

- &#xNAN;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f the target entities.

### `entityID` @type(Integer) @required

- ID of the selecting entity.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the selection mode:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {18}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Create LBCs
BoundaryConditions.Pressure.General(dPressure=100000000.0, crlTargets=[Face(26)])
BoundaryConditions.Force.General(forceLBC=FORCE_LBC(vecForce=[DFLT_DBL, DFLT_DBL, -10.0]), 
    crlTargets=[Face(52)])
BoundaryConditions.FixedConstraint(crlTargets=[Face(77, 51, 25)])

# Highlight Pressure item in Assembly tree
listDItemLoadBCs = JPT.GetAllLoadsBCs()
for lbc in listDItemLoadBCs:
    if lbc.type == JPT.DItemType.LBC_G_PRESSURE:
        iID = lbc.id
JPT.HighlightByID(JPT.DItemType.LBC_G_PRESSURE, iID, JPT.BoolType.TRUE_VAL)
```
