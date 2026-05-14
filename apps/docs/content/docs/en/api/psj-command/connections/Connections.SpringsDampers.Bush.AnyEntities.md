---
title: "Connections.SpringsDampers.Bush.AnyEntities()"
description: "Create bush connection between nodes in target entities."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > SpringsDampers > Bush > AnyEntities"
---

## Description

Create bush connection between nodes in target entities.

## Syntax

```psj
Connections.SpringsDampers.Bush.AnyEntities(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:16 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:String @optional @default:"BUSH _1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
<!-- @since:5.1.0 @required -->
### `crlMaster`

- The master.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
<!-- @since:5.1.0 @required -->
### `crlSlave`

- The slave.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGround`

- The ground.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOriMode`

- The ori mode.

<!-- @since:5.0.1 @type:Position List @optional @default:[] -->
### `poslVector`

- The vector.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
<!-- @since:5.1.0 @default:all DFLT _DBL -->
### `dlStiffness`

- The Stiffness 1 to 6.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
<!-- @since:5.1.0 @default:all DFLT _DBL -->
### `dlDampCoef`

- The Damping Coeff. 1 to 6.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
<!-- @since:5.1.0 @default:all DFLT _DBL -->
### `dlDampConst`

- The Damping Const. 1 to 6.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRotStrain`

- The rotation strain.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTransStrain`

- The trans strain.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRotStress`

- The rotation stress.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTransStress`

- The trans stress.

<!-- @since:5.1.0 @type:Lits of Cursor @optional @default:all 0:0 -->
### `crlStiffTbl`

- The Field Data for the table of Stiffness 1 to 6.

<!-- @since:5.1.0 @type:Lits of Cursor @optional @default:all 0:0 -->
### `crlDampCoefTbl`

- The Field Data for the table of Damping Coef. 1 to 6.

<!-- @since:5.1.0 @type:Lits of Cursor @optional @default:all 0:0 -->
### `crlDampConstTbl`

- The Field Data for table of Damping Const. 1 to 6.
-

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEditObj`

- The edit object.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:DFLT _DBL -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEqual`

- The equal.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {4-15}
#Prepare Model
Geometry.Part.Cube(iPartColor=6409934)

Connections.SpringsDampers.Bush.AnyEntities(
    strName="BUSH _1", 
    crlMaster=[Edge(18)], 
    crlSlave=[Edge(10)], 
    iOriMode=1, 
    poslVector=[0, 0, 0], 
    dlStiffness=[100.0, 200.0, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    dlDampCoef=[500.0, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    dlDampConst=[0.2, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL],
    crlStiffTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampCoefTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampConstTbl=[Unknown(0, 0, 0, 0, 0, 0)])
```
