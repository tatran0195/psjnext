# Title:   Analysis.ADVC.MakeProcess.ModalFreqResp()
# Desc:    Create an ADVC Modal Frequency Response process. This process could be created in one time or multiple times
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.ADVC.MakeProcess.ModalFreqResp
# ---
Geometry.Part.Cube()

process = Analysis.ADVC.MakeProcess.ModalFreqResp(strName="Process_0", listLoadNode=[],  # [hl:start]
    listLoadCaseNode=[], listLoadNodeContact=[], listAdvcRefStressResult=[])  # [hl:end]
print(str(process)) #for checking return value
