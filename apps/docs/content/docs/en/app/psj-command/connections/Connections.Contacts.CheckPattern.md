---
title: "Connections.Contacts.CheckPattern()"
description: "Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > Check Pattern"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option.

## Syntax

```psj
Connections.Contacts.CheckPattern(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to be checked.

### `bShowMismatch` @type(Boolean) @default(False)

- Whether to display the part where the mesh pattern does not matches.

### `bShowMatch` @type(Boolean) @default(True)

- Whether to display the part where the mesh pattern matches.

### `dTolerance` @type(Double) @default(0.01)

- The distance between faces to detect the mesh pattern.

## Return Code

Two lists of cursor list: first list contains the entities mesh pattern matched, second list contains the entities mesh pattern isn't match.

## Sample Code

```psj {13}
Geometry.Part.Cube(iPartColor=12276667)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=14511581)

Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)],
                                          crlFaceSlaves=[Face(49)],
                                          dSearchDist=10.0,
                                          dPenaltyFactor=1.0,
                                          iContactColor=16711680)

checking_status = Connections.Contacts.CheckPattern(crlParts=[Part(1, 2)])

JPT.Debugger(checking_status)
```
