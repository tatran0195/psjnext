# Title:   Analysis.AbaqusStep.DynamicStep()
# Desc:    Create Abaqus step for Dynamic analysis
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.AbaqusStep.DynamicStep
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

creating_status = Analysis.AbaqusStep.DynamicStep("Step1",   # [hl]
                                                  iAutomatic=1,   # [hl]
                                                  listOutput=[])  # [hl]

JPT.Debugger(creating_status)
