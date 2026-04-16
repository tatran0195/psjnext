# Title:   Analysis.ADVC.MakeProcess.EigenValue()
# Desc:    Create a Structure - Eigenvalue analysis as an ADVC process
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.ADVC.MakeProcess.EigenValue
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

creating_status = Analysis.ADVC.MakeProcess.EigenValue(strName="Process_0")  # [hl]

JPT.Debugger(creating_status)

Analysis.ADVC.Structure(strPath=environ["Temp"] + \
                                "/TechnoStar/Test.adx", 
                        strName="Job_1", 
                        crlProcessSequence=[ADVCProcessEigen(1)], 
                        crlTargets=[Part(1)], 
                        bAutoAssignDummyProp=True, 
                        crDummyPropMaterial=Material(1), 
                        listLoadNodeContact=[], 
                        iUiPrecision=6, 
                        bExportGeometryID=True)
