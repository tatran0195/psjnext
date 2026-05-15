---
title: "Connections.Contacts.TSSS.FindContactPairs()"
description: "Find the contact pairs in model"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > Contacts > TSSS > ContactTable"
---

## Description

Find the contact pairs in model.

## Syntax

```psj
Connections.Contacts.TSSS.FindContactPairs(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlParts

- Specify the parts to find contact pairs.

<!-- @since:5.1.0 @optional -->
### dFindTolerance

- Specify the gap distance in meters between parts to detect contact pairs.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### dTolForTIED

- Specify the gap distance in meters between parts for tied definition. Among the detected contact pairs, the contact pair candidate that is less than the entered tolerance is automatically defined as the tied definition.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### iSearchArea

- Specify the search area criteria.
  - 0: Minimum, only faces found with the searching tolerance will take as potential contact pairs
  - 1: Maximum, it will display as a contact pair candidate up to the face that smoothly connects with the searched face
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bCheckFaceDir

- Specify the option used to check face direction.
  - _True_: Check the face direction.
  - _False_: Does not check the face direction.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iMasterBasis

- Specify the contact segment judgment criteria to be the master face of the detected contact pairs.
  - 0: Mesh size, segment group with large element surface area average value
  - 1: Area, segment group with large total area
- The default value is 0.

## Return Code

A _List of pairs_ specifying the found contact pairs.

## Sample Code

```psj {4}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
result = Connections.Contacts.TSSS.FindContactPairs(crlParts=[Part(1, 2, 3)], iSearchArea=0)
JPT.Debugger(result)
```
