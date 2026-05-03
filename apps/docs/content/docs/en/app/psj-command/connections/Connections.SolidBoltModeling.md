---
title: "Connections.SolidBoltModeling()"
description: "Create a solid bolt composed of hexa elements."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > SolidBoltModeling"
macro_link: ""
---

## Description

Create a solid bolt composed of hexa elements.

## Syntax

```psj
Connections.SolidBoltModeling(...)
```

## Inputs

### `crlTopTargets` @type(List\[Cursor]) @required

- Top side edges or faces.

### `crlBottomTargets` @type(List\[Cursor]) @required

- Bottom side edges or faces.

### `strName` @type(String) @default("Bolt\_1")

- The name of created bolt connection.

### `iBoltType` @type(Integer) @default(0)

- Bolt type.
  - 0: Bolt - Nut
  - 1: Bolt

### `dMaxHeight` @type(Double) @default(100)

- The maximum length of bolt hole where a new bolt is created.

### `dMaxDiameter` @type(Double) @default(36)

- The maximum diameter to search bolt hole.

### `dMinDiameter` @type(Double) @default(3)

- The minimum diameter to search bolt hole.

### `bPretension` @type(Boolean) @default(False)

- Whether or not create pretension setting.

### `iSolverType` @type(Integer) @default(0)

- Solver type.
  - 0: All
  - 1: Abaqus

### `iForceUnit` @type(Integer) @default(0)

- Unit of pretension force.
  - 0: N
  - 1: mN
  - 2: kN
  - 3: kgf
  - 4: lbf
  - 5: tf

### `dPretensionValue` @type(Double) @default(100)

- The value of pretension force.

### `iDirection` @type(Integer) @default(0)

- Force direction.
  - 0: UX
  - 1: UY
  - 2: UZ

### `crCoord` @type(Cursor) @default(None)

- Coordinate for force direction.

### `bFixLength` @type(Boolean) @default(False)

- Whether or not create fixed length setting.

### `dDiameter` @type(Double) @default(4)

- Nominal thread diameter of the created bolt.

### `dBoltHeadWidthAcrossFlat` @type(Double) @default(7)

- The bolt head diagonal distance.

### `dBoltHeadHeight` @type(Double) @default(2.8)

- Bolt head height.

### `dShaftLength` @type(Double) @default(40)

- Bolt shaft length.

### `dPitch` @type(Double) @default(5)

- Bolt thread length.

### `iTopHeadHeightDivision` @type(Integer) @default(1)

- The number of mesh divisions in the top side of bolt head height direction.

### `iTopHeadRadialDivision` @type(Integer) @default(1)

- The number of mesh divisions in the radial direction of the bolt head circumference.

### `dNutWidthAcrossFlat` @type(Double) @default(7)

- The bolt nut diagonal distance.

### `dNutHeight` @type(Double) @default(3.2)

- Bolt nut height.

### `iBotHeadHeightDivision` @type(Integer) @default(1)

- The number of mesh divisions in the bolt head height direction.

### `iBotHeadRadialDivision` @type(Integer) @default(1)

- The number of mesh divisions in the radial direction of the top side of bolt head circumference.

## Return Code

A _List of Cursor_ specifying created solid bolt parts.

## Sample Code

```psj {48-60}
##################
# Prepare model
##################

# Create a cube
cube=Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    strName="Cube_3", 
    iPartColor=6409934)

# Get top face
maxface=JPT.Exec(f'FindFacesInPart({cube},"MaxZFACE")')

# Imprint circle on the top face.
Geometry.Edge.Circle(
    veclPositions=[[0.005, 0.005, 0.01]], 
    crlTargetFace=maxface, 
    dOutRadius=2.0, 
    iNoOfDiv=8)

# Get newly created edge - > top edge.
edge1=JPT.GetMaxIDEntity(JPT.DItemType.EDGE)

# Delete newly created face.
face=JPT.GetMaxIDEntity(JPT.DItemType.FACE)
JPT.Exec(f'DeleteFace([{face}], 1)')

# Get bottom face
minface=JPT.Exec(f'FindFacesInPart({cube},"MinZFACE")')

# Imprint circle on the bottom face.
Geometry.Edge.Circle(
    veclPositions=[[0.005, 0.005, 0.0]], 
    crlTargetFace=minface, 
    dOutRadius=2.0, 
    iNoOfDiv=8)
# Get newly created edge - > bottom edge.
edge2=JPT.GetMaxIDEntity(JPT.DItemType.EDGE)

# Delete newly created face.
face=JPT.GetMaxIDEntity(JPT.DItemType.FACE)
JPT.Exec(f'DeleteFace([{face}], 1)')

# Create side face of bolt hole.
Geometry.Face.Edges(crlEdges=[Edge(edge1, edge2)])

# Create a solid bolt at the hole.
Connections.SolidBoltModeling(
    crlTopTargets=[Edge(edge1)], 
    crlBottomTargets=[Edge(edge2)], 
    strName="Bolt_1", iBoltType=1, 
    dMaxHeight=10,     
    dDiameter=3, 
    dBoltHeadWidthAcrossFlat=5.5,
    dBoltHeadHeight=2, 
    dShaftLength=10, 
    dPitch=1, 
    iTopHeadHeightDivision=2,
    iTopHeadRadialDivision=2)
```
