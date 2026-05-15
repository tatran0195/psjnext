---
title: "Connections.Contacts.CheckPattern()"
description: "Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Check Pattern"
---

## Description

Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option.

## Syntax

```psj
Connections.Contacts.CheckPattern(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the parts to be checked.

<!-- @since:5.0.1 @optional -->
### bShowMismatch

- Specify whether to display the part where the mesh pattern does not matches.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bShowMatch

- Specify whether to display the part where the mesh pattern matches.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the distance between faces to detect the mesh pattern.
- The default value is 0.01.

## Return Code

Two lists of cursor list: first list contains the entities mesh pattern matched, second list contains the entities mesh pattern isn't match.

## Sample Code

```psj {13}
Geometry.Part.Cube(iPartColor=12276667)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=14511581)

Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)],
                                          crlFaceSlaves=[Face(49)],
                                          dSearchDist=10.0,
                                          dPenaltyFactor=1.0,
                                          iContactColor=16711680)

checking _status = Connections.Contacts.CheckPattern(crlParts=[Part(1, 2)])

JPT.Debugger(checking _status)
```
