---
title: "Connections.Contacts.TSSolver.Auto()"
description: "Search and creat contact between the existing parts automatically based on the specified conditions"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > TSSolver > Auto"
---

## Description

Search and creat contact between the existing parts automatically based on the specified conditions.

## Syntax

```psj
Connections.Contacts.TSSolver.Auto(...)
```

## Inputs

### `strlNames` @type(List\[String]) @required

- The list of the contact names to be created.

### `crllMasterFaceTargets` @type(List\[Cursor]) @required

- The list of master faces.

### `crllSlaveFaceTargets` @type(List\[Cursor]) @required

- The list of slave faces.

### `crlContactTypes` @type(List\[Cursor]) @default(\[1])

- The list of contact types.

### `dlInterferenceClosures` @type(List\[Double]) @default(\[1.0])

- The list interference closures.

### `dlFrictionCoefficients` @type(List\[Double]) @default(\[DFLT\_DBL])

- The list friction coefficients.

### `blInitialAdjustments` @type(Boolean) @default(False)

- Whether or not using initial adjustments.

### `crlColors` @type(List\[Cursor]) @default(65280)

- The list of contact colors.

### `crlEdit` @type(List\[Cursor]) @default(\[])

- The list of existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new contact settings item will be created.

### `crlMasterGroups` @type(List\[Cursor]) @default(\[])

- The list of master groups.

### `crlSlaveGroups` @type(List\[Cursor]) @default(\[])

- The list of slave groups.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {6,7,8,9,10,11}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

created_contact = Connections.Contacts.TSSolver.Auto(strlNames=["C1_Cube_1(24)_Cube_2(49)"], 
                                                     crllMasterFaceTargets=[[Face(24)]], 
                                                     crllSlaveFaceTargets=[[Face(49)]],
                                                     crlEdit=[None],
                                                     crlMasterGroups=[None], 
                                                     crlSlaveGroups=[None])

JPT.Debugger(created_contact)
```
