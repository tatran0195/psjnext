---
title: Unit Types
id: unit-types
---

This is an enumeration type represents units used in Jupiter.
Functions used for unit conversion:

- [`JPT.ConvertFromDocUnit`](../../../../psj-utility/JPT.ConvertFromDocUnit): Convert the inputted value from the current Jupiter unit system to SI[m] unit.
- [`JPT.ConvertFromMacroUnit`](../../../../psj-utility/JPT.ConvertFromMacroUnit): Convert the inputted value from the specified unit to the SI[m] unit.
- [`JPT.ConvertValueToDocUnit`](../../../../psj-utility/JPT.ConvertValueToDocUnit): Convert the inputted value from SI[m] units to the current Jupiter unit system.
- [`JPT.ConvertValueToMacroUnit`](../../../../psj-utility/JPT.ConvertValueToMacroUnit): Convert the inputted value from the SI[m] unit to the specified unit.

> For more information, refer to [Convert Unit tutorial](../../../../tutorials/basic/convert-unit)

| ID  | Unit Type                                    | Description                     | String Unit                                                                                |
| --- | -------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------ |
| 0   | `JPT.UnitType.Unit_Length`                   | Length                          | $mm\\m\\ft\\in\\cm$                                                                        |
| 1   | `JPT.UnitType.Unit_Time`                     | Time                            | $s\\min\\h$                                                                                |
| 2   | `JPT.UnitType.Unit_Mass`                     | Mass                            | $t\\kg\\kgf*s^2/mm\\slug\\lbf*s^2/in\\lb\\g$                                               |
| 3   | `JPT.UnitType.Unit_Force`                    | Force                           | $N\\mN\\kN\\kgf\\lbf\\tf$                                                                  |
| 4   | `JPT.UnitType.Unit_Angle`                    | Angle                           | $deg\\rad$                                                                                 |
| 5   | `JPT.UnitType.Unit_Temperature`              | Temperature                     | $K\\deg C\\deg F$                                                                          |
| 6   | `JPT.UnitType.Unit_Area`                     | Area                            | $mm^2\\m^2\\ft^2\\in^2\\cm^2$                                                              |
| 7   | `JPT.UnitType.Unit_Volume`                   | Volume                          | $mm^3\\m^3\\ft^3\\in^3\\cm^3$                                                              |
| 8   | `JPT.UnitType.Unit_Velocity`                 | Velocity                        | $mm/s\\m/s\\ft/s\\in/s$                                                                    |
| 9   | `JPT.UnitType.Unit_Acceleration`             | Acceleration                    | $mm/s^2\\m/s^2\\ft/s^2\\in/s^2\\g\\Gal$                                                    |
| 10  | `JPT.UnitType.Unit_RotateVelo`               | Rotational velocity             | $rad/s\\deg/s\\rpm$                                                                        |
| 11  | `JPT.UnitType.Unit_RotateAcc`                | Rotational acceleration         | $rad/s^2\\deg/s^2$                                                                         |
| 12  | `JPT.UnitType.Unit_Moment`                   | Moment                          | $N*mm\\N*m\\mN*mm\\kgf*mm\\lbf*ft\\lbf*in\\tf*m$                                           |
| 13  | `JPT.UnitType.Unit_Pressure`                 | Pressure                        | $MPa\\Pa\\kPa\\kgf/mm^2\\lbf/ft^2\\lbf/in^2\\tf/m^2\\GPa$                                  |
| 14  | `JPT.UnitType.Unit_Density`                  | Density                         | $t/mm^3\\kg/m^3\\kg/mm^3\\kgf*s^2/mm^4\\slug/ft^3\\lbf*s^2/in^4$                           |
| 15  | `JPT.UnitType.Unit_Stiffness`                | Stiffness                       | $N/mm\\N/m\\mN/mm\\kgf/mm\\lbf/ft\\lbf/in$                                                 |
| 16  | `JPT.UnitType.Unit_RotateStiff`              | Rotational stiffness            | $N*mm/rad\\N*m/rad\\mN*mm/rad\\kgf*mm/rad\\lbf*ft/rad\\lbf*in/rad\\N*mm/deg\\mN*mm/deg$    |
| 17  | `JPT.UnitType.Unit_DampingCoef`              | Damping coefficient             | $N*s/mm\\N*s/m\\mN*s/mm\\kgf*s/mm\\lbf*s/ft\\lbf*s/in$                                     |
| 18  | `JPT.UnitType.Unit_RotateDampingCoef`        | Rotational damping coefficient  | $N*mm*s/rad\\N*m*s/rad\\mN*mm*s/rad\\kgf*mm*s/rad\\lbf*ft*s/rad\\lbf*in*s/rad\\N*mm*s/deg$ |
| 19  | `JPT.UnitType.Unit_Modulus`                  | Elastic modulus                 | $N/mm^2\\N/m^2\\mN/mm^2\\kgf/mm^2\\lbf/ft^2\\lbf/in^2$                                     |
| 20  | `JPT.UnitType.Unit_Energy`                   | Energy                          | $mJ\\J\\miuJ\\kcal\\ft*lbf\\in*lbf\\kJ\\cal$                                               |
| 21  | `JPT.UnitType.Unit_Power`                    | Power                           | $mW\\W\\miuW\\kcal/s\\ft*lbf/s\\in*lbf/s$                                                  |
| 22  | `JPT.UnitType.Unit_ThermalExCoef`            | Coefficient of linear expansion | $/K$                                                                                       |
| 23  | `JPT.UnitType.Unit_ThermalConductivity`      | Thermal conductivity            | $mW/mm*K\\W/m*K\\miuW/mm*K\\kcal/mm*h*K\\lbf/ft*s*K\\lbf/in*s*K$                           |
| 24  | `JPT.UnitType.Unit_ConvectionCoef`           | Convection coefficient          | $mW/mm^2*K\\W/m^2*K\\miuW/mm^2*K\\kcal/mm^2*h*K\\lbf/ft*s*K\\lbf/in*s*K$                   |
| 25  | `JPT.UnitType.Unit_SpecificHeat`             | Specific heat                   | $mJ/t*K\\J/kg*K\\miuJ/kg*K\\kcal/kg*K\\ft*lbf/slug*K\\in^2/s^2*K$                          |
| 26  | `JPT.UnitType.Unit_HeatFlux`                 | Heat flux                       | $mW/mm^2\\W/m^2\\miuW/mm^2\\kcal/mm^2*h\\lbf/ft*s\\lbf/in*s$                               |
| 27  | `JPT.UnitType.Unit_HeatGeneration`           | Heat generation                 | $mW/mm^3\\W/m^3\\miuW/mm^3\\kcal//mm^3*h\\lbf/ft^2*s\\lbf/in^2*s$                          |
| 28  | `JPT.UnitType.Unit_LinearDensity`            | Linear density                  | $kg/m\\oz/ft\\oz/in\\lb/yd$                                                                |
| 29  | `JPT.UnitType.Unit_SurfaceDensity`           | Surface density                 |
| 30  | `JPT.UnitType.Unit_AreaMomentInertia`        | Moment of Inertia (Area)        | $mm^4\\m^4\\ft^4\\in^4\\cm^4$                                                              |
| 31  | `JPT.UnitType.Unit_TorsionalConst`           | Torsional rigidity              | $mm^4\\m^4\\ft^4\\in^4\\cm^4$                                                              |
| 32  | `JPT.UnitType.Unit_WarpCoef`                 | Warping factor                  | $mm^6\\m^6\\ft^6\\in^6\\cm^6$                                                              |
| 33  | `JPT.UnitType.Unit_LinearMassMomentIntertia` | Mass moment of inertia          | $t*mm\\kg*m\\kg*mm\\kgf*s^2\\slug*ft\\lbf*s^2$                                             |
| 34  | `JPT.UnitType.Unit_MomentInertia`            | Inertia (Area) moment           | $t*mm^2\\kg*m^2\\kg*mm^2\\kgf*mm*s^2\\slug*ft^2\\lbf*in*s^$                                |
| 35  | `JPT.UnitType.Unit_Stress`                   | Stress                          | $N/mm^2\\N/m^2\\mN/mm^2$                                                                   |
| 36  | `JPT.UnitType.Unit_Strain`                   | Strain                          | $N-m\\N-mm$                                                                                |
| 37  | `JPT.UnitType.Unit_StrainEnergy`             | Strain energy                   | $N-mm\\N-m$                                                                                |
| 38  | `JPT.UnitType.Unit_ThermalEnergy`            | Thermal energy                  | $J\\mJ\\cal$                                                                               |
| 39  | `JPT.UnitType.Unit_Frequency`                | Frequency                       | $Hz$                                                                                       |
| 40  | `JPT.UnitType.Unit_VolumeEnergyDensity`      | Volume energy density           | $J/mm^3\\J/m^3\\mJ/mm^3$                                                                   |
| 41  | `JPT.UnitType.Unit_ElectricalResistivity`    | Electrical resistivity          | $Ohm-mm\\Ohm-m$                                                                            |
| 42  | `JPT.UnitType.Unit_StressReciprocal`         | Stress Reciprocal               | $Ohm-mm\\Ohm-m$                                                                            |
| 43  | `JPT.UnitType.Unit_ThermalRadiation`         | Thermal radiation               | $mm^2/N\\m^2/N\\mm^2/mN$                                                                   |
| 44  | `JPT.UnitType.Unit_Displacement`             | Displacement                    | $mm^2/N\\m^2/N\\mm^2/mN$                                                                   |
| 45  | `JPT.UnitType.Unit_EnergyDensity`            | Energy density                  | $mJ/mm^3\\J/m^3\\Kcal/mm^3$                                                                |
| 46  | `JPT.UnitType.Unit_TemperatureGradient`      | Temperature gradient            | $K/m\\K/mm$                                                                                |
| 47  | `JPT.UnitType.Unit_Current`                  | Current                         | $A\\mA\\uA\\kA$                                                                            |
| 48  | `JPT.UnitType.Unit_Voltage`                  | Current                         | $V\\mV\\uV\\kV$                                                                            |
