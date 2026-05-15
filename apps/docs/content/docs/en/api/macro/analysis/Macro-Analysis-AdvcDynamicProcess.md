---
title: "AdvcDynamicProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC dynamic process

## Syntax

```psj
AdvcDynamicProcess(string m _strName,int m _iGeomNonlinear,int fixed _or _auto,int num _of _inc,
    double max _time,double max _dt,double min _dt,int load _type,int output _last,int output _interval,
    int restart _last,int restart _interval,double output _time _interval,double restart _time _interval,
    bool m _bConvergence,double cg _tol,double cg _nr _tol,double cg _disp _tol,double cg _nr _disp _tol,
    double cg _disp _limit _tol,double cg _total _disp _limit _tol,double newton _tol,double newton _disp _tol,
    double newton _disp _limit _tol,double newton _total _disp _limit _tol,int cgloop _max,int newton _max,
    double ht _nl _loop _tol,int ht _nl _loop _max,bool m _bContact,int subdivide _mode,int contactloop _max,
    int internal _contactloop _max,double separation _tol,double relative _separation _tol,
    double penetration _tol,double relative _penetration _tol,int maxchp,int friction _onset,
    double stick _slip _tol,double friction _tol,int estimate _impact _time,bool m _bAutoIncrement,
    int newton _residue _incr _max,int begin _residue _incr _check,int begin _logarithmic _rate _check,
    double cut _back _factor _for _divergence,double cut _back _factor _for _too _slow _convergence,
    double cut _back _factor _for _excessive _distortion,int incr _enlarge _newton _max,
    int incr _enlarge _suppress,double increase _factor _for _static,double increase _factor _for _dynamic,
    double increase _factor _for _creep,double increase _factor _for _rdnlk,double temperature _incr _max,
    int use _temperature _incr _max,double half _step _tol,double stra _tol,double creep _stra _tol,
    double rdnlk _stra _tol,bool m _bDynamic,double alpha,double beta,double gamma,Cursor m _crEdit,
    list m _LoadNodeList,list m _LoadCaseNodeList,list m _LoadNodeContactList,list m _OutputParamList,
    int m _iRefType,string m _strRefPath,list m _ReferenceResultList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name of ADVC dynamic process

<!-- @since:5.0.1 -->
### 2. Int

Geom nonlinear\[0:blank; 1:Total Lagrange; 2:Updated Lagrange;]

<!-- @since:5.0.1 -->
### 3. Int

Time\[0:Auto; 1:Fixed]

<!-- @since:5.0.1 -->
### 4. Int

Number of increment

<!-- @since:5.0.1 -->
### 5. Double

Max time

<!-- @since:5.0.1 -->
### 6. Double

Max dt

<!-- @since:5.0.1 -->
### 7. Double

Min dt

<!-- @since:5.0.1 -->
### 8. Int

Load type\[-1:default; 0:Step; 1:Ramp]

<!-- @since:5.0.1 -->
### 9. Int

Output last\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 10. Int

Output interval

<!-- @since:5.0.1 -->
### 11. Int

Restart last\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 12. Int

Restart interval

<!-- @since:5.0.1 -->
### 13. Double

Output time interval

<!-- @since:5.0.1 -->
### 14. Double

Restart time interval

<!-- @since:5.0.1 -->
### 15. Bool

If convergence parameter defined

<!-- @since:5.0.1 -->
### 16. Double

cg\_tol

<!-- @since:5.0.1 -->
### 17. Double

cg\_nr\_tol

<!-- @since:5.0.1 -->
### 18. Double

cg\_disp\_tol

<!-- @since:5.0.1 -->
### 19. Double

cg\_nr\_disp\_tol

<!-- @since:5.0.1 -->
### 20. Double

cg\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 21. Double

cg\_total\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 22. Double

newton\_tol

<!-- @since:5.0.1 -->
### 23. Double

newton\_disp\_tol

<!-- @since:5.0.1 -->
### 24. Double

newton\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 25. Double

newton\_total\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 26. Int

cgloop\_max

<!-- @since:5.0.1 -->
### 27. Int

newton\_max

<!-- @since:5.0.1 -->
### 28. Double

ht\_nl\_loop\_tol

<!-- @since:5.0.1 -->
### 29. Int

ht\_nl\_loop\_max

<!-- @since:5.0.1 -->
### 30. Bool

If contact parameter defined

<!-- @since:5.0.1 -->
### 31. Int

subdivide\_mode\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 32. Int

contactloop\_max

<!-- @since:5.0.1 -->
### 33. Int

internal\_contactloop\_max

<!-- @since:5.0.1 -->
### 34. Double

separation\_tol

<!-- @since:5.0.1 -->
### 35. Double

relative\_separation\_tol

<!-- @since:5.0.1 -->
### 36. Double

penetration\_tol

<!-- @since:5.0.1 -->
### 37. Double

relative\_penetration\_tol

<!-- @since:5.0.1 -->
### 38. Int

maxchp

<!-- @since:5.0.1 -->
### 39. Int

friction\_onset\[0:delayd; 1:immediate]

<!-- @since:5.0.1 -->
### 40. Double

stick\_slip\_tol

<!-- @since:5.0.1 -->
### 41. Double

friction\_tol

<!-- @since:5.0.1 -->
### 42. Int

estimate\_impact\_time\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 43. Bool

If auto increment parameter defined

<!-- @since:5.0.1 -->
### 44. Int

newton\_residue\_incr\_max

<!-- @since:5.0.1 -->
### 45. Int

begin\_residue\_incr\_check

<!-- @since:5.0.1 -->
### 46. Int

begin\_logarithmic\_rate\_check

<!-- @since:5.0.1 -->
### 47. Double

cut\_back\_factor\_for\_divergence

<!-- @since:5.0.1 -->
### 48. Double

cut\_back\_factor\_for\_too\_slow\_convergence

<!-- @since:5.0.1 -->
### 49. Double

cut\_back\_factor\_for\_excessive\_distortion

<!-- @since:5.0.1 -->
### 50. Int

incr\_enlarge\_newton\_max

<!-- @since:5.0.1 -->
### 51. Int

incr\_enlarge\_suppress

<!-- @since:5.0.1 -->
### 52. Double

increase\_factor\_for\_static

<!-- @since:5.0.1 -->
### 53. Double

increase\_factor\_for\_dynamic

<!-- @since:5.0.1 -->
### 54. Double

increase\_factor\_for\_creep

<!-- @since:5.0.1 -->
### 55. Double

increase\_factor\_for\_rdnlk

<!-- @since:5.0.1 -->
### 56. Double

temperature\_incr\_max

<!-- @since:5.0.1 -->
### 57. Int

use\_temperature\_incr\_max\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 58. Double

half\_step\_tol

<!-- @since:5.0.1 -->
### 59. Double

stra\_tol

<!-- @since:5.0.1 -->
### 60. Double

creep\_stra\_tol

<!-- @since:5.0.1 -->
### 61. Double

rdnlk\_stra\_tol

<!-- @since:5.0.1 -->
### 62. Bool

If dynamic parameter defined

<!-- @since:5.0.1 -->
### 63. Double

Alpha

<!-- @since:5.0.1 -->
### 64. Double

Beta

<!-- @since:5.0.1 -->
### 65. Double

Gamma

<!-- @since:5.0.1 -->
### 66. Cursor

Edit cursor

<!-- @since:5.0.1 -->
### 67. List

Status of Loads

<!-- @since:5.0.1 -->
### 68. List

Status of Load Cases

<!-- @since:5.0.1 -->
### 69. List

Status and other data of Contacts

<!-- @since:5.0.1 -->
### 70. List

Output parameters

<!-- @since:5.0.1 -->
### 71. Int

Reference result type\[0:Temperature Load; 1:Stress]

<!-- @since:5.0.1 -->
### 72. String

Path of reference result

<!-- @since:5.0.1 -->
### 73. List

Data of reference result

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcDynamicProcess("Test",1,1,1,0.001,0.001,0.001,1,1,1,1,1,0.001,0.001,1,0.001,
    0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,1,1,0.001,1,1,1,1,1,0.001,
    0.001,0.001,0.001,1,1,0.001,0.001,1,1,1,1,1,0.001,0.001,0.001,1,1,0.001,0.001,
    0.001,0.001,0.001,1,0.001,0.001,0.001,0.001,1,0.001,0.001,0.001,1:11,,,,,1,"Test",)
```
