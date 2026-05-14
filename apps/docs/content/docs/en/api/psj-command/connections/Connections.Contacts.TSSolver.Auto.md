---
title: "Connections.Contacts.TSSolver.Auto()"
description: "Search and creat contact between the existing parts automatically based on the specified conditions"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > TSSolver > Auto"
---

## Description

Search and creat contact between the existing parts automatically based on the specified conditions.

## Syntax

```psj
Connections.Contacts.TSSolver.Auto(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlNames`

- The list of the contact names to be created.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crllMasterFaceTargets`

- The list of master faces.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crllSlaveFaceTargets`

- The list of slave faces.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[1] -->
### `crlContactTypes`

- The list of contact types.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[1.0] -->
### `dlInterferenceClosures`

- The list interference closures.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[DFLT _DBL] -->
### `dlFrictionCoefficients`

- The list friction coefficients.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `blInitialAdjustments`

- Whether or not using initial adjustments.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:65280 -->
### `crlColors`

- The list of contact colors.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEdit`

- The list of existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is left _None_, a new contact settings item will be created.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterGroups`

- The list of master groups.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveGroups`

- The list of slave groups.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {6,7,8,9,10,11}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6250449)

created _contact = Connections.Contacts.TSSolver.Auto(strlNames=["C1 _Cube _1(24)_Cube _2(49)"], 
                                                     crllMasterFaceTargets=[[Face(24)]], 
                                                     crllSlaveFaceTargets=[[Face(49)]],
                                                     crlEdit=[None],
                                                     crlMasterGroups=[None], 
                                                     crlSlaveGroups=[None])

JPT.Debugger(created _contact)
```
