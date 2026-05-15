---
title: "Connections.SolidBoltModeling()"
description: "Create a solid bolt composed of hexa elements."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > SolidBoltModeling"
macro _link: ""
---

## Description

Create a solid bolt composed of hexa elements.

## Syntax

```psj
Connections.SolidBoltModeling(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTopTargets

- Specify top side edges or faces.

<!-- @since:5.1.0 @required -->
### crlBottomTargets

- Specify bottom side edges or faces.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of created bolt connection.
- The default value is "Bolt\_1".

<!-- @since:5.1.0 @optional -->
### iBoltType

- Specify bolt type.
  - 0: Bolt - Nut
  - 1: Bolt
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dMaxHeight

- Specify the maximum length of bolt hole where a new bolt is created.
- The default value is 100.

<!-- @since:5.1.0 @optional -->
### dMaxDiameter

- Specify the maximum diameter to search bolt hole.
- The default value is 36.

<!-- @since:5.1.0 @optional -->
### dMinDiameter

- Specify the minimum diameter to search bolt hole.
- The default value is 3.

<!-- @since:5.1.0 @optional -->
### bPretension

- Specify whether or not create pretension setting.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iSolverType

- Specify solver type.
  - 0: All
  - 1: Abaqus
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iForceUnit

- Specify unit of pretension force.
  - 0: N
  - 1: mN
  - 2: kN
  - 3: kgf
  - 4: lbf
  - 5: tf
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dPretensionValue

- Specify the value of pretension force.
- The default value is 100.

<!-- @since:5.1.0 @optional -->
### iDirection

- Specify force direction.
  - 0: UX
  - 1: UY
  - 2: UZ
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crCoord

- Specify coordinate for force direction.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bFixLength

- Specify whether or not create fixed length setting.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dDiameter

- Specify nominal thread diameter of the created bolt.
- The default value is 4.

<!-- @since:5.1.0 @optional -->
### dBoltHeadWidthAcrossFlat

- Specify the bolt head diagonal distance.
- The default value is 7.

<!-- @since:5.1.0 @optional -->
### dBoltHeadHeight

- Specify bolt head height.
- The default value is 2.8.

<!-- @since:5.1.0 @optional -->
### dShaftLength

- Specify bolt shaft length.
- The default value is 40.

<!-- @since:5.1.0 @optional -->
### dPitch

- Specify bolt thread length.
- The default value is 5.

<!-- @since:5.1.0 @optional -->
### iTopHeadHeightDivision

- Specify the number of mesh divisions in the top side of bolt head height direction.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTopHeadRadialDivision

- Specify the number of mesh divisions in the radial direction of the bolt head circumference.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dNutWidthAcrossFlat

- Specify the bolt nut diagonal distance.
- The default value is 7.

<!-- @since:5.1.0 @optional -->
### dNutHeight

- Specify bolt nut height.
- The default value is 3.2.

<!-- @since:5.1.0 @optional -->
### iBotHeadHeightDivision

- Specify the number of mesh divisions in the bolt head height direction.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iBotHeadRadialDivision

- Specify the number of mesh divisions in the radial direction of the top side of bolt head circumference.
- The default value is 1.

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
    strName="Cube _3", 
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
    strName="Bolt _1", iBoltType=1, 
    dMaxHeight=10,     
    dDiameter=3, 
    dBoltHeadWidthAcrossFlat=5.5,
    dBoltHeadHeight=2, 
    dShaftLength=10, 
    dPitch=1, 
    iTopHeadHeightDivision=2,
    iTopHeadRadialDivision=2)
```
