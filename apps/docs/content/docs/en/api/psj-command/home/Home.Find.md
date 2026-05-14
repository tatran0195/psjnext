---
title: "Home.Find()"
description: "Search entities in Jupiter by using their IDs or names"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > Find"
---

## Description

Search entities in Jupiter by using their IDs or names.

## Syntax

```psj
Home.Find(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strSearch`

- The search ID or name of the target you want to search.

<!-- @since:5.0.1 @type:String @optional @default:"Part" -->
### `strSelectedType`

- The searching type. The searching type is one of the following.
  - "Part": Part Search.
  - "Face": Face Search.
  - "Edge": Edge Search.
  - "Vertex": Vertex Search.
  - "3D Element": 3D Element Search.
  - "2D Element": 2D Element Search.
  - "1D Element": 1D Element Search.
  - "Node": Node Search.
  - "Group": Group Search.
  - "Force": Force Search.
  - "Pressure": Pressure Search.
  - "Constraint": Constraint Search.
  - "DoF Set": DoF Set Search.
  - "Centrifugal Force": Centrifugal Force Search.
  - "Gravity": Gravity Search.
  - "Weld": Weld Search.
  - "Connection": Connection Search.
  - "Contact": Contact Search.
  - "Coordinate": Coordinate Search.
  - "Local Mesh Settings": Local Mesh Settings Search.
  - "Property": Property Search.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFindMatch`

- The enables/disables the find matching option. if this option is turned on, the _strSearch_ need to match the whole string.

## Return Code

A _List of Cursor_ specifying all found entities.

## Sample Code

```psj {8-11}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01,
                             0.0,
                             0.0],
                   strName="Cube _2",
                   iPartColor=6409934)

find _name = Home.Find(strSearch="cube")
find _name _match = Home.Find(strSearch="cube _2",
                            bFindMatch=True)
find _id = Home.Find(strSearch="1")

JPT.Debugger(find _name)

JPT.Debugger(find _name _match)

JPT.Debugger(find _id)
```
