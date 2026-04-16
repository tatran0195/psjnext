# Title:   Tools.RenumberByFile()
# Desc:    Renumber the model by a CSV file. The renumber targets are Nodes, 2D Elements, 3D Elements
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.RenumberByFile
# ---
jpt_path = JPT.GetAppPathInfo((JPT.PathType.PROGRAM_PATH))

sample_model = jpt_path + 'SampleData\\PSJ\\PSJ-Utility\\JtdbSample\\RenumberByFile.jth5'
sample_csv = jpt_path + 'SampleData\\PSJ\\PSJ-Utility\\Utils\\RenumberByFile.csv'

#import model
FileMenu.LoadJTH5(sample_model)
JPT.ViewFitToModel()

result = Tools.RenumberByFile(sample_csv)  # [hl]

JPT.Debugger(result)
