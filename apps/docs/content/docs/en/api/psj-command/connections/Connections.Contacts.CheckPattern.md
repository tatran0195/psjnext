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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to be checked.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bShowMismatch`

- Whether to display the part where the mesh pattern does not matches.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bShowMatch`

- Whether to display the part where the mesh pattern matches.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dTolerance`

- The distance between faces to detect the mesh pattern.

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
