---
title: "ContactMSCNastran()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create contact for nastran

## Syntax

```psj
ContactMSCNastran(String m _strName,int iType,int iAlg,double dRROR,double dFNTOL,
    double dFRIC,double dCINTERF,int iISEARCH,int iICOORD,double dFRLIM,double dBIAS,
    int iISTYP,int faceSlave, int faceMaster, int slaveEdge,int masterEdge,
    Cursor[] m _taTarget,Cursor m _crEdit,int m _Color,int m _iMethod)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of contact

<!-- @since:5.0.1 -->
### 2. Int

contact type\[0:General; 1:Tied; 2:Tied & MaIntain Gap; 3:Tied & Full moment; 4:Tied & Full moment & MaIntain Gap]

<!-- @since:5.0.1 -->
### 3. Int

algorithm\[0:face to face]

<!-- @since:5.0.1 -->
### 4. Double

Touching Distance Range

<!-- @since:5.0.1 -->
### 5. Double

Separation Force

<!-- @since:5.0.1 -->
### 6. Double

Friction Coefficient

<!-- @since:5.0.1 -->
### 7. Double

Interference Closure

<!-- @since:5.0.1 -->
### 8. Int

Searching Order\[0:Double; 1:Slave to Master; 2:Program decision]

<!-- @since:5.0.1 -->
### 9. Int

Modify coordinates\[0:None; 1:Modify position; 2:Delay sliding; 3:Both effect]

<!-- @since:5.0.1 -->
### 10. Double

Friction stress limit

<!-- @since:5.0.1 -->
### 11. Double

Tolerance Bias Factor

<!-- @since:5.0.1 -->
### 12. Int

Condition check\[0:Double Side; 1:Optimized]

<!-- @since:5.0.1 -->
### 13. Int

Shell element face Slave\[1:Top\&Btm Thk. offset; 2:Btm w/ Thk. offset; 3:Btm w/o Thk. offset; 4:Top w/ Thk. offset; 5:Top w/o Thk. Offset; 6:Top\&Btm w/o Thk. offset]

<!-- @since:5.0.1 -->
### 14. Int

Shell element face Master\[1:Top\&Btm Thk. offset; 2:Btm w/ Thk. offset; 3:Btm w/o Thk. offset; 4:Top w/ Thk. offset; 5:Top w/o Thk. Offset; 6:Top\&Btm w/o Thk. offset]

<!-- @since:5.0.1 -->
### 15. Int

Beam/Bar Shell Elem. Edge Slave\[1:Beam/Bar Edge only; 10:Free\&Hard Edge only; 11:Both]

<!-- @since:5.0.1 -->
### 16. Int

Beam/Bar Shell Elem. Edge Master\[1:Beam/Bar Edge only; 10:Free\&Hard Edge only; 11:Both]

<!-- @since:5.0.1 -->
### 17. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 18. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 19. Int

contact maker color

<!-- @since:5.0.1 -->
### 20. Int

method type\[0:MANUAL\_FACE; 1:MANUAL\_GROUP; 2:BY\_GROUP\_MATRIX; 3:SHARE\_FACE; 4:AUTO\_SETTING; 5:METHOD\_UNKNOWN]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ContactMSCNastran("ContactMSCNastran _1", 0, 0, 0.0005, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 2147483647, 2147483647, 1.79769e+308, 1.79769e+308, 2147483647,
    0, 0, 0, 0, [79:1-79:2], 0:0, 16711680, 1)
```
