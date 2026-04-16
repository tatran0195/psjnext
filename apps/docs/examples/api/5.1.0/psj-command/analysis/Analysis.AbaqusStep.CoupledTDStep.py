# Title:   Analysis.AbaqusStep.CoupledTDStep()
# Desc:    Create Abaqus step for Coupled Temperature-Displacement analysis
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.AbaqusStep.CoupledTDStep
# ---
from os import environ
import re

Geometry.Part.Cube(iPartColor=5619133)
Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=12, 
                     bInternalMeshOnly=False, 
                     iPartColor=65280)
                     
Properties.Material.Add("Concrete", 
                        [Density([(DENSITY, 2.3e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 30000.0), 
                                 (POISSONS_RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)], 
                 strName="Solid Property 1", 
                 iPropertyColor=12275404, 
                 crMaterial=Material(1), 
                 iCordM=-2, 
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL, 
                 dDispHG=DFLT_DBL, 
                 iFLG=-1)

creating_status = Analysis.AbaqusStep.CoupledTDStep(strName="Step1",   # [hl]
                                                    strDesp="Test",   # [hl]
                                                    abaqusPair1=ABAQUS_PAIR(dlTList=[0.0]),   # [hl]
                                                    abaqusPair2=ABAQUS_PAIR(dlTList=[0.0]),   # [hl]
                                                    iMatrixStorage=1,   # [hl]
                                                    iType=2,   # [hl]
                                                    iEnableNlgeom=1,   # [hl]
                                                    iTransient=0,   # [hl]
                                                    listAbaqusOutputRequest=[])  # [hl]

JPT.Debugger(creating_status)
