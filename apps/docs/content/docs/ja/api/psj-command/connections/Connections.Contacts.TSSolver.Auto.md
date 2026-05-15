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

<!-- @since:5.0.1 @required -->
### strlNames

- Specify the list of the contact names to be created.

<!-- @since:5.0.1 @required -->
### crllMasterFaceTargets

- Specify the list of master faces.

<!-- @since:5.0.1 @required -->
### crllSlaveFaceTargets

- Specify the list of slave faces.

<!-- @since:5.0.1 @optional -->
### crlContactTypes

- Specify the list of contact types.
- The default value is \[1].

<!-- @since:5.0.1 @optional -->
### dlInterferenceClosures

- Specify the list interference closures.
- The default value is \[1.0].

<!-- @since:5.0.1 @optional -->
### dlFrictionCoefficients

- Specify the list friction coefficients.
- The default value is \[DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### blInitialAdjustments

- Specify Whether or not using initial adjustments.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crlColors

- Specify the list of contact colors.
- The default value is 65280.

<!-- @since:5.0.1 @optional -->
### crlEdit

- Specify the list of existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is left _None_, a new contact settings item will be created.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlMasterGroups

- Specify the list of master groups.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveGroups

- Specify the list of slave groups.
- The default value is \[].

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
