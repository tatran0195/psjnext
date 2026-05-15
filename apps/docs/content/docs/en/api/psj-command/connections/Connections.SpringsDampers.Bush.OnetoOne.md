---
title: "Connections.SpringsDampers.Bush.OnetoOne()"
description: "Create bush connection between target nodes within tolerance."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > SpringsDampers > Bush > OnetoOne"
---

## Description

Create bush connection between target nodes within tolerance.

## Syntax

```psj
Connections.SpringsDampers.Bush.OnetoOne(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 21.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "BUSH\_1".

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 @required -->
### crlMaster

- Specify the target nodes.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iGround

- Specify the ground.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOriMode

- Specify the ori mode.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### poslVector

- Specify the vector.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dlStiffness

- Specify the Stiffness 1 to 6.
- The default value is all DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dlDampCoef

- Specify the Damping Coeff. 1 to 6.
- The default value is all DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dlDampConst

- Specify the Damping Const. 1 to 6.
- The default value is all DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dRotStrain

- Specify the rotation strain.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTransStrain

- Specify the trans strain.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dRotStress

- Specify the rotation stress.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTransStress

- Specify the trans stress.
- The default value is DFLT\_DBL.

<!-- @since:5.1.0 @optional -->
### crlStiffTbl

- Specify the Field Data for the table of Stiffness 1 to 6.
- The default value is all 0:0.

<!-- @since:5.1.0 @optional -->
### crlDampCoefTbl

- Specify the Field Data for the table of Damping Coef. 1 to 6.
- The default value is all 0:0.

<!-- @since:5.1.0 @optional -->
### crlDampConstTbl

- Specify the Field Data for table of Damping Const. 1 to 6.
- The default value is all 0:0.

<!-- @since:5.0.1 @optional -->
### crEditObj

- Specify the edit object.
- The default value is None.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### crlSlave

- Specify the slave.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iEqual

- Specify the equal.
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {4-15}
#Prepare Model
Geometry.Part.Cube(iPartColor=6409934)

Connections.SpringsDampers.Bush.OnetoOne(
    strName="BUSH _1", 
    crlMaster=[Node(4, 25, 1, 9, 8, 89, 5, 73)], 
    dTol=0.01, 
    iOriMode=1,  
    poslVector=[0, 0, 0],    
    dlStiffness=[100.0, 200.0, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    dlDampCoef=[500.0, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    dlDampConst=[0.2, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL],
    crlStiffTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampCoefTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampConstTbl=[Unknown(0, 0, 0, 0, 0, 0)])
```
