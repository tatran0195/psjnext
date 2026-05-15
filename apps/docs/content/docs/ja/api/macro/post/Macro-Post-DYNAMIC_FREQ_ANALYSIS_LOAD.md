---
title: "DYNAMIC _FREQ _ANALYSIS _LOAD()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Load for Frequency response analysis

## Syntax

```psj
DYNAMIC _FREQ _ANALYSIS _LOAD(int AnalysisType, cursor ParentAnalysis, cursor	Coord, string Name, int LoadPtn, vector Force, 
donble Amplitude,double Delay, double Phase, bool Bf, double Bf, cursor BfCurve, bool Ff, double Ff, cursor FfCurve, bool UnitLoad, 
bool CentripetalForce, cursor[] Target, cursor Edit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Analysis type

<!-- @since:5.0.1 -->
### 2. int

Parent analysis

<!-- @since:5.0.1 -->
### 3. cursor

Coordinate

<!-- @since:5.0.1 -->
### 4. string

Load Name

<!-- @since:5.0.1 -->
### 5. int

Direction
0: X
1: Y
2: Z
3: RX
4: RY
5: RZ
6: Normal

<!-- @since:5.0.1 -->
### 6. vector

Force direction in vector format.

<!-- @since:5.0.1 -->
### 7. double

Amplitude

<!-- @since:5.0.1 -->
### 8. double

Delay

<!-- @since:5.0.1 -->
### 9. double

Phase

<!-- @since:5.0.1 -->
### 10. bool

Check flag of B(f) table input

<!-- @since:5.0.1 -->
### 11. double

B(f) value without table = 1.0

<!-- @since:5.0.1 -->
### 12. cursor

Cursor to B(f) table

<!-- @since:5.0.1 -->
### 13. bool

Check flag of F(f) table input

<!-- @since:5.0.1 -->
### 14. double

F(f) value without table = 0.0

<!-- @since:5.0.1 -->
### 15. cursor

Cursor to F(f) table

<!-- @since:5.0.1 -->
### 16. bool

Unit Load flag

<!-- @since:5.0.1 -->
### 17. bool

mr\*omega^2 flag

<!-- @since:5.0.1 -->
### 18. cursor\[]

Target nodes

<!-- @since:5.0.1 -->
### 12. cursor

Target Load when modify

## Return Code

Nothing.

## Sample Code

```psj
DYNAMIC _FREQ _ANALYSIS _LOAD(0, 0:0, 0:0, "FRQLOAD10", 2, [0, 0, 1], 1, 1, 1, 0, 1, 0:0, 0, 0, 0:0, 0, 0, [10:9513], 0:0)
```
