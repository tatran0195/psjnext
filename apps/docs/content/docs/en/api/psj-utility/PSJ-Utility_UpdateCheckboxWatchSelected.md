---
title: "JPT.UpdateCheckboxWatchSelected()"
description: "Select (Checked)/Deselect (Unchecked) entities by specifying their ID and their type"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Change checkbox state ON or OFF in Watch Selected window by specifying the entity's ID and type.

## Syntax

```psj
JPT.UpdateCheckboxWatchSelected(DItemType, listOfEntities, BoolType)
```

## Inputs

<!-- @since:5.0.1 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of the entity.

<!-- @since:5.0.1 @type:List[Integer] @required -->
### `listOfEntities`

- The ID of the entities which will be selected or deselected.

<!-- @since:5.0.1 @type:BoolType @required -->
### `BoolType`

- The _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the state of checkbox:
  - _True_: Check the checkbox of item in Watch Selected window.
  - _False_: Uncheck the checkbox of item in Watch Selected window.

:::tip
You also can input **1** instead of inputting JPT.BoolType.TRUE\_VAL,
or input **0** instead of inputting JPT.BoolType.FALSE\_VAL.
:::

## Return Code

This utility function does not have output value.

## Sample Code

```psj {139-145}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                   strName="Cube _3",
                   iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                   strName="Cube _4",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                   strName="Cube _5",
                   iPartColor=7463537)
Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                   strName="Cube _6",
                   iPartColor=7434735)
Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                   strName="Cube _7",
                   iPartColor=14903267)
Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                   strName="Cube _8",
                   iPartColor=15658599)
JPT.ViewFitToModel()

# Renumber Node ID & Element ID
Tools.Renumber(listRenumberItem=[RENUMBER _ITEM(crTarget=Part(1),
                                               iBeginID=1,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(2),
                                               iBeginID=489,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(3),
                                               iBeginID=977,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(4),
                                               iBeginID=1465,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(5),
                                               iBeginID=1953,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(6),
                                               iBeginID=2441,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(7),
                                               iBeginID=2929,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(8),
                                               iBeginID=3417,
                                               iCount=488,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True)])
Tools.Renumber(listRenumberItem=[RENUMBER _ITEM(crTarget=Part(1),
                                               iBeginID=1,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(2),
                                               iBeginID=973,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(3),
                                               iBeginID=1945, iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(4),
                                               iBeginID=2917,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(5),
                                               iBeginID=3889,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(6),
                                               iBeginID=4861,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(7),
                                               iBeginID=5833,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True),
                                 RENUMBER _ITEM(crTarget=Part(8),
                                               iBeginID=6805,
                                               iTargetType=2,
                                               iCount=972,
                                               ilOffset=[10000, 100, 1],
                                               dlCoordTolerance=[0.1, 0.1, 0.1],
                                               bEnable=True)],
               bAssignProp=False)

# Find entities
Home.Find(strSearch="1 2 3 4 5",
          strSelectedType="Node")
Home.Find(strSearch="1 2 3 4 5",
          strSelectedType="2D Element")

# Change checkbox state in Watch Selected window
JPT.UpdateCheckboxWatchSelected(JPT.DItemType.NODE,
                                [1, 2, 3],
                                JPT.BoolType.FALSE _VAL)
JPT.UpdateCheckboxWatchSelected(JPT.DItemType.ELEM,
                                [1, 2, 3],
                                JPT.BoolType.FALSE _VAL)
```
