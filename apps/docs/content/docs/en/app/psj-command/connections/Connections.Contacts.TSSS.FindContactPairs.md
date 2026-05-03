---
title: "Connections.Contacts.TSSS.FindContactPairs()"
description: "Find the contact pairs in model"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > Contacts > TSSS > ContactTable"
---

## Description

Find the contact pairs in model.

## Syntax

```psj
Connections.Contacts.TSSS.FindContactPairs(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to find contact pairs.

### `dFindTolerance` @type(Double) @default(0.001)

- The gap distance in meters between parts to detect contact pairs.

### `dTolForTIED` @type(Double) @default(0.001)

- The gap distance in meters between parts for tied definition. Among the detected contact pairs, the contact pair candidate that is less than the entered tolerance is automatically defined as the tied definition.

### `iSearchArea` @type(Integer) @default(1)

- The search area criteria.
  - 0: Minimum, only faces found with the searching tolerance will take as potential contact pairs
  - 1: Maximum, it will display as a contact pair candidate up to the face that smoothly connects with the searched face

### `bCheckFaceDir` @type(Boolean) @default(False)

- The option used to check face direction.
  - _True_: Check the face direction.
  - _False_: Does not check the face direction.

### `iMasterBasis` @type(Integer) @default(0)

- The contact segment judgment criteria to be the master face of the detected contact pairs.
  - 0: Mesh size, segment group with large element surface area average value
  - 1: Area, segment group with large total area

## Return Code

A _List of pairs_ specifying the found contact pairs.

## Sample Code

```psj {4}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
result = Connections.Contacts.TSSS.FindContactPairs(crlParts=[Part(1, 2, 3)], iSearchArea=0)
JPT.Debugger(result)
```
