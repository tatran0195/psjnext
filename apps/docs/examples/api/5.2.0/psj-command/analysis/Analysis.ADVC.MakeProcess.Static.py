# Title:   Analysis.ADVC.MakeProcess.Static()
# Desc:    Create ADVC Structure Static process for analysis work. This process could be created in one time or multiple times
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.ADVC.MakeProcess.Static
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

creating_status = Analysis.ADVC.MakeProcess.Static(strName="Process_0",   # [hl]
                                                   advcStructTimeStep=ADVC_STRUCT_TIME_STEP(iNumOfInc=10),   # [hl]
                                                   dStabilizationFactor=DFLT_DBL,   # [hl]
                                                   listLoadNode=[],   # [hl]
                                                   listLoadCaseNode=[],   # [hl]
                                                   listLoadNodeContact=[],   # [hl]
                                                   listAdvcRefStressResult=[])  # [hl]

JPT.Debugger(creating_status)

Analysis.ADVC.Structure(strPath=environ["Temp"] + \
                                "/TechnoStar/Test.adx", 
                        strName="Job_1", 
                        crlProcessSequence=[ADVCProcessStatic(1)], 
                        crlTargets=[Part(1)], 
                        bAutoAssignDummyProp=True, 
                        listLoadNodeContact=[], 
                        iUiPrecision=6, 
                        bExportGeometryID=True)
