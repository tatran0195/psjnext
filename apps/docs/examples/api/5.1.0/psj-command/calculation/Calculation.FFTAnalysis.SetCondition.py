# Title:   Calculation.FFTAnalysis.SetCondition()
# Desc:    Perform a FFT analysis
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FFTAnalysis.SetCondition
# ---
# Please set path to your sample file.
filePath="C:/Temp/Sample..."

# Prepare result model
Home.ImportResults.ADVC(filePath, iImportType=1, dFaceAngle=60, dEdgeAngle=60)

# Set FFT condition
FFTCondition = Calculation.FFTAnalysis.SetCondition(crlTargets=[Elem(...)], crl2DElems=[Elem(...)],   # [hl:start]
                                    crTopNode=RONode(7584), crBottomNode=RONode(9717), 
                                    dlCenterPoint=[207.65, -190.85, 191.06], dBoreRadius=49.8668, 
                                    dBoreHeight=170.105, dlAxisDefined=[0.0, 0.71, -0.71], 
                                    iDepthDirection=-1, iNumOfLayerPoint=20, 
                                    dlLayers=[0.0, 56.7015, 113.403, 170.105], dlAxisX=[0.14, 0.7, 0.7])  # [hl:end]
JPT.Debugger(FFTCondition)
