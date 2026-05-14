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

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTopTargets`

- The top side edges or faces.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlBottomTargets`

- The bottom side edges or faces.

<!-- @since:5.1.0 @type:String @optional @default:"Bolt _1" -->
### `strName`

- The name of created bolt connection.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBoltType`

- The bolt type.
  - 0: Bolt - Nut
  - 1: Bolt

<!-- @since:5.1.0 @type:Double @optional @default:100 -->
### `dMaxHeight`

- The maximum length of bolt hole where a new bolt is created.

<!-- @since:5.1.0 @type:Double @optional @default:36 -->
### `dMaxDiameter`

- The maximum diameter to search bolt hole.

<!-- @since:5.1.0 @type:Double @optional @default:3 -->
### `dMinDiameter`

- The minimum diameter to search bolt hole.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bPretension`

- Whether or not create pretension setting.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSolverType`

- The solver type.
  - 0: All
  - 1: Abaqus

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iForceUnit`

- The unit of pretension force.
  - 0: N
  - 1: mN
  - 2: kN
  - 3: kgf
  - 4: lbf
  - 5: tf

<!-- @since:5.1.0 @type:Double @optional @default:100 -->
### `dPretensionValue`

- The value of pretension force.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDirection`

- The force direction.
  - 0: UX
  - 1: UY
  - 2: UZ

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate for force direction.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFixLength`

- Whether or not create fixed length setting.

<!-- @since:5.1.0 @type:Double @optional @default:4 -->
### `dDiameter`

- The nominal thread diameter of the created bolt.

<!-- @since:5.1.0 @type:Double @optional @default:7 -->
### `dBoltHeadWidthAcrossFlat`

- The bolt head diagonal distance.

<!-- @since:5.1.0 @type:Double @optional @default:2.8 -->
### `dBoltHeadHeight`

- The bolt head height.

<!-- @since:5.1.0 @type:Double @optional @default:40 -->
### `dShaftLength`

- The bolt shaft length.

<!-- @since:5.1.0 @type:Double @optional @default:5 -->
### `dPitch`

- The bolt thread length.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTopHeadHeightDivision`

- The number of mesh divisions in the top side of bolt head height direction.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTopHeadRadialDivision`

- The number of mesh divisions in the radial direction of the bolt head circumference.

<!-- @since:5.1.0 @type:Double @optional @default:7 -->
### `dNutWidthAcrossFlat`

- The bolt nut diagonal distance.

<!-- @since:5.1.0 @type:Double @optional @default:3.2 -->
### `dNutHeight`

- The bolt nut height.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iBotHeadHeightDivision`

- The number of mesh divisions in the bolt head height direction.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iBotHeadRadialDivision`

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
