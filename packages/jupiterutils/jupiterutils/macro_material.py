from __future__ import annotations
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from jupiterutils.Utility import JPT
import re
from jupiterutils.table_material import *


def from_xml_to_list(table: Element) -> tuple(list, list):
    row = int(table.attrib["Row"]) if table.attrib["Row"] else 1
    col = int(table.attrib["Col"]) if table.attrib["Col"] else 1
    # Get data from the table text
    data_row = to_float(table[0].text, col) if table[0].text else None
    # Organize the data into columns
    data_col: list = list(to_data_col(data_row, row, col)) if data_row else None
    return [row, col], data_col


def to_float(text: str, col=1) -> list:
    list = [float(x) if x.strip() != "" else None for x in text.split(",")]
    return [list[x : x + col] for x in range(0, len(list), col)]


def to_data_col(data: list, row: int, col: int) -> list:
    data_col = [[] for _ in range(col)]
    for i in range(col):
        for j in range(row):
            data_col[i].append(data[j][i])
    return data_col


def get_mat_prop_data(strXML):
    mat_name = ""
    nas_id = 0
    description = ""
    data = []
    strXML = strXML.replace("#", '"')
    root_elem = ElementTree.fromstring(strXML)
    if len(root_elem) == 0:
        raise ValueError
    mat_elem = root_elem[0]
    mat_name = mat_elem.attrib["Name"]
    nas_id = int(mat_elem.attrib["NasId"])
    description = mat_elem.attrib["Description"]
    if len(mat_elem) == 0:
        raise ValueError
    layer_elem = mat_elem[0]
    for prop_elem in layer_elem:
        try:
            if prop_elem.tag == "Density":
                obj = Density.from_xml(prop_elem)
            elif prop_elem.tag == "Elastic":
                obj = Elastic.from_xml(prop_elem)
            elif prop_elem.tag == "HyperElastic":
                obj = HyperElastic.from_xml(prop_elem)
            elif prop_elem.tag == "LowDensityFoam":
                if len(prop_elem.items()) == 0:
                    continue
                obj = LowDensityFoam.from_xml(prop_elem)
            elif prop_elem.tag == "Plastic":
                obj = Plastic.from_xml(prop_elem)
            elif prop_elem.tag == "Creep":
                obj = Creep.from_xml(prop_elem)
            elif prop_elem.tag == "RDNLK":
                obj = RDNLK.from_xml(prop_elem)
            elif prop_elem.tag == "Damping":
                obj = Damping.from_xml(prop_elem)
            elif prop_elem.tag == "Rigid":
                obj = Rigid.from_xml(prop_elem)
            elif prop_elem.tag == "ViscoElastic":
                obj = ViscoElastic.from_xml(prop_elem)
            elif prop_elem.tag == "Expansion":
                obj = Expansion.from_xml(prop_elem)
            elif prop_elem.tag == "Conductivity":
                obj = Conductivity.from_xml(prop_elem)
            elif prop_elem.tag == "SpecificHeat":
                obj = SpecificHeat.from_xml(prop_elem)
            elif prop_elem.tag == "HeatGenerateRate":
                obj = HeatGenerateRate.from_xml(prop_elem)
            elif prop_elem.tag == "GasketMembraneElastic":
                obj = GasketMembraneElastic.from_xml(prop_elem)
            elif prop_elem.tag == "GasketTransverseElastic":
                obj = GasketTransverseElastic.from_xml(prop_elem)
            elif prop_elem.tag == "GasketThickness":
                obj = GasketThickness.from_xml(prop_elem)
            elif prop_elem.tag == "GasketAdditionalBehavior":
                obj = GasketAdditionalBehavior.from_xml(prop_elem)
            elif prop_elem.tag == "StructuralViscosity":
                obj = StructuralViscosity.from_xml(prop_elem)
            elif prop_elem.tag == "Cohesive":
                obj = Cohesive.from_xml(prop_elem)
            elif prop_elem.tag == "Resistivity":
                obj = Resistivity.from_xml(prop_elem)
            elif prop_elem.tag == "FatigueLimitDiagram":
                obj = FatigueLimitDiagram.from_xml(prop_elem)
            else:
                raise NotImplementedError(f"{prop_elem.tag} is not implemented")

            data.append(obj)
        except Exception as e:
            raise Exception(f"Error in get_mat_prop_data ({prop_elem.tag}): {str(e)}")
    return mat_name, nas_id, description, data


def diff_str_xml(strXML1, strXML2):
    strXML1_mod = re.sub("DBId=#[0-9]+#", "DBId=#0#", strXML1).strip()
    strXML2_mod = re.sub("DBId=#[0-9]+#", "DBId=#0#", strXML2).strip()
    return strXML1_mod == strXML2_mod


def getMatIdFromXML(strMat):
    strMaterialID = 0
    m = re.search("NasId=#[0-9]+#", strMat)
    if m:
        m = re.search("[0-9]+", m.group())
        if m:
            strMaterialID = int(m.group())
    return strMaterialID


def getMatColorFromXML(strMat):
    strColor = 0
    m = re.search("Color=#[0-9]+#", strMat)
    if m:
        m = re.search("[0-9]+", m.group())
        if m:
            strColor = int(m.group())
    return strColor


def getMatNameFromXML(strMat):
    m = re.search("Material Name=#[^#]*#", strMat)
    if m:
        strName = m.group()
        strName = strName[strName.find("#") + 1 : strName.rfind("#")]
        return strName
    return ""


def mat_formatting(mat_str, replace_space):
    if replace_space:
        return mat_str.replace("\n", "").replace("    ", "")
    else:
        return mat_str


def convert_mat_value_from_doc(val, unit):
    # temporary disable unit conversion, wait for further feedback
    # if val != "" and val is not None:
    # val = JPT.ConvertFromDocUnit(val, unit)
    return val


def convert_mat_value_to_doc(val, unit):
    # temporary disable unit conversion, wait for further feedback
    # if val != "" and val is not None:
    # val = JPT.ConvertValueToDocUnit(val, unit)
    return val


class CMaterial:
    tmpl = """<?xml version=#1.0#?>
<JPT-MATERIAL-LIBRARY Version=#4#>
    <Material Name=#{0}# Description=#{1}# Id=#0# NasId=#{2}# DBId=#{3}# IsCompositeMaterial=#false# CId=#0# Color=#{4}#>
        <Layer Thick=# # Angle=# # Id=#0#>
{5}
        </Layer>
    </Material>
</JPT-MATERIAL-LIBRARY>"""

    def __init__(self, name, mat_id, db_id, mat_layers, mat_color, description):
        self.replace_str = True
        self.name = name
        self.mat_id = mat_id
        self.db_id = db_id
        self.mat_layers = []
        self.mat_color = mat_color
        self.description = description
        # 1 Layer
        if type(mat_layers) is list and type(mat_layers[0]) is not list:
            self.mat_layers = [mat_layers]
        # Multi Layer
        elif type(mat_layers) is list and type(mat_layers[0]) is list:
            raise NotImplementedError()

    def toStr(self, replace_str):
        mat_layer = self.mat_layers[0]
        data_str = "\n".join(matProp.toStr(replace_str) for matProp in mat_layer)
        return mat_formatting(
            self.tmpl.format(
                self.name,
                self.description,
                self.mat_id,
                self.db_id,
                self.mat_color,
                data_str,
            ),
            replace_str,
        )

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class MatPropBase:
    def __init__(self, **kwargs):
        self.replace_str = True
        super().__init__(**kwargs)
        ...


class Density(MatPropBase, TableDensity):
    tmpl = """        <Density temperatureDependency=#{0}# dependencies=#{1}#>
            <Table Row=#{2}# Col=#{3}#>
                <Data>{4}</Data>
            </Table>
        </Density>"""

    def __init__(
        self, density: list, temperatureDependency=False, dependencies=0, **kwargs
    ):
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        for param in density:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

    @classmethod
    def from_xml(cls, data: object) -> Density:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])

            params.append((DENSITY, list_data[0])) if len(list_data) > 0 else (
                DENSITY,
                [],
            )
            if temperatureDependency:
                params.append((TEMPERATURE, list_data[1])) if len(list_data) > 1 else (
                    TEMPERATURE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                density=params,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []
            listStr.append(
                f"density=[{(', '.join((f'({DICT_CHARACTERISTICS[name]}, {str(data)})' for name, data in self.table_data.data[0] if data)))}]"
            )
            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")
            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            rho_data, temp_data, extra_data = self.table_data.data[0]
            rho = [
                convert_mat_value_from_doc(rho, JPT.UnitType.Unit_Density)
                for rho in rho_data[1]
            ]
            temp = [
                convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                for temp in temp_data[1]
            ]
            extra = extra_data[1]
            tableDataStr = ""
            for row in range(self.table_data.row[0]):
                if rho:
                    tableDataStr += f"{str(rho[row]) if rho[row] is not None else ''},"
                if temp:
                    tableDataStr += (
                        f"{str(temp[row]) if temp[row] is not None else ''},"
                    )
                for i in range(len(extra)):
                    tableDataStr += (
                        f"{str(extra[i][row]) if extra[i][row] is not None else ''},"
                    )
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])
            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)
            return mat_formatting(
                self.tmpl.format(
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Elastic(MatPropBase, TableElasticity):
    tmpl = """        <Elastic Type=#{0}# temperatureDependency=#{1}# frequencyDependency=#{2}# dependencies=#{3}# Moduli=#{4}# SubOption=#{5}# noCompression=#{6}# noTension=#{7}#>
            <Table Row=#{8}# Col=#{9}#>
                <Data>{10}</Data>
            </Table>
            <Table Row=#{11}# Col=#{12}#>
                <Data>{13}</Data>
            </Table>            
        </Elastic>"""

    def __init__(
        self,
        elastic: list,
        elasticType=0,
        temperatureDependency=False,
        frequencyDependency=False,
        dependencies=0,
        moduli="LONG_TERM",
        subOption="Fail_Strain",
        noCompression=False,
        noTension=False,
        **kwargs,
    ):
        self.elasticType = elasticType
        self.temperatureDependency = temperatureDependency
        self.frequencyDependency = frequencyDependency
        self.dependencies = dependencies
        self.moduli = moduli
        self.subOption = subOption
        self.noCompression = noCompression
        self.noTension = noTension
        kwargs["elasticType"] = self.elasticType
        for param in elastic:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e
        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        if self.elasticType in [
            ELASTIC_TYPE.ISOTROPIC,
            ELASTIC_TYPE.ANISOTROPIC_2D,
            ELASTIC_TYPE.TRACTION,
        ]:
            min_col = 3
        elif self.elasticType in [
            ELASTIC_TYPE.ORTHOTROPIC_2D,
            ELASTIC_TYPE.ANISOTROPIC_3D,
        ]:
            min_col = 6
        elif self.elasticType in [
            ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_1,
            ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_2,
        ]:
            min_col = 9
        # if self.table_data.col[0] < min_col:
        self.table_data.col[0] = min_col

        if self.elasticType not in [
            ELASTIC_TYPE.ANISOTROPIC_2D,
            ELASTIC_TYPE.ANISOTROPIC_3D,
        ]:
            # Anisotropic does not depend on temperature, freq and dependencies
            if self.temperatureDependency:
                self.table_data.col[0] += 1
            if self.frequencyDependency:
                self.table_data.col[0] += 1
            self.table_data.col[0] += self.dependencies

        if self.elasticType in [ELASTIC_TYPE.ISOTROPIC, ELASTIC_TYPE.ANISOTROPIC_2D]:
            self.table_data.col[1] = 3

    @classmethod
    def from_xml(cls, data: object) -> Elastic:
        # Initialize data from object
        elasticType = int(data.attrib["Type"])
        temperatureDependency = data.attrib["temperatureDependency"] == "1"
        frequencyDependency = data.attrib["frequencyDependency"] == "1"
        dependencies = int(data.attrib["dependencies"])
        moduli = str(data.attrib["Moduli"])
        subOption = str(data.attrib["SubOption"])
        noCompression = data.attrib["noCompression"] == "1"
        noTension = data.attrib["noTension"] == "1"
        params = []
        if elasticType == ELASTIC_TYPE.ISOTROPIC:
            [row, col], list_data = from_xml_to_list(data[0])
            params.append((YOUNGS_MODULUS, list_data[0])) if len(list_data) > 0 else (
                YOUNGS_MODULUS,
                [],
            )
            params.append((SHEAR_MODULUS, list_data[1])) if len(list_data) > 1 else (
                SHEAR_MODULUS,
                [],
            )
            params.append((POISSONS_RATIO, list_data[2])) if len(list_data) > 2 else (
                POISSONS_RATIO,
                [],
            )
            if temperatureDependency:
                params.append((TEMPERATURE, list_data[3])) if len(list_data) > 3 else (
                    TEMPERATURE,
                    [],
                )
            if frequencyDependency:
                i = 4 if temperatureDependency else 3
                params.append((FREQUENCY_DEPENDENCE, list_data[i])) if len(
                    list_data
                ) > i else (
                    FREQUENCY_DEPENDENCE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )

            [row_nastran, col_nastran], list_data_nastran = from_xml_to_list(data[1])
            params.append(
                (NASTRAN_FAILURE_INDEX_TENSION, list_data_nastran[0])
            ) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[0]
            ) else (
                NASTRAN_FAILURE_INDEX_TENSION,
                [],
            )
            params.append(
                (NASTRAN_FAILURE_INDEX_COMPRESSION, list_data_nastran[1])
            ) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[1]
            ) else (
                NASTRAN_FAILURE_INDEX_COMPRESSION,
                [],
            )
            params.append(
                (NASTRAN_FAILURE_INDEX_SHEAR, list_data_nastran[2])
            ) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[2]
            ) else (
                NASTRAN_FAILURE_INDEX_SHEAR,
                [],
            )
        elif elasticType == ELASTIC_TYPE.ORTHOTROPIC_2D:
            [row, col], list_data = from_xml_to_list(data[0])
            params.append((E1, list_data[0])) if len(list_data) > 0 else (
                E1,
                [],
            )
            params.append((E2, list_data[1])) if len(list_data) > 1 else (
                E2,
                [],
            )
            params.append((G12, list_data[2])) if len(list_data) > 2 else (
                G12,
                [],
            )
            params.append((G1Z, list_data[3])) if len(list_data) > 3 else (
                G1Z,
                [],
            )
            params.append((G2Z, list_data[4])) if len(list_data) > 4 else (
                G2Z,
                [],
            )
            params.append((NU12, list_data[5])) if len(list_data) > 5 else (
                NU12,
                [],
            )
            idx = 6

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if frequencyDependency:
                params.append((FREQUENCY_DEPENDENCE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    FREQUENCY_DEPENDENCE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )

            [row_nastran, col_nastran], list_data_nastran = from_xml_to_list(data[1])
            params.append((XT, list_data_nastran[0])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[0]
            ) else (
                XT,
                [],
            )
            params.append((XC, list_data_nastran[1])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[1]
            ) else (
                XC,
                [],
            )
            params.append((YT, list_data_nastran[2])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[2]
            ) else (
                YT,
                [],
            )
            params.append((YC, list_data_nastran[3])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[3]
            ) else (
                YC,
                [],
            )
            params.append((S, list_data_nastran[4])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[4]
            ) else (
                S,
                [],
            )
            params.append((F12, list_data_nastran[5])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[5]
            ) else (
                F12,
                [],
            )
            params.append((STRN, list_data_nastran[6])) if not all(
                isinstance(val, type(None)) for val in list_data_nastran[6]
            ) else (
                STRN,
                [],
            )
        elif elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_1:
            [row, col], list_data = from_xml_to_list(data[0])
            params.append((E1, list_data[0])) if len(list_data) > 0 else (
                E1,
                [],
            )
            params.append((E2, list_data[1])) if len(list_data) > 1 else (
                E2,
                [],
            )
            params.append((E3, list_data[2])) if len(list_data) > 2 else (
                E3,
                [],
            )
            params.append((NU12, list_data[3])) if len(list_data) > 3 else (
                NU12,
                [],
            )
            params.append((NU13, list_data[4])) if len(list_data) > 4 else (
                NU13,
                [],
            )
            params.append((NU23, list_data[5])) if len(list_data) > 5 else (
                NU23,
                [],
            )
            params.append((G12, list_data[6])) if len(list_data) > 6 else (
                G12,
                [],
            )
            params.append((G13, list_data[7])) if len(list_data) > 7 else (
                G13,
                [],
            )
            params.append((G23, list_data[8])) if len(list_data) > 8 else (
                G23,
                [],
            )
            idx = 9

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if frequencyDependency:
                params.append((FREQUENCY_DEPENDENCE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    FREQUENCY_DEPENDENCE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
        elif elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_2:
            [row, col], list_data = from_xml_to_list(data[0])
            lst_name = [D1111, D1122, D2222, D1133, D2233, D3333, D1212, D1313, D2323]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if frequencyDependency:
                params.append((FREQUENCY_DEPENDENCE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    FREQUENCY_DEPENDENCE,
                    [],
                )

            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
        elif elasticType == ELASTIC_TYPE.ANISOTROPIC_2D:
            [row, col], list_data = from_xml_to_list(data[0])
            lst_name = [E1, E2, E3]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )

            [row_nastran, col_nastran], list_data_nastran = from_xml_to_list(data[1])
            lst_name = [
                NASTRAN_FAILURE_INDEX_TENSION,
                NASTRAN_FAILURE_INDEX_COMPRESSION,
                NASTRAN_FAILURE_INDEX_SHEAR,
            ]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data_nastran[i])) if not all(
                    isinstance(val, type(None)) for val in list_data_nastran[i]
                ) else (
                    NAME,
                    [],
                )
        elif elasticType == ELASTIC_TYPE.ANISOTROPIC_3D:
            [row, col], list_data = from_xml_to_list(data[0])
            lst_name = [E1, E2, E3, E4, E5, E6]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
        elif elasticType == ELASTIC_TYPE.TRACTION:
            [row, col], list_data = from_xml_to_list(data[0])
            params.append((EKNN, list_data[0])) if len(list_data) > 0 else (
                EKNN,
                [],
            )
            params.append((G1KSS, list_data[1])) if len(list_data) > 0 else (
                G1KSS,
                [],
            )
            params.append((G2KTT, list_data[2])) if len(list_data) > 0 else (
                G2KTT,
                [],
            )
            if temperatureDependency:
                params.append((TEMPERATURE, list_data[3])) if len(list_data) > 3 else (
                    TEMPERATURE,
                    [],
                )
            if frequencyDependency:
                i = 4 if temperatureDependency else 3
                params.append((FREQUENCY_DEPENDENCE, list_data[i])) if len(
                    list_data
                ) > i else (
                    FREQUENCY_DEPENDENCE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            ...
        elif (
            elasticType == ELASTIC_TYPE.LAMINA
            or elasticType == ELASTIC_TYPE.COUPLED_TRACTION
            or elasticType == ELASTIC_TYPE.SHORT_FIBER
        ):
            [row, col], list_data = from_xml_to_list(data[0])
            if temperatureDependency:
                params.append((TEMPERATURE, list_data[0])) if len(list_data) > 0 else (
                    TEMPERATURE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            ...

        return cls(
            elastic=params,
            elasticType=elasticType,
            temperatureDependency=temperatureDependency,
            frequencyDependency=frequencyDependency,
            dependencies=dependencies,
            moduli=moduli,
            subOption=subOption,
            noCompression=noCompression,
            noTension=noTension,
        )

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []
            listDataStr = []
            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            # listDataStr = [
            #     f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
            #     if data and not all(isinstance(val, type(None)) for val in data)
            #     else f"({DICT_CHARACTERISTICS[name]}, [])"
            #     for name, data in self.table_data.data[0]
            # ]
            if len(self.table_data.data) > 1:
                for name, data in self.table_data.data[1]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
                # listDataStr.extend(
                #     [
                #         f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                #         if data and not all(isinstance(val, type(None)) for val in data)
                #         else f"({DICT_CHARACTERISTICS[name]}, [])"
                #         for name, data in self.table_data.data[1]
                #     ]
                # )
            listStr.append(f"elastic=[{(', '.join(listDataStr))}]")
            if self.elasticType != 0:
                listStr.append(f"elasticType={str(self.elasticType)}")
            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.frequencyDependency:
                listStr.append(f"frequencyDependency={str(self.frequencyDependency)}")
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")
            if self.moduli != "LONG_TERM":
                listStr.append(f'moduli="{str(self.moduli)}"')
            if self.subOption != "Fail_Strain":
                listStr.append(f'subOption="{str(self.subOption)}"')
            if self.noCompression:
                listStr.append(f"noCompression={str(self.noCompression)}")
            if self.noTension:
                listStr.append(f"noTension={str(self.noTension)}")
            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            if self.elasticType == ELASTIC_TYPE.ISOTROPIC:
                (
                    e_data,
                    g_data,
                    nu_data,
                    temp_data,
                    freq_data,
                    extra_data,
                ) = self.table_data.data[0]
                e = [
                    convert_mat_value_from_doc(e, JPT.UnitType.Unit_Modulus)
                    for e in e_data[1]
                ]
                g = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g_data[1]
                ]
                nu = nu_data[1]
                temp = [
                    convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                    for temp in temp_data[1]
                ]
                freq = [
                    convert_mat_value_from_doc(freq, JPT.UnitType.Unit_Frequency)
                    for freq in freq_data[1]
                ]
                extra = extra_data[1]
                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [e, g, nu]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")
                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    if self.frequencyDependency:
                        listTableDataStr.append(
                            f"{str(freq[row]) if freq[row] is not None else ' '}"
                        ) if freq else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])
                (
                    nastran_tension_data,
                    nastran_compression_data,
                    nastran_shear_data,
                ) = self.table_data.data[1]
                tableDataStr1 = ""
                listTableDataStr.clear()
                nastran_tension = nastran_tension_data[1]
                nastran_compression = nastran_compression_data[1]
                nastran_shear = nastran_shear_data[1]
                for row in range(self.table_data.row[1]):
                    for d in [nastran_tension, nastran_compression, nastran_shear]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        )

                tableDataStr1 = ",".join(listTableDataStr)
                if not tableDataStr1:
                    tableDataStr1 = ",".join([" "] * self.table_data.col[1])
                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "3",
                        tableDataStr,
                        str(self.table_data.row[1]) if self.table_data.row[1] else "0",
                        str(self.table_data.col[1]) if self.table_data.col[1] else "3",
                        tableDataStr1,
                    ),
                    replace_str,
                )
            elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_2D:
                (
                    e1_data,
                    e2_data,
                    g12_data,
                    g1z_data,
                    g2z_data,
                    nu12_data,
                    temp_data,
                    freq_data,
                    extra_data,
                ) = self.table_data.data[0]
                e1 = [
                    convert_mat_value_from_doc(e, JPT.UnitType.Unit_Modulus)
                    for e in e1_data[1]
                ]
                e2 = [
                    convert_mat_value_from_doc(e, JPT.UnitType.Unit_Modulus)
                    for e in e2_data[1]
                ]
                g12 = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g12_data[1]
                ]
                g1z = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g1z_data[1]
                ]
                g2z = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g2z_data[1]
                ]
                nu12 = nu12_data[1]
                freq = [
                    convert_mat_value_from_doc(freq, JPT.UnitType.Unit_Frequency)
                    for freq in freq_data[1]
                ]
                temp = [
                    convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                    for temp in temp_data[1]
                ]
                extra = extra_data[1]
                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [e1, e2, g12, g1z, g2z, nu12]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    if self.frequencyDependency:
                        listTableDataStr.append(
                            f"{str(freq[row]) if freq[row] is not None else ' '}"
                        ) if freq else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])
                (
                    xt_data,
                    xc_data,
                    yt_data,
                    yc_data,
                    s_data,
                    f12_data,
                    strn_data,
                ) = self.table_data.data[1]
                tableDataStr1 = ""
                listTableDataStr.clear()
                xt = xt_data[1]
                xc = xc_data[1]
                yt = yt_data[1]
                yc = yc_data[1]
                s = s_data[1]
                f12 = f12_data[1]
                strn = strn_data[1]
                for row in range(self.table_data.row[1]):
                    for d in [xt, xc, yt, yc, s, f12, strn]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        )

                tableDataStr1 = ",".join(listTableDataStr)
                if not tableDataStr1:
                    tableDataStr1 = ",".join([" "] * self.table_data.col[1])
                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "6",
                        tableDataStr,
                        str(self.table_data.row[1]) if self.table_data.row[1] else "0",
                        str(self.table_data.col[1]) if self.table_data.col[1] else "7",
                        tableDataStr1,
                    ),
                    replace_str,
                )
            elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_1:
                (
                    e1_data,
                    e2_data,
                    e3_data,
                    nu12_data,
                    nu13_data,
                    nu23_data,
                    g12_data,
                    g13_data,
                    g23_data,
                    temp_data,
                    freq_data,
                    extra_data,
                ) = self.table_data.data[0]
                e1 = [
                    convert_mat_value_from_doc(e, JPT.UnitType.Unit_Modulus)
                    for e in e1_data[1]
                ]
                e2 = [
                    convert_mat_value_from_doc(e, JPT.UnitType.Unit_Modulus)
                    for e in e2_data[1]
                ]
                e3 = [
                    convert_mat_value_from_doc(e, JPT.UnitType.Unit_Modulus)
                    for e in e3_data[1]
                ]
                nu12 = nu12_data[1]
                nu13 = nu13_data[1]
                nu23 = nu23_data[1]
                g12 = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g12_data[1]
                ]
                g13 = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g13_data[1]
                ]
                g23 = [
                    convert_mat_value_from_doc(g, JPT.UnitType.Unit_Modulus)
                    for g in g23_data[1]
                ]
                freq = [
                    convert_mat_value_from_doc(freq, JPT.UnitType.Unit_Frequency)
                    for freq in freq_data[1]
                ]
                temp = [
                    convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                    for temp in temp_data[1]
                ]
                extra = extra_data[1]
                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [e1, e2, e3, nu12, nu13, nu23, g12, g13, g23]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    if self.frequencyDependency:
                        listTableDataStr.append(
                            f"{str(freq[row]) if freq[row] is not None else ' '}"
                        ) if freq else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])

                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "9",
                        tableDataStr,
                        "1",
                        "3",
                        ",".join([" "] * 3),
                    ),
                    replace_str,
                )
            elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_2:
                (
                    d1111_data,
                    d1122_data,
                    d2222_data,
                    d1133_data,
                    d2233_data,
                    d3333_data,
                    d1212_data,
                    d1313_data,
                    d2323_data,
                    temp_data,
                    freq_data,
                    extra_data,
                ) = self.table_data.data[0]
                d1111 = d1111_data[1]
                d1122 = d1122_data[1]
                d2222 = d2222_data[1]
                d1133 = d1133_data[1]
                d2233 = d2233_data[1]
                d3333 = d3333_data[1]
                d1212 = d1212_data[1]
                d1313 = d1313_data[1]
                d2323 = d2323_data[1]

                freq = [
                    convert_mat_value_from_doc(freq, JPT.UnitType.Unit_Frequency)
                    for freq in freq_data[1]
                ]
                temp = [
                    convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                    for temp in temp_data[1]
                ]
                extra = extra_data[1]
                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [
                        d1111,
                        d1122,
                        d2222,
                        d1133,
                        d2233,
                        d3333,
                        d1212,
                        d1313,
                        d2323,
                    ]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    if self.frequencyDependency:
                        listTableDataStr.append(
                            f"{str(freq[row]) if freq[row] is not None else ' '}"
                        ) if freq else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])

                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "9",
                        tableDataStr,
                        "1",
                        "3",
                        ",".join([" "] * 3),
                    ),
                    replace_str,
                )
            elif self.elasticType == ELASTIC_TYPE.ANISOTROPIC_2D:
                (
                    e1_data,
                    e2_data,
                    e3_data,
                ) = self.table_data.data[0]
                e1 = e1_data[1]
                e2 = e2_data[1]
                e3 = e3_data[1]

                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [e1, e2, e3]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])

                (
                    nastran_tension_data,
                    nastran_compression_data,
                    nastran_shear_data,
                ) = self.table_data.data[1]
                tableDataStr1 = ""
                listTableDataStr.clear()
                nastran_tension = nastran_tension_data[1]
                nastran_compression = nastran_compression_data[1]
                nastran_shear = nastran_shear_data[1]

                for row in range(self.table_data.row[1]):
                    for d in [nastran_tension, nastran_compression, nastran_shear]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                tableDataStr1 = ",".join(listTableDataStr)
                if not tableDataStr1:
                    tableDataStr1 = ",".join([" "] * self.table_data.col[1])

                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "3",
                        tableDataStr,
                        str(self.table_data.row[1]) if self.table_data.row[1] else "0",
                        str(self.table_data.col[1]) if self.table_data.col[1] else "3",
                        tableDataStr1,
                    ),
                    replace_str,
                )
            elif self.elasticType == ELASTIC_TYPE.ANISOTROPIC_3D:
                (
                    e1_data,
                    e2_data,
                    e3_data,
                    e4_data,
                    e5_data,
                    e6_data,
                ) = self.table_data.data[0]
                e1 = e1_data[1]
                e2 = e2_data[1]
                e3 = e3_data[1]
                e4 = e4_data[1]
                e5 = e5_data[1]
                e6 = e6_data[1]

                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [e1, e2, e3, e4, e5, e6]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])

                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "3",
                        tableDataStr,
                        "1",
                        "3",
                        ",".join([" "] * 3),
                    ),
                    replace_str,
                )
            elif self.elasticType == ELASTIC_TYPE.TRACTION:
                (
                    eknn_data,
                    g1kss_data,
                    g2ktt_data,
                    temp_data,
                    freq_data,
                    extra_data,
                ) = self.table_data.data[0]
                eknn = eknn_data[1]
                g1kss = g1kss_data[1]
                g2ktt = g2ktt_data[1]
                temp = [
                    convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                    for temp in temp_data[1]
                ]
                freq = [
                    convert_mat_value_from_doc(freq, JPT.UnitType.Unit_Frequency)
                    for freq in freq_data[1]
                ]
                extra = extra_data[1]
                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    for d in [eknn, g1kss, g2ktt]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    if self.frequencyDependency:
                        listTableDataStr.append(
                            f"{str(freq[row]) if freq[row] is not None else ' '}"
                        ) if freq else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])
                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "3",
                        tableDataStr,
                        "1",
                        "3",
                        ",".join([" "] * 3),
                    ),
                    replace_str,
                )
                ...
            elif (
                self.elasticType == ELASTIC_TYPE.LAMINA
                or self.elasticType == ELASTIC_TYPE.COUPLED_TRACTION
                or self.elasticType == ELASTIC_TYPE.SHORT_FIBER
            ):
                (
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                temp = [
                    convert_mat_value_from_doc(temp, JPT.UnitType.Unit_Temperature)
                    for temp in temp_data[1]
                ]
                extra = extra_data[1]
                tableDataStr = ""
                listTableDataStr = []
                for row in range(self.table_data.row[0]):
                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ''}"
                        ) if temp else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ''}"
                        )
                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])
                tempDependStr = "1" if self.temperatureDependency else "0"
                freqDependStr = "1" if self.frequencyDependency else "0"
                dependenciesStr = str(self.dependencies)
                noCompressionStr = "1" if self.noCompression else "0"
                noTensionStr = "1" if self.noTension else "0"
                return mat_formatting(
                    self.tmpl.format(
                        self.elasticType,
                        tempDependStr,
                        freqDependStr,
                        dependenciesStr,
                        self.moduli,
                        self.subOption,
                        noCompressionStr,
                        noTensionStr,
                        str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                        str(self.table_data.col[0]) if self.table_data.col[0] else "0",
                        tableDataStr,
                        "1",
                        "3",
                        ",".join([" "] * 3),
                    ),
                    replace_str,
                )
                ...
            ...
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr()." + str(e))

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class HyperElastic(MatPropBase, TableHyperElastic):
    tmpl = """        <HyperElastic Type=#{0}# Moduli=#{1}# temperatureDependency=#{2}# Order=#{3}# Beta=#{4}# Compressible=#{5}# Properties=#{6}# DeviatoricResponse=#{7}# VolumetricResponse=#{8}# poissonRatio=#{9}# ShearModulusForDamping=#{10}# LimitStressForDamping=#{11}# dependencies=#{12}# InputSource=#{13}#>
            <Table Row=#{14}# Col=#{15}#>
                <Data>{16}</Data>
            </Table>
            <UniaxialTestData BSmoothing=#{17}# Smoothing=#{18}# BLateralNominalStrain=#{19}# temperatureDependency=#{20}# dependencies=#{21}#>
                <Table Row=#{22}# Col=#{23}#>
                    <Data>{24}</Data>
                </Table>
            </UniaxialTestData>
            <RelaxationTestData BSTART=#{25}# TRAMP=#{26}#>
                <Table Row=#{27}# Col=#{28}#>
                    <Data>{29}</Data>
                </Table>
            </RelaxationTestData>
        </HyperElastic>"""

    def __init__(
        self,
        hyperElastic: list,
        hyperElasticType: HYPERELASTIC_TYPE,
        moduli: HYPERELASTIC_MODULI,
        inputSource: int,
        temperatureDependency=False,
        strainEnergyPotentialOrder=0,
        beta=HYPERELASTIC_BETA.FITTED_VAL,
        compressible=False,
        properties=0,
        deviatoricResponse=HYPERELASTIC_DEVIATORICRESPONSE.BIAXIAL,
        volumetricResponse=HYPERELASTIC_VOLUMETRICRESPONSE.DEFAULT,
        poissonRatio: float = None,
        shearModulusDamping: float = None,
        limiStressDamping: float = None,
        dependencies=0,
        applySmooth=False,
        smoothing=3,
        includeLateralNormalStrain=False,
        uniaxialTemperatureDependency=False,
        uniaxialDependencies=0,
        bstart: float = None,
        tramp: float = None,
        **kwargs,
    ):
        self.hElasticType = hyperElasticType
        self.moduli = moduli
        self.temperatureDependency = temperatureDependency
        self.order = strainEnergyPotentialOrder
        self.beta = beta
        self.compressible = compressible
        self.properties = properties
        self.deviatoricResponse = deviatoricResponse
        self.volumetricResponse = volumetricResponse
        self.poissonRatio = poissonRatio
        self.shearModulusDamping = shearModulusDamping
        self.limiStressDamping = limiStressDamping
        self.dependencies = dependencies
        self.inputSource = inputSource
        # uniaxial
        self.applySmooth = applySmooth
        self.smoothing = smoothing
        self.includeLateralNormalStrain = includeLateralNormalStrain
        self.uniaxialTemperatureDependency = uniaxialTemperatureDependency
        self.uniaxialDependencies = uniaxialDependencies
        # relaxiation
        self.bstart = bstart
        self.tramp = tramp
        for param in hyperElastic:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None
        kwargs["hyperElasticType"] = hyperElasticType
        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        if hyperElasticType in [
            HYPERELASTIC_TYPE.ARRUDA_BOYCE,
            HYPERELASTIC_TYPE.MOONEY_RIVLIN,
            HYPERELASTIC_TYPE.OGDEN,
            HYPERELASTIC_TYPE.POLYNOMIAL,
        ]:
            self.table_data.col[0] = 3
        elif hyperElasticType in [
            HYPERELASTIC_TYPE.NEO_HOOKE,
            HYPERELASTIC_TYPE.REDUCED_POLYNOMIAL,
        ]:
            self.table_data.col[0] = 2
        elif hyperElasticType in [HYPERELASTIC_TYPE.VAN_DER_WAALS]:
            self.table_data.col[0] = 5
        elif hyperElasticType in [HYPERELASTIC_TYPE.YEOH]:
            self.table_data.col[0] = 6
        elif hyperElasticType in [
            HYPERELASTIC_TYPE.MARLOW,
            HYPERELASTIC_TYPE.USER,
            HYPERELASTIC_TYPE.UNKNOWN,
        ]:
            self.table_data.col[0] = 1
        if self.temperatureDependency:
            self.table_data.col[0] += 1
        # uniaxial test data table
        self.table_data.col[1] = 2
        if self.includeLateralNormalStrain:
            self.table_data.col[1] += 1
        if self.uniaxialTemperatureDependency:
            self.table_data.col[1] += 1
        self.table_data.col[1] += self.uniaxialDependencies
        # relaxiation test data table:
        self.table_data.col[2] = 2

    @classmethod
    def from_xml(cls, data: object) -> HyperElastic:
        try:
            # Initialize data from object
            hElasticType = HYPERELASTIC_TYPE[data.attrib["Type"]]
            moduli = HYPERELASTIC_MODULI[data.attrib["Moduli"]]
            temperatureDependency = bool(data.attrib["temperatureDependency"] == "1")
            order = int(data.attrib["Order"])
            beta = HYPERELASTIC_BETA[data.attrib["Beta"]]
            compressible = bool(data.attrib["Compressible"] == "1")
            properties = int(data.attrib["Properties"])
            deviatoricResponse = HYPERELASTIC_DEVIATORICRESPONSE[
                data.attrib["DeviatoricResponse"]
            ]
            volumetricResponse = HYPERELASTIC_VOLUMETRICRESPONSE[
                data.attrib["VolumetricResponse"]
            ]
            poissonRatio = (
                float(data.attrib["poissonRatio"])
                if data.attrib["poissonRatio"] != "1.79769e+308"
                else None
            )
            shearModulusDamping = (
                float(data.attrib["ShearModulusForDamping"])
                if data.attrib["ShearModulusForDamping"] != "1.79769e+308"
                else None
            )
            limiStressDamping = (
                float(data.attrib["LimitStressForDamping"])
                if data.attrib["LimitStressForDamping"] != "1.79769e+308"
                else None
            )
            dependencies = int(data.attrib["dependencies"])
            inputSource = int(data.attrib["InputSource"])

            applySmooth = bool(data[1].attrib["BSmoothing"] == "1")
            smoothing = int(data[1].attrib["Smoothing"])
            includeLateralNormalStrain = bool(
                data[1].attrib["BLateralNominalStrain"] == "1"
            )
            uniaxialTemperatureDependency = bool(
                data[1].attrib["temperatureDependency"] == "1"
            )
            uniaxialDependencies = int(data[1].attrib["dependencies"])

            bstart = (
                float(data[2].attrib["BSTART"])
                if data[2].attrib["BSTART"] != "1.79769e+308"
                else None
            )
            tramp = (
                float(data[2].attrib["TRAMP"])
                if data[2].attrib["TRAMP"] != "1.79769e+308"
                else None
            )

            # coefficeint table
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [SHEAR_STIFFNESS_H]
            if hElasticType in [HYPERELASTIC_TYPE.ARRUDA_BOYCE]:
                lst_name = [MU, LAMDA_M, D]
            elif hElasticType in [
                HYPERELASTIC_TYPE.MOONEY_RIVLIN,
                HYPERELASTIC_TYPE.POLYNOMIAL,
            ]:
                lst_name = [C10, C01, D1]
            elif hElasticType in [
                HYPERELASTIC_TYPE.NEO_HOOKE,
                HYPERELASTIC_TYPE.REDUCED_POLYNOMIAL,
            ]:
                lst_name = [C10, D1]
            elif hElasticType in [HYPERELASTIC_TYPE.OGDEN]:
                lst_name = [MU1, ALPHA1, D1]
            elif hElasticType in [HYPERELASTIC_TYPE.VAN_DER_WAALS]:
                lst_name = [MU, LAMDA_M, ALPHA, BETA, D]
            elif hElasticType in [HYPERELASTIC_TYPE.YEOH]:
                lst_name = [C0, C20, C30, D1, D2, D3]
            elif hElasticType in [
                HYPERELASTIC_TYPE.MARLOW,
                HYPERELASTIC_TYPE.USER,
                HYPERELASTIC_TYPE.UNKNOWN,
            ]:
                lst_name = []
                list_data = []
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )

            # uniaxial test data table
            [row, col], list_data = from_xml_to_list(data[1][0])
            idx = 0
            lst_name = [NOMIAL_STRESS, NOMIAL_STRAIN]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if includeLateralNormalStrain:
                params.append((LATERAL_NOMIAL_STRAIN, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    LATERAL_NOMIAL_STRAIN,
                    [],
                )
                idx += 1
            if uniaxialTemperatureDependency:
                params.append((TEMPERATURE_UNIAXIAL, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE_UNIAXIAL,
                    [],
                )
                idx += 1
            if uniaxialDependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS_UNIAXIAL,
                            [
                                list_data[i]
                                if list_data[i]
                                else (EXTRA_FIELDS_UNIAXIAL, [])
                                for i in range(col - uniaxialDependencies, col)
                            ],
                        )
                    )
                )

            # relaxation test data table
            [row, col], list_data = from_xml_to_list(data[2][0])
            idx = 0
            lst_name = [STRESS, TIME]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            return cls(
                hyperElastic=params,
                hyperElasticType=hElasticType,
                moduli=moduli,
                temperatureDependency=temperatureDependency,
                strainEnergyPotentialOrder=order,
                beta=beta,
                compressible=compressible,
                properties=properties,
                deviatoricResponse=deviatoricResponse,
                volumetricResponse=volumetricResponse,
                poissonRatio=poissonRatio,
                shearModulusDamping=shearModulusDamping,
                limiStressDamping=limiStressDamping,
                dependencies=dependencies,
                inputSource=inputSource,
                applySmooth=applySmooth,
                smoothing=smoothing,
                includeLateralNormalStrain=includeLateralNormalStrain,
                uniaxialTemperatureDependency=uniaxialTemperatureDependency,
                uniaxialDependencies=uniaxialDependencies,
                bstart=bstart,
                tramp=tramp,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []
            listDataStr = []

            listStr.append(f'hyperElasticType="{str(self.hElasticType)}"')
            listStr.append(f'moduli="{str(self.moduli)}"')
            listStr.append(f"inputSource={str(self.inputSource)}")

            for i in range(3):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"hyperElastic=[{(', '.join(listDataStr))}]")
            if self.temperatureDependency:
                listStr.append(
                    f'temperatureDependency="{str(self.temperatureDependency)}"'
                )

            if self.hElasticType in [HYPERELASTIC_TYPE.ARRUDA_BOYCE]:
                listStr.append(f'volumetricResponse="{str(self.volumetricResponse)}"')
                if self.poissonRatio is not None:
                    listStr.append(f"poissonRatio={str(self.poissonRatio)}")
            elif self.hElasticType in [HYPERELASTIC_TYPE.MARLOW]:
                listStr.append(f'deviatoricResponse="{str(self.deviatoricResponse)}"')
                listStr.append(f'volumetricResponse="{str(self.volumetricResponse)}"')
                if self.poissonRatio is not None:
                    listStr.append(f"poissonRatio={str(self.poissonRatio)}")
            elif self.hElasticType in [
                HYPERELASTIC_TYPE.MOONEY_RIVLIN,
                HYPERELASTIC_TYPE.NEO_HOOKE,
                HYPERELASTIC_TYPE.POLYNOMIAL,
                HYPERELASTIC_TYPE.REDUCED_POLYNOMIAL,
                HYPERELASTIC_TYPE.YEOH,
            ]:
                listStr.append(f'volumetricResponse="{str(self.volumetricResponse)}"')
                if self.poissonRatio is not None:
                    listStr.append(f"poissonRatio={str(self.poissonRatio)}")
                listStr.append(f"strainEnergyPotentialOrder={str(self.order)}")
            elif self.hElasticType in [HYPERELASTIC_TYPE.OGDEN]:
                listStr.append(f'volumetricResponse="{str(self.volumetricResponse)}"')
                if self.poissonRatio is not None:
                    listStr.append(f"poissonRatio={str(self.poissonRatio)}")
                listStr.append(f"strainEnergyPotentialOrder={str(self.order)}")
                if self.shearModulusDamping is not None:
                    listStr.append(
                        f"shearModulusDamping={str(self.shearModulusDamping)}"
                    )
                if self.limiStressDamping is not None:
                    listStr.append(f"limiStressDamping={str(self.limiStressDamping)}")
            elif self.hElasticType in [HYPERELASTIC_TYPE.USER]:
                listStr.append(f"compressible={str(self.compressible)}")
                listStr.append(f"properties={str(self.properties)}")
            elif self.hElasticType in [HYPERELASTIC_TYPE.VAN_DER_WAALS]:
                listStr.append(f'volumetricResponse="{str(self.volumetricResponse)}"')
                if self.poissonRatio is not None:
                    listStr.append(f"poissonRatio={str(self.poissonRatio)}")
                listStr.append(f'beta="{str(self.beta)}"')
            elif self.hElasticType in [HYPERELASTIC_TYPE.UNKNOWN]:
                ...

            if self.applySmooth:
                listStr.append(f"applySmooth={str(self.applySmooth)}")
            listStr.append(f"smoothing={str(self.smoothing)}")
            if self.includeLateralNormalStrain == True:
                listStr.append(
                    f"includeLateralNormalStrain={str(self.includeLateralNormalStrain)}"
                )
            if self.uniaxialTemperatureDependency == True:
                listStr.append(
                    f"uniaxialTemperatureDependency={str(self.uniaxialTemperatureDependency)}"
                )
            if self.uniaxialDependencies != 0:
                listStr.append(f"uniaxialDependencies={str(self.uniaxialDependencies)}")

            if self.bstart is not None:
                listStr.append(f"bstart={str(self.bstart)}")
            if self.tramp is not None:
                listStr.append(f"tramp={str(self.tramp)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except Exception as e:
            raise NameError(
                f"Error in {self.__class__.__name__}.to_PSJ_str(): {str(e)}"
            )

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            if self.hElasticType in [HYPERELASTIC_TYPE.ARRUDA_BOYCE]:
                mu_data, lamda_m_data, d_data, temp_data = self.table_data.data[0]
                mu = mu_data[1]  # may need conversion for unit later
                lamda_m = lamda_m_data[1]  # may need conversion for unit later
                d = d_data[1]  # may need conversion for unit later
                lst_name = [mu, lamda_m, d]
            elif self.hElasticType in [
                HYPERELASTIC_TYPE.MOONEY_RIVLIN,
                HYPERELASTIC_TYPE.POLYNOMIAL,
            ]:
                c10_data, c01_data, d1_data, temp_data = self.table_data.data[0]
                c10 = c10_data[1]  # may need conversion for unit later
                c01 = c01_data[1]  # may need conversion for unit later
                d1 = d1_data[1]  # may need conversion for _uniaxialunit later
                lst_name = [c10, c01, d1]
            elif self.hElasticType in [
                HYPERELASTIC_TYPE.NEO_HOOKE,
                HYPERELASTIC_TYPE.REDUCED_POLYNOMIAL,
            ]:
                c10_data, d1_data, temp_data = self.table_data.data[0]
                c10 = c10_data[1]  # may need conversion for unit later
                d1 = d1_data[1]  # may need conversion for unit later
                lst_name = [c10, d1]
            elif self.hElasticType in [HYPERELASTIC_TYPE.OGDEN]:
                mu1_data, alpha1_data, d1_data, temp_data = self.table_data.data[0]
                mu1 = mu1_data[1]  # may need conversion for unit later
                alpha1 = alpha1_data[1]  # may need conversion for unit later
                d1 = d1_data[1]  # may need conversion for unit later
                lst_name = [mu1, alpha1, d1]
            elif self.hElasticType in [HYPERELASTIC_TYPE.VAN_DER_WAALS]:
                (
                    mu_data,
                    lamda_m_data,
                    alpha_data,
                    beta_data,
                    d_data,
                    temp_data,
                ) = self.table_data.data[0]
                mu = mu_data[1]  # may need conversion for unit later
                lamda_m = lamda_m_data[1]  # may need conversion for unit later
                alpha = alpha_data[1]  # may need conversion for unit later
                beta = beta_data[1]  # may need conversion for unit later
                d = d_data[1]  # may need conversion for unit later
                lst_name = [mu, lamda_m, alpha, beta, d]
            elif self.hElasticType in [HYPERELASTIC_TYPE.YEOH]:
                (
                    c0_data,
                    c20_data,
                    c30_data,
                    d1_data,
                    d2_data,
                    d3_data,
                    temp_data,
                ) = self.table_data.data[0]
                c0 = c0_data[1]  # may need conversion for unit later
                c20 = c20_data[1]  # may need conversion for unit later
                c30 = c30_data[1]  # may need conversion for unit later
                d1 = d1_data[1]  # may need conversion for unit later
                d2 = d2_data[1]  # may need conversion for unit later
                d3 = d3_data[1]  # may need conversion for unit later
                lst_name = [c0, c20, c30, d1, d2, d3]
            elif self.hElasticType in [
                HYPERELASTIC_TYPE.MARLOW,
                HYPERELASTIC_TYPE.USER,
                HYPERELASTIC_TYPE.UNKNOWN,
            ]:
                lst_name = []
                temp_data = [TEMPERATURE, []]

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            # extra_h = extra_data_h[1]
            for row in range(self.table_data.row[0]):
                for d in lst_name:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                # for i in range(len(extra_h)):
                #     listTableDataStr.append(
                #         f"{str(extra_h[i][row]) if extra_h[i][row] is not None else ' '}"
                #     )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            # Uniaxial test data information
            tableDataStrV = ""
            listTableDataStrV = []

            (
                stress_data_v,
                strain_data_v,
                lateral_data_v,
                temp_data_v,
                extra_data_v,
            ) = self.table_data.data[1]
            stress_v = stress_data_v[1]  # may need conversion for unit later
            strain_v = strain_data_v[1]  # may need conversion for unit later
            lateral_v = lateral_data_v[1]  # may need conversion for unit later
            temp_v = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data_v[1]
            ]
            extra_v = extra_data_v[1]

            for row in range(self.table_data.row[1]):
                for d in [stress_v, strain_v]:
                    listTableDataStrV.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStrV.append(" ")

                if self.includeLateralNormalStrain:
                    listTableDataStrV.append(
                        f"{str(lateral_v[row]) if lateral_v[row] is not None else ' '}"
                    ) if lateral_v else listTableDataStrV.append(" ")
                if self.uniaxialTemperatureDependency:
                    listTableDataStrV.append(
                        f"{str(temp_v[row]) if temp_v[row] is not None else ' '}"
                    ) if temp_v else listTableDataStrV.append(" ")
                for i in range(len(extra_v)):
                    listTableDataStrV.append(
                        f"{str(extra_v[i][row]) if extra_v[i][row] is not None else ' '}"
                    )

            tableDataStrV = ",".join(listTableDataStrV)
            if not tableDataStrV:
                tableDataStrV = ",".join([" "] * self.table_data.col[1])

            # Relaxation test data information
            tableDataStr2 = ""
            listTableDataStr2 = []

            stress_data_2, time_data_2 = self.table_data.data[2]
            stress = stress_data_2[1]  # may need conversion for unit later
            time = time_data_2[1]  # may need conversion for unit later

            for row in range(self.table_data.row[2]):
                for d in [stress, time]:
                    listTableDataStr2.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr2.append(" ")

            tableDataStr2 = ",".join(listTableDataStr2)
            if not tableDataStr2:
                tableDataStr2 = ",".join([" "] * self.table_data.col[1])

            return mat_formatting(
                self.tmpl.format(
                    str(self.hElasticType),
                    str(self.moduli),
                    "1" if self.temperatureDependency else "0",
                    str(self.order),
                    str(self.beta),
                    "1" if self.compressible else "0",
                    str(self.properties),
                    str(self.deviatoricResponse),
                    str(self.volumetricResponse),
                    str(self.poissonRatio)
                    if self.poissonRatio is not None
                    else "1.79769e+308",
                    str(self.shearModulusDamping)
                    if self.shearModulusDamping is not None
                    else "1.79769e+308",
                    str(self.limiStressDamping)
                    if self.limiStressDamping is not None
                    else "1.79769e+308",
                    str(self.dependencies),
                    str(self.inputSource),
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                    "1" if self.applySmooth else "0",
                    str(self.smoothing),
                    "1" if self.includeLateralNormalStrain else "0",
                    "1" if self.uniaxialTemperatureDependency else "0",
                    str(self.uniaxialDependencies),
                    str(self.table_data.row[1]) if self.table_data.row[1] else "1",
                    str(self.table_data.col[1]) if self.table_data.col[1] else "1",
                    tableDataStrV if tableDataStrV[-1] != "," else tableDataStrV[:-1],
                    str(self.bstart) if self.bstart is not None else "1.79769e+308",
                    str(self.tramp) if self.tramp is not None else "1.79769e+308",
                    str(self.table_data.row[2]) if self.table_data.row[2] else "1",
                    str(self.table_data.col[2]) if self.table_data.col[2] else "1",
                    tableDataStrV if tableDataStr2[-1] != "," else tableDataStr2[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class LowDensityFoam(MatPropBase, TableLowDensityFoam):
    tmpl = """        <LowDensityFoam>
            <Table Row=#0# Col=#0#>
                <Data></Data>
            </Table>
        </LowDensityFoam>
        <LowDensityFoam mu0=#{0}# mu1=#{1}# alpha=#{2}#>
            <UNIAXIALTESTDATA_TENSION dependencies=#{3}#>
                <Table Row=#{4}# Col=#{5}#>
                    <Data>{6}</Data>
                </Table>
            </UNIAXIALTESTDATA_TENSION>
            <UNIAXIALTESTDATA_COMPRESSION dependencies=#{7}#>
                <Table Row=#{8}# Col=#{9}#>
                    <Data>{10}</Data>
                </Table>
            </UNIAXIALTESTDATA_COMPRESSION>
        </LowDensityFoam>"""

    def __init__(
        self,
        lowDensityFoam: list,
        mu0: float = 0.0,
        mu1: float = 0.0,
        alpha: float = 0.0,
        dependenciesTension: int = 0,
        dependenciesCompression: int = 0,
        **kwargs,
    ):
        self.lowDensityFoam = lowDensityFoam
        self.mu0 = mu0
        self.mu1 = mu1
        self.alpha = alpha
        self.dependenciesTension = dependenciesTension
        self.dependenciesCompression = dependenciesCompression

        for param in lowDensityFoam:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None
        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns

        self.table_data.col[0] = 3
        self.table_data.col[0] += self.dependenciesTension
        self.table_data.col[1] = 3
        self.table_data.col[1] += self.dependenciesCompression

    @classmethod
    def from_xml(cls, data: Element) -> LowDensityFoam:
        try:
            # Initialize data from object
            mu0 = float(data.attrib["mu0"])
            mu1 = float(data.attrib["mu1"])
            alpha = float(data.attrib["alpha"])
            dependenciesTension = int(data[0].attrib["dependencies"])
            dependenciesCompression = int(data[1].attrib["dependencies"])

            # tension
            params = []
            [row, col], list_data = from_xml_to_list(data[0][0])
            idx = 0
            lst_name = [STRESS_TENSION, STRAIN_TENSION, STRAIN_RATE_TENSION]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if dependenciesTension:
                params.append(
                    (
                        (
                            EXTRA_FIELDS_TENSION,
                            [
                                list_data[i]
                                if list_data[i]
                                else (EXTRA_FIELDS_TENSION, [])
                                for i in range(col - dependenciesTension, col)
                            ],
                        )
                    )
                )

            # compression
            [row, col], list_data = from_xml_to_list(data[1][0])
            idx = 0
            lst_name = [STRESS_COMPRESSION, STRAIN_COMPRESSION, STRAIN_RATE_COMPRESSION]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if dependenciesCompression:
                params.append(
                    (
                        (
                            EXTRA_FIELDS_COMPRESSION,
                            [
                                list_data[i]
                                if list_data[i]
                                else (EXTRA_FIELDS_COMPRESSION, [])
                                for i in range(col - dependenciesCompression, col)
                            ],
                        )
                    )
                )

            return cls(
                lowDensityFoam=params,
                mu0=mu0,
                mu1=mu1,
                alpha=alpha,
                dependenciesTension=dependenciesTension,
                dependenciesCompression=dependenciesCompression,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []
            listDataStr = []

            for i in range(2):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"lowDensityFoam=[{(', '.join(listDataStr))}]")

            listStr.append(f"mu0={str(self.mu0)}")
            listStr.append(f"mu1={str(self.mu1)}")
            listStr.append(f"alpha={str(self.alpha)}")

            if self.dependenciesTension:
                listStr.append(f"dependenciesTension={str(self.dependenciesTension)}")
            if self.dependenciesCompression:
                listStr.append(
                    f"dependenciesCompression={str(self.dependenciesCompression)}"
                )

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except Exception as e:
            raise NameError(
                f"Error in {self.__class__.__name__}.to_PSJ_str(): {str(e)}"
            )

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            # Tension
            (
                stress_tens_data,
                strain_tens_data,
                strain_rate_tens_data,
                extra_data_tens,
            ) = self.table_data.data[0]
            # may need conversion for unit later
            stress_tens = stress_tens_data[1]
            # may need conversion for unit later
            strain_tens = strain_tens_data[1]
            # may need conversion for unit later
            strain_rate_tens = strain_rate_tens_data[1]
            lst_name = [stress_tens, strain_tens, strain_rate_tens]

            extra_data_tens = extra_data_tens[1]
            for row in range(self.table_data.row[0]):
                for d in lst_name:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                for i in range(len(extra_data_tens)):
                    listTableDataStr.append(
                        f"{str(extra_data_tens[i][row]) if extra_data_tens[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            # Compression
            tableDataStr2 = ""
            listTableDataStr2 = []
            (
                stress_comp_data,
                strain_comp_data,
                strain_rate_comp_data,
                extra_data_comp,
            ) = self.table_data.data[1]
            # may need conversion for unit later
            stress_comp = stress_comp_data[1]
            # may need conversion for unit later
            strain_comp = strain_comp_data[1]
            # may need conversion for unit later
            strain_rate_comp = strain_rate_comp_data[1]
            lst_name = [stress_comp, strain_comp, strain_rate_comp]

            extra_data_comp = extra_data_comp[1]
            for row in range(self.table_data.row[0]):
                for d in lst_name:
                    listTableDataStr2.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr2.append(" ")

                for i in range(len(extra_data_comp)):
                    listTableDataStr2.append(
                        f"{str(extra_data_comp[i][row]) if extra_data_comp[i][row] is not None else ' '}"
                    )

            tableDataStr2 = ",".join(listTableDataStr2)
            if not tableDataStr2:
                tableDataStr2 = ",".join([" "] * self.table_data.col[1])

            return mat_formatting(
                self.tmpl.format(
                    str(self.mu0),
                    str(self.mu1),
                    str(self.alpha),
                    str(self.dependenciesTension),
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                    str(self.dependenciesCompression),
                    str(self.table_data.row[1]) if self.table_data.row[1] else "1",
                    str(self.table_data.col[1]) if self.table_data.col[1] else "1",
                    tableDataStr2 if tableDataStr2[-1] != "," else tableDataStr2[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Plastic(MatPropBase, TablePlastic):
    tmpl = """        <Plastic Harden=#{0}# Curve=#{1}# Curve_ForCombined=#{2}# DataType=#{3}# temperatureDependency=#{4}# dependencies=#{5}# UseStrain=#{6}# ExportAdvc=#{7}# Backstress=#{8}# SubOption_Type=#{9}# SubOption_FieldNum=#{10}# SubOption_UseTempDependent=#{11}# SubOption_UseParameter=#{12}#>
            <Table Row=#{13}# Col=#{14}#>
                <Data>{15}</Data>
            </Table>
            <SubOption_Table Row=#{16}# Col=#{17}#>
                <Data>{18}</Data>
            </SubOption_Table>
        </Plastic>"""

    def __init__(
        self,
        plastic: list,
        harden=0,
        curve=0,
        curve_ForCombined=0,
        dataType=0,
        temperatureDependency=False,
        dependencies=0,
        useStrain=False,
        exportAdvc=False,
        backStress=1,
        subOption_Type=0,
        subOption_FieldNum=0,
        subOption_UseTempDependent=False,
        subOption_UseParameter=False,
        **kwargs,
    ):
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        self.harden = harden
        self.curve = curve
        self.curve_ForCombined = curve_ForCombined
        self.dataType = dataType
        self.useStrain = useStrain
        self.exportAdvc = exportAdvc
        self.backStress = backStress
        self.subOption_Type = subOption_Type
        self.subOption_FieldNum = subOption_FieldNum
        self.subOption_UseTempDependent = subOption_UseTempDependent
        self.subOption_UseParameter = subOption_UseParameter
        kwargs["harden"] = self.harden
        kwargs["dataType"] = self.dataType
        kwargs["curve_ForCombined"] = self.curve_ForCombined
        for param in plastic:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)

        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        if self.harden in [PLASTIC_HARDENING.ISOTROPIC, PLASTIC_HARDENING.KINEMATIC]:
            min_col = 2
        elif self.harden in [PLASTIC_HARDENING.USER]:
            min_col = 1
        elif self.harden in [PLASTIC_HARDENING.JOHNSON_COOK]:
            min_col = 6
        elif self.harden in [PLASTIC_HARDENING.COMBINED]:
            if self.dataType == 1:
                min_col = 3
            else:
                min_col = 2
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        if self.useStrain:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

        if self.subOption_Type in [3]:
            self.table_data.col[1] = 3 if self.subOption_UseParameter else 2
            self.table_data.col[1] += self.subOption_FieldNum
            if self.subOption_UseTempDependent:
                self.table_data.col[1] += 1
        else:
            self.table_data.col[1] = 0

    @classmethod
    def from_xml(cls, data: object) -> Plastic:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            harden = int(data.attrib["Harden"])
            curve = int(data.attrib["Curve"])
            curve_ForCombined = int(data.attrib["Curve_ForCombined"])
            dataType = int(data.attrib["DataType"])
            useStrain = data.attrib["UseStrain"] == "true"
            exportAdvc = data.attrib["ExportAdvc"] == "true"
            backStress = int(data.attrib["Backstress"])
            subOption_Type = int(data.attrib["SubOption_Type"])
            subOption_FieldNum = int(data.attrib["SubOption_FieldNum"])
            subOption_UseTempDependent = (
                data.attrib["SubOption_UseTempDependent"] == "true"
            )
            subOption_UseParameter = data.attrib["SubOption_UseParameter"] == "true"
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            lst_name = []
            if harden in [PLASTIC_HARDENING.ISOTROPIC, PLASTIC_HARDENING.KINEMATIC]:
                lst_name = [STRESS, STRAIN]
            elif harden == PLASTIC_HARDENING.JOHNSON_COOK:
                lst_name = [A, B, M, N, MELTING_TEMP, TRANSITION_TEMP]
            elif harden == PLASTIC_HARDENING.USER:
                lst_name = [HARDENING_PROP]
            elif harden == PLASTIC_HARDENING.COMBINED:
                if dataType == 0:
                    if curve_ForCombined in [0, 1]:
                        lst_name = [STRESS, STRAIN]
                    elif curve_ForCombined == 2:
                        lst_name = [GAMMA, HARD_PARAM]
                elif dataType == 1:
                    lst_name = [STRESS, GAMMA, HARD_PARAM]
                elif dataType == 2:
                    lst_name = [STRESS, STRAIN]

            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if useStrain:
                params.append((STRAIN_RATE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
            if temperatureDependency:
                idx = (idx + 1) if useStrain else idx
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )

            if len(data) > 1:
                if subOption_Type == 3:
                    [row1, col1], list_data = from_xml_to_list(data[-1])

                    lst_name = (
                        [EQUIV_STRESS, Q_INFINITY, HARDENING_B]
                        if subOption_UseParameter
                        else [EQUIV_STRESS, EQUIV_STRAIN]
                    )
                    idx = 0
                    for i, NAME in enumerate(lst_name):
                        params.append((NAME, list_data[i])) if len(list_data) > i else (
                            NAME,
                            [],
                        )
                    idx = len(lst_name)
                    if subOption_FieldNum:
                        params.append(
                            (
                                (
                                    EXTRA_FIELDS_SUB,
                                    [
                                        list_data[i]
                                        if list_data[i]
                                        else (EXTRA_FIELDS_SUB, [])
                                        for i in range(idx, idx + subOption_FieldNum)
                                    ],
                                )
                            )
                        )
                    idx += subOption_FieldNum
                    if subOption_UseTempDependent:
                        params.append((TEMPERATURE_SUB, list_data[idx])) if len(
                            list_data
                        ) > idx else (
                            TEMPERATURE_SUB,
                            [],
                        )

            return cls(
                plastic=params,
                harden=harden,
                curve=curve,
                curve_ForCombined=curve_ForCombined,
                dataType=dataType,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
                useStrain=useStrain,
                exportAdvc=exportAdvc,
                backStress=backStress,
                subOption_Type=subOption_Type,
                subOption_FieldNum=subOption_FieldNum,
                subOption_UseTempDependent=subOption_UseTempDependent,
                subOption_UseParameter=subOption_UseParameter,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []
            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            if len(self.table_data.data) > 1:
                for name, data in self.table_data.data[1]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"plastic=[{(', '.join(listDataStr))}]")

            if self.harden != 0:
                listStr.append(f"harden={str(self.harden)}")
            if self.curve != 0:
                listStr.append(f"curve={str(self.curve)}")
            if self.curve_ForCombined != 0:
                listStr.append(f"curve_ForCombined={str(self.curve_ForCombined)}")
            if self.dataType != 0:
                listStr.append(f"dataType={str(self.dataType)}")
            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")
            if self.useStrain:
                listStr.append(f"useStrain={str(self.useStrain)}")
            if self.exportAdvc:
                listStr.append(f"exportAdvc={str(self.exportAdvc)}")
            if self.backStress != 1:
                listStr.append(f"backStress={str(self.backStress)}")
            if self.subOption_Type != 0:
                listStr.append(f"subOption_Type={str(self.subOption_Type)}")
            if self.subOption_FieldNum != 0:
                listStr.append(f"subOption_FieldNum={str(self.subOption_FieldNum)}")
            if self.subOption_UseTempDependent:
                listStr.append(
                    f"subOption_UseTempDependent={str(self.subOption_UseTempDependent)}"
                )
            if self.subOption_UseParameter:
                listStr.append(
                    f"subOption_UseParameter={str(self.subOption_UseParameter)}"
                )

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []
            if self.harden in [
                PLASTIC_HARDENING.ISOTROPIC,
                PLASTIC_HARDENING.KINEMATIC,
            ]:
                (
                    stress_data,
                    strain_data,
                    rate_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                stress = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Stress)
                    for x in stress_data[1]
                ]
                strain = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Strain)
                    for x in strain_data[1]
                ]

                rate = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Strain)
                    for x in rate_data[1]
                ]
                temp = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                    for x in temp_data[1]
                ]
                extra = extra_data[1]

                for row in range(self.table_data.row[0]):
                    for d in [stress, strain]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.useStrain:
                        listTableDataStr.append(
                            f"{str(rate[row]) if rate[row] is not None else ' '}"
                        ) if rate else listTableDataStr.append(" ")
                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
            elif self.harden == PLASTIC_HARDENING.JOHNSON_COOK:
                (
                    a_data,
                    b_data,
                    m_data,
                    n_data,
                    melttemp_data,
                    transtemp_data,
                ) = self.table_data.data[0]
                a = a_data[1]
                b = b_data[1]
                n = n_data[1]
                m = m_data[1]
                melt_temp = melttemp_data[1]
                trans_temp = transtemp_data[1]

                for row in range(self.table_data.row[0]):
                    for d in [a, b, m, n, melt_temp, trans_temp]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

            elif self.harden == PLASTIC_HARDENING.USER:
                (harden_data,) = self.table_data.data[0]
                hardening_prop = harden_data[1]

                for row in range(self.table_data.row[0]):
                    for d in [hardening_prop]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

            elif self.harden == PLASTIC_HARDENING.COMBINED:
                rate_data = temp_data = extra_data = []
                if self.dataType == 0:
                    if self.curve_ForCombined in [0, 1]:
                        (
                            stress_data,
                            strain_data,
                            rate_data,
                            temp_data,
                            extra_data,
                        ) = self.table_data.data[0]
                        stress = stress_data[1]
                        strain = strain_data[1]
                        lst = [stress, strain]
                    elif self.curve_ForCombined == 2:
                        (
                            gamma_data,
                            hard_data,
                            rate_data,
                            temp_data,
                            extra_data,
                        ) = self.table_data.data[0]
                        gamma = gamma_data[1]
                        hard_param = hard_data[1]
                        lst = [gamma, hard_param]
                elif self.dataType == 1:
                    (
                        stress_data,
                        gamma_data,
                        hard_data,
                        rate_data,
                        temp_data,
                        extra_data,
                    ) = self.table_data.data[0]
                    stress = stress_data[1]
                    gamma = gamma_data[1]
                    hard_param = hard_data[1]
                    lst = [stress, gamma, hard_param]
                elif self.dataType == 2:
                    (
                        stress_data,
                        strain_data,
                        rate_data,
                        temp_data,
                        extra_data,
                    ) = self.table_data.data[0]
                    stress = stress_data[1]
                    strain = strain_data[1]
                    lst = [stress, strain]
                rate = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Strain)
                    for x in rate_data[1]
                ]
                temp = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                    for x in temp_data[1]
                ]
                extra = extra_data[1]
                for row in range(self.table_data.row[0]):
                    for d in lst:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.useStrain:
                        listTableDataStr.append(
                            f"{str(rate[row]) if rate[row] is not None else ' '}"
                        ) if rate else listTableDataStr.append(" ")
                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
            else:
                raise ValueError(f"Invalid hardening type")
            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            table1 = {"col": 0, "row": 0, "tableStr": ""}
            if self.subOption_Type == 3:
                (
                    eqstress_data,
                    eqstrain_data,
                    qinfty_data,
                    hardenb_data,
                    subextra_data,
                    subtemp_data,
                ) = self.table_data.data[1]
                eqstress = eqstress_data[1]
                eqstrain = eqstrain_data[1]
                qinfty = qinfty_data[1]
                hardenb = hardenb_data[1]
                subextra = subextra_data[1]
                subtemp = subtemp_data[1]

                tableDataStr1 = ""
                listTableDataStr1 = []
                for row in range(self.table_data.row[1]):
                    lst = (
                        [eqstress, qinfty, hardenb]
                        if self.subOption_UseParameter
                        else [eqstress, eqstrain]
                    )
                    for d in lst:
                        listTableDataStr1.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr1.append(" ")

                    for i in range(len(subextra)):
                        listTableDataStr1.append(
                            f"{str(subextra[i][row]) if subextra[i][row] is not None else ' '}"
                        )
                    if self.subOption_UseTempDependent:
                        listTableDataStr1.append(
                            f"{str(subtemp[row]) if subtemp[row] is not None else ' '}"
                        ) if subtemp else listTableDataStr1.append(" ")

                tableDataStr1 = ",".join(listTableDataStr1)
                if not tableDataStr1:
                    tableDataStr1 = ",".join([" "] * self.table_data.col[1])
                table1["row"] = self.table_data.row[1]
                table1["col"] = self.table_data.col[1]
                table1["tableStr"] = tableDataStr1

            hardenStr = str(self.harden)
            curveStr = str(self.curve)
            curve_ForCombinedStr = str(self.curve_ForCombined)
            dataTypeStr = str(self.dataType)
            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)
            useStrainStr = "true" if self.useStrain else "false"
            exportAdvcStr = "true" if self.exportAdvc else "false"
            backStressStr = str(self.backStress)
            subOption_TypeStr = str(self.subOption_Type)
            subOption_FieldNumStr = str(self.subOption_FieldNum)
            subOption_UseTempDependentStr = (
                "true" if self.subOption_UseTempDependent else "false"
            )
            subOption_UseParameterStr = (
                "true" if self.subOption_UseParameter else "false"
            )

            return mat_formatting(
                self.tmpl.format(
                    hardenStr,
                    curveStr,
                    curve_ForCombinedStr,
                    dataTypeStr,
                    tempDependStr,
                    dependenciesStr,
                    useStrainStr,
                    exportAdvcStr,
                    backStressStr,
                    subOption_TypeStr,
                    subOption_FieldNumStr,
                    subOption_UseTempDependentStr,
                    subOption_UseParameterStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                    table1["row"],
                    table1["col"],
                    table1["tableStr"],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Creep(MatPropBase, TableCreep):
    tmpl = """        <Creep LawType=#{0}# SubOption=#{1}# AdvcLawType=#{2}# AdvcHardenType=#{3}# temperatureDependency=#{4}# dependencies=#{5}#>
            <Table Row=#{6}# Col=#{7}#>
                <Data>{8}s</Data>
            </Table>
        </Creep>"""

    def __init__(
        self,
        creep: list,
        lawType: PLASTICITY_CREEP_LAW_TYPE = 0,
        suboption: int = 0,
        advcLawType: int = 0,
        advcHardenType: int = 0,
        dependencies: int = 0,
        temperatureDependency: bool = False,
        **kwargs,
    ):
        self.creep = creep
        self.lawType = lawType
        self.suboption = suboption
        self.advcLawType = advcLawType
        self.advcHardenType = advcHardenType
        self.dependencies = dependencies
        self.temperatureDependency = temperatureDependency
        kwargs["lawType"] = lawType
        for param in creep:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None
        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        if self.lawType in [
            PLASTICITY_CREEP_LAW_TYPE.STRAIN_HARDENING,
            PLASTICITY_CREEP_LAW_TYPE.TIME_HARDENING,
        ]:
            self.table_data.col[0] = 3
        elif self.lawType in [PLASTICITY_CREEP_LAW_TYPE.HYPERBOLIC_SINE]:
            self.table_data.col[0] = 5
        elif self.lawType in [PLASTICITY_CREEP_LAW_TYPE.ADVC_LAW]:
            self.table_data.col[0] = 4
        else:
            self.table_data.col[0] = 0
        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: Element) -> Creep:
        try:
            # Initialize data from object
            lawType = int(data.attrib["LawType"])
            suboption = int(data.attrib["SubOption"])
            advcLawType = int(data.attrib["AdvcLawType"])
            advcHardenType = int(data.attrib["AdvcHardenType"])
            temperatureDependency = bool(data.attrib["temperatureDependency"] == "1")
            dependencies = int(data.attrib["dependencies"])

            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = []
            if lawType in [
                PLASTICITY_CREEP_LAW_TYPE.STRAIN_HARDENING,
                PLASTICITY_CREEP_LAW_TYPE.TIME_HARDENING,
            ]:
                lst_name = [POWER_LAW_MULTIPLIER, EQ_STRESS_ORDER, TIME_ORDER]
            elif lawType in [PLASTICITY_CREEP_LAW_TYPE.HYPERBOLIC_SINE]:
                lst_name = [
                    POWER_LAW_MULTIPLIER,
                    HYPER_LAW_MULTIPLIER,
                    EQ_STRESS_MULTIPLIER,
                    ACTIVATION_ENERGY,
                    UNIVERSAL_GAS_CONST,
                ]
            elif lawType in [PLASTICITY_CREEP_LAW_TYPE.ADVC_LAW]:
                lst_name = [C0, C1, C2, C3]
            else:
                lst_name = []
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1

            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )

            return cls(
                creep=params,
                lawType=lawType,
                suboption=suboption,
                advcLawType=advcLawType,
                advcHardenType=advcHardenType,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []
            listDataStr = []

            for i in range(1):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"creep=[{(', '.join(listDataStr))}]")

            listStr.append(f"lawType={str(self.lawType)}")
            listStr.append(f"suboption={str(self.suboption)}")
            listStr.append(f"advcHardenType={str(self.advcHardenType)}")
            listStr.append(f"advcLawType={str(self.advcLawType)}")

            if self.temperatureDependency:
                listStr.append(
                    f'temperatureDependency={"1" if self.temperatureDependency else "0"}'
                )
            if self.dependencies:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except Exception as e:
            raise NameError(
                f"Error in {self.__class__.__name__}.to_PSJ_str(): {str(e)}"
            )

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            if self.lawType in [
                PLASTICITY_CREEP_LAW_TYPE.STRAIN_HARDENING,
                PLASTICITY_CREEP_LAW_TYPE.TIME_HARDENING,
            ]:
                (
                    plm_data,
                    esm_data,
                    to_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                plm = plm_data[1]
                esm = esm_data[1]
                to = to_data[1]
                lst_name = [plm, esm, to]
            elif self.lawType in [PLASTICITY_CREEP_LAW_TYPE.HYPERBOLIC_SINE]:
                (
                    plm_data,
                    hlm_data,
                    esm_data,
                    ae_data,
                    ugc_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                plm = plm_data[1]
                hlm = hlm_data[1]
                esm = esm_data[1]
                ae = ae_data[1]
                ugc = ugc_data[1]
                lst_name = [plm, hlm, esm, ae, ugc]
            elif self.lawType in [PLASTICITY_CREEP_LAW_TYPE.ADVC_LAW]:
                lst_name = [C0, C1, C2, C3]
                (
                    c0_data,
                    c1_data,
                    c2_data,
                    c3_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                c0 = c0_data[1]
                c1 = c1_data[1]
                c2 = c2_data[1]
                c3 = c3_data[1]
                lst_name = [c0, c1, c2, c3]
            else:
                lst_name = []
                temp_data, extra_data = (TEMPERATURE, []), (EXTRA_FIELDS, [])

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]
            for row in range(self.table_data.row[0]):
                for d in lst_name:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                for i in range(len(extra)):
                    listTableDataStr.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])
            return mat_formatting(
                self.tmpl.format(
                    str(self.lawType),
                    str(self.suboption),
                    str(self.advcLawType),
                    str(self.advcHardenType),
                    str(self.temperatureDependency),
                    str(self.dependencies),
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if len(tableDataStr) > 0 else "",
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class RDNLK(MatPropBase):
    tmpl = """        <RDNLK PreDefinedMaterial=#{0}#></RDNLK>"""

    def __init__(self, predefinedMaterial=0, **kwargs):
        self.predefinedMaterial = predefinedMaterial
        # for param in []:
        #     kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        # super().__init__(**kwargs)
        # try:
        #     self.table_data = super().get_table_data()
        # except Exception as e:
        #     raise Exception(f"Error in get_table_data function of class {__class__.__name__}: {str(e)}") from e

    @classmethod
    def from_xml(cls, data: object) -> RDNLK:
        try:
            # Initialize data from object
            predefinedMaterial = int(data.attrib["PreDefinedMaterial"])

            return cls(
                predefinedMaterial=predefinedMaterial,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listStr.append(f"predefinedMaterial={str(self.predefinedMaterial)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            predefinedMaterial = str(self.predefinedMaterial)

            return mat_formatting(
                self.tmpl.format(
                    predefinedMaterial,
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Damping(MatPropBase, TableDamping):
    tmpl = """        <Damping Alpha=#{0}# Beta=#{1}# Composite=#{2}# Structural=#{3}#>
            <Table Row=#{4}# Col=#{5}#>
                <Data>{6}</Data>
            </Table>
        </Damping>"""

    def __init__(
        self,
        damping: list,
        alpha: float = None,
        beta: float = None,
        composite: float = None,
        structural: float = None,
        **kwargs,
    ):
        self.damping = damping
        self.alpha = alpha
        self.beta = beta
        self.composite = composite
        self.structural = structural
        for param in damping:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None
        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e
        # Re-define col of table, do when characteristic may have empty value in some required columns
        # min_col = 0
        # self.table_data.col[1] = min_col

    @classmethod
    def from_xml(cls, data: object) -> Damping:
        try:
            # Initialize data from object
            alpha = (
                float(data.attrib["Alpha"])
                if data.attrib["Alpha"] != "1.79769e+308"
                else None
            )
            beta = (
                float(data.attrib["Beta"])
                if data.attrib["Beta"] != "1.79769e+308"
                else None
            )
            composite = (
                float(data.attrib["Composite"])
                if data.attrib["Composite"] != "1.79769e+308"
                else None
            )
            structural = (
                float(data.attrib["Structural"])
                if data.attrib["Structural"] != "1.79769e+308"
                else None
            )

            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            if col > 0:
                idx = 0
                lst_name = [DAMPING, FREQUENCY]
                for i, NAME in enumerate(lst_name):
                    params.append((NAME, list_data[i])) if len(list_data) > i else (
                        NAME,
                        [],
                    )
                idx = len(lst_name)

            return cls(
                damping=params,
                alpha=alpha,
                beta=beta,
                composite=composite,
                structural=structural,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []
            if self.table_data.col[0] > 0:
                for name, data in self.table_data.data[0]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"damping=[{(', '.join(listDataStr))}]")

            if self.alpha is not None:
                listStr.append(f"alpha={str(self.alpha)}")
            if self.beta is not None:
                listStr.append(f"beta={str(self.beta)}")
            if self.composite is not None:
                listStr.append(f"composite={str(self.composite)}")
            if self.structural is not None:
                listStr.append(f"structural={str(self.structural)}")
            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except Exception as e:
            raise NameError(
                f"Error in {self.__class__.__name__}.to_PSJ_str(): {str(e)}"
            )

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            if self.table_data.col[0] > 0:
                (
                    damping_data,
                    frequency_data,
                ) = self.table_data.data[0]
                damping = damping_data[1]  # may need conversion for unit later
                frequency = frequency_data[1]  # may need conversion for unit later

                for row in range(self.table_data.row[0]):
                    for d in [damping, frequency]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[0])

            return mat_formatting(
                self.tmpl.format(
                    str(self.alpha) if self.alpha is not None else "1.79769e+308",
                    str(self.beta) if self.beta is not None else "1.79769e+308",
                    str(self.composite)
                    if self.composite is not None
                    else "1.79769e+308",
                    str(self.structural)
                    if self.structural is not None
                    else "1.79769e+308",
                    str(self.table_data.row[0]) if self.table_data.row[0] else "0",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "0",
                    tableDataStr,
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Rigid(MatPropBase):
    tmpl = """        <Rigid Translational=#{0}# Rotational=#{1}#></Rigid>"""

    def __init__(self, translational: int = None, rotational: int = None, **kwargs):
        self.translational = translational
        self.rotational = rotational
        # for param in []:
        #     kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        # for value in DICT_CHARACTERISTICS.values():
        #     if value.lower() not in kwargs:
        #         kwargs[value.lower()] = None

        # super().__init__(**kwargs)
        # try:
        #     self.table_data = super().get_table_data()
        # except Exception as e:
        #     raise Exception(f"Error in get_table_data function of class {__class__.__name__}: {str(e)}") from e

    @classmethod
    def from_xml(cls, data: object) -> Rigid:
        try:
            # Initialize data from object
            translational = (
                int(data.attrib["Translational"])
                if data.attrib["Translational"] != "2147483647"
                else None
            )
            rotational = (
                int(data.attrib["Rotational"])
                if data.attrib["Rotational"] != "2147483647"
                else None
            )

            return cls(
                translational=translational,
                rotational=rotational,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            if self.translational is not None:
                listStr.append(f"translational={str(self.translational)}")
            if self.rotational is not None:
                listStr.append(f"rotational={str(self.rotational)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            return mat_formatting(
                self.tmpl.format(
                    str(self.translational)
                    if self.translational is not None
                    else "2147483647",
                    str(self.rotational)
                    if self.rotational is not None
                    else "2147483647",
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class ViscoElastic(MatPropBase, TableViscoElastic):
    tmpl = """        <ViscoElastic TimeShiftTempDepend=#{0}# dependencies=#{1}#>
            <Table Row=#{2}# Col=#{3}#>
                <Data>{4}</Data>
            </Table>
            <Table Row=#{5}# Col=#{6}#>
                <Data>{7}</Data>
            </Table>
        </ViscoElastic>"""

    def __init__(
        self,
        viscoElastic: list,
        timeShiftTempDepend=False,
        timeShiftDependencies=0,
        **kwargs,
    ):
        self.timeShiftTempDepend = timeShiftTempDepend
        self.timeShiftDependencies = timeShiftDependencies
        for param in viscoElastic:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e
        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        if self.timeShiftTempDepend:
            min_col += 1
        min_col += self.timeShiftDependencies
        self.table_data.col[1] = min_col

    @classmethod
    def from_xml(cls, data: object) -> ViscoElastic:
        try:
            # Initialize data from object
            timeShiftTempDepend = data.attrib["TimeShiftTempDepend"] == "true"
            timeShiftDependencies = int(data.attrib["dependencies"])

            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [SHEAR_MODULUS, BULK_MODULUS, TIME_DELAY]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            [row, col], list_data = from_xml_to_list(data[1])
            idx = 0
            lst_name = [SHIFT_FACTOR]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if timeShiftTempDepend:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if timeShiftDependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - timeShiftDependencies, col)
                            ],
                        )
                    )
                )

            return cls(
                viscoElastic=params,
                timeShiftTempDepend=timeShiftTempDepend,
                timeShiftDependencies=timeShiftDependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []
            for i in range(2):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"viscoElastic=[{(', '.join(listDataStr))}]")

            if self.timeShiftTempDepend is True:
                listStr.append(f"timeShiftTempDepend={str(self.timeShiftTempDepend)}")
            if self.timeShiftDependencies != 0:
                listStr.append(
                    f"timeShiftDependencies={str(self.timeShiftDependencies)}"
                )
            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except Exception as e:
            raise NameError(
                f"Error in {self.__class__.__name__}.to_PSJ_str(): {str(e)}"
            )

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            (
                shear_data,
                bulk_data,
                time_delay_data,
            ) = self.table_data.data[0]
            shear = shear_data[1]  # may need conversion for unit later
            bulk = bulk_data[1]  # may need conversion for unit later
            time_delay = time_delay_data[1]

            for row in range(self.table_data.row[0]):
                for d in [shear, bulk, time_delay]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            # Time shift information
            tableDataStrTimeShift = ""
            listTableDataStrTimeShift = []

            (
                shift_factor_data,
                temp_data,
                extra_data,
            ) = self.table_data.data[1]
            shift = shift_factor_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]

            for row in range(self.table_data.row[1]):
                for d in [shift]:
                    listTableDataStrTimeShift.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStrTimeShift.append(" ")

                if self.timeShiftTempDepend:
                    listTableDataStrTimeShift.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStrTimeShift.append(" ")
                for i in range(len(extra)):
                    listTableDataStrTimeShift.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStrTimeShift = ",".join(listTableDataStrTimeShift)
            if not tableDataStrTimeShift:
                tableDataStrTimeShift = ",".join([" "] * self.table_data.col[1])

            timeShiftTempDepend = "true" if self.timeShiftTempDepend else "false"
            timeShiftDependencies = str(self.timeShiftDependencies)
            return mat_formatting(
                self.tmpl.format(
                    timeShiftTempDepend,
                    timeShiftDependencies,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                    str(self.table_data.row[1]) if self.table_data.row[1] else "1",
                    str(self.table_data.col[1]) if self.table_data.col[1] else "1",
                    tableDataStrTimeShift
                    if tableDataStrTimeShift[-1] != ","
                    else tableDataStrTimeShift[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Expansion(MatPropBase, TableExpansion):
    tmpl = """        <Expansion Type=#{0}# userSubroutine=#0# zero=#{1}# temperatureDependency=#{2}# dependencies=#{3}#>
            <Table Row=#{4}# Col=#{5}#>
                <Data>{6}</Data>
            </Table>
        </Expansion>"""

    def __init__(
        self,
        expansion: list,
        expansionType=0,
        temperatureReference=Union[None, float],
        temperatureDependency=False,
        dependencies=0,
        **kwargs,
    ):
        self.expansionType = expansionType
        self.temperatureReference = temperatureReference
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        for param in expansion:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        kwargs["expansionType"] = expansionType
        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        if self.expansionType == EXPANSION_TYPE.ISOTROPIC:
            min_col = 1
        elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_2D:
            min_col = 2
        elif self.expansionType in [
            EXPANSION_TYPE.ORTHOTROPIC_3D,
            EXPANSION_TYPE.ANISOTROPIC_2D,
        ]:
            min_col = 3
        elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_3D:
            min_col = 6
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: object) -> Expansion:
        try:
            # Initialize data from object
            expansionType = int(data.attrib["Type"])
            temperatureReference = (
                float(data.attrib["zero"])
                if data.attrib["zero"] != "1.79769e+308"
                else None
            )
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = []
            if expansionType == EXPANSION_TYPE.ISOTROPIC:
                lst_name = [ALPHA]
            elif expansionType == EXPANSION_TYPE.ORTHOTROPIC_2D:
                lst_name = [ALPHA11, ALPHA22]
            elif expansionType == EXPANSION_TYPE.ORTHOTROPIC_3D:
                lst_name = [ALPHA11, ALPHA22, ALPHA33]
            elif expansionType == EXPANSION_TYPE.ANISOTROPIC_2D:
                lst_name = [ALPHA11, ALPHA22, ALPHA12]
            elif expansionType == EXPANSION_TYPE.ANISOTROPIC_3D:
                lst_name = [ALPHA11, ALPHA22, ALPHA33, ALPHA12, ALPHA13, ALPHA23]

            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                expansion=params,
                expansionType=expansionType,
                temperatureReference=temperatureReference,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"expansion=[{(', '.join(listDataStr))}]")

            if self.expansionType != 0:
                listStr.append(f"expansionType={str(self.expansionType)}")

            if self.temperatureReference is not None:
                listStr.append(f"temperatureReference={str(self.temperatureReference)}")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            if self.expansionType == EXPANSION_TYPE.ISOTROPIC:
                alpha_data, temp_data, extra_data = self.table_data.data[0]
                alpha = alpha_data[1]
                lst = [alpha]
            elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_2D:
                (
                    alpha11_data,
                    alpha22_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                alpha11 = alpha11_data[1]
                alpha22 = alpha22_data[1]
                lst = [alpha11, alpha22]
            elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_3D:
                (
                    alpha11_data,
                    alpha22_data,
                    alpha33_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                alpha11 = alpha11_data[1]
                alpha22 = alpha22_data[1]
                alpha33 = alpha33_data[1]
                lst = [alpha11, alpha22, alpha33]
            elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_2D:
                (
                    alpha11_data,
                    alpha22_data,
                    alpha12_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                alpha11 = alpha11_data[1]
                alpha22 = alpha22_data[1]
                alpha12 = alpha12_data[1]
                lst = [alpha11, alpha22, alpha12]
            elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_3D:
                (
                    alpha11_data,
                    alpha22_data,
                    alpha33_data,
                    alpha12_data,
                    alpha13_data,
                    alpha23_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                alpha11 = alpha11_data[1]
                alpha22 = alpha22_data[1]
                alpha12 = alpha12_data[1]
                alpha33 = alpha33_data[1]
                alpha23 = alpha23_data[1]
                alpha13 = alpha13_data[1]
                lst = [alpha11, alpha22, alpha33, alpha12, alpha13, alpha23]

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]

            for row in range(self.table_data.row[0]):
                for d in lst:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                for i in range(len(extra)):
                    listTableDataStr.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)
            expanstionTypeStr = str(self.expansionType)
            tempRefStr = (
                str(
                    convert_mat_value_from_doc(
                        self.temperatureReference, JPT.UnitType.Unit_Temperature
                    )
                )
                if self.temperatureReference is not None
                else ""
            )

            return mat_formatting(
                self.tmpl.format(
                    expanstionTypeStr,
                    tempRefStr,
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Conductivity(MatPropBase, TableConductivity):
    tmpl = """        <Conductivity Type=#{0}# temperatureDependency=#{1}# dependencies=#{2}#>
            <Table Row=#{3}# Col=#{4}#>
                <Data>{5}</Data>
            </Table>
        </Conductivity>"""

    def __init__(
        self,
        conductivity: list,
        conductivityType=0,
        temperatureDependency=False,
        dependencies=0,
        **kwargs,
    ):
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        self.conductivityType = conductivityType
        kwargs["conductivityType"] = self.conductivityType
        for param in conductivity:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        if self.conductivityType in [CONDUCTIVITY_TYPE.ISOTROPIC]:
            min_col = 1
        elif self.conductivityType in [CONDUCTIVITY_TYPE.ORTHOTROPIC]:
            min_col = 3
        elif self.conductivityType in [CONDUCTIVITY_TYPE.ANISOTROPIC]:
            min_col = 6
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: object) -> Conductivity:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            conductivityType = int(data.attrib["Type"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = []
            if conductivityType == CONDUCTIVITY_TYPE.ISOTROPIC:
                lst_name = [CONDUCTIVITY]
            elif conductivityType == CONDUCTIVITY_TYPE.ORTHOTROPIC:
                lst_name = [K11, K22, K33]
            elif conductivityType == CONDUCTIVITY_TYPE.ANISOTROPIC:
                lst_name = [K11, K12, K22, K13, K23, K33]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                conductivity=params,
                conductivityType=conductivityType,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"conductivity=[{(', '.join(listDataStr))}]")

            if self.conductivityType != 0:
                listStr.append(f"conductivityType={str(self.conductivityType)}")
            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []
            if self.conductivityType == CONDUCTIVITY_TYPE.ISOTROPIC:
                conductivity_data, temp_data, extra_data = self.table_data.data[0]
                conductivity = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Stress)
                    for x in conductivity_data[1]
                ]
                temp = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                    for x in temp_data[1]
                ]
                extra = extra_data[1]

                for row in range(self.table_data.row[0]):
                    for d in [conductivity]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
            elif self.conductivityType == CONDUCTIVITY_TYPE.ORTHOTROPIC:
                (
                    k11_data,
                    k22_data,
                    k33_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                k11 = k11_data[1]
                k22 = k22_data[1]
                k33 = k33_data[1]
                temp = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                    for x in temp_data[1]
                ]
                extra = extra_data[1]

                for row in range(self.table_data.row[0]):
                    for d in [k11, k22, k33]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
            elif self.conductivityType == CONDUCTIVITY_TYPE.ANISOTROPIC:
                (
                    k11_data,
                    k12_data,
                    k22_data,
                    k13_data,
                    k23_data,
                    k33_data,
                    temp_data,
                    extra_data,
                ) = self.table_data.data[0]
                k11 = k11_data[1]
                k22 = k22_data[1]
                k33 = k33_data[1]
                k12 = k12_data[1]
                k13 = k13_data[1]
                k23 = k23_data[1]
                temp = [
                    convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                    for x in temp_data[1]
                ]
                extra = extra_data[1]

                for row in range(self.table_data.row[0]):
                    for d in [k11, k12, k22, k13, k23, k33]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                    if self.temperatureDependency:
                        listTableDataStr.append(
                            f"{str(temp[row]) if temp[row] is not None else ' '}"
                        ) if temp else listTableDataStr.append(" ")
                    for i in range(len(extra)):
                        listTableDataStr.append(
                            f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                        )
            else:
                raise ValueError(f"Invalid hardening type")
            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            conductivityTypeStr = str(self.conductivityType)
            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)

            return mat_formatting(
                self.tmpl.format(
                    conductivityTypeStr,
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class SpecificHeat(MatPropBase, TableSpecificHeat):
    tmpl = """        <SpecificHeat temperatureDependency=#{0}# dependencies=#{1}#>
            <Table Row=#{2}# Col=#{3}#>
                <Data>{4}</Data>
            </Table>
        </SpecificHeat>"""

    def __init__(
        self, specificHeat: list, temperatureDependency=False, dependencies=0, **kwargs
    ):
        self.specificHeat = specificHeat
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        for param in specificHeat:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: object) -> SpecificHeat:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [SPECIFIC_HEAT]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                specificHeat=params,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"specificHeat=[{(', '.join(listDataStr))}]")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            heat_data, temp_data, extra_data = self.table_data.data[0]
            heat = heat_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]

            for row in range(self.table_data.row[0]):
                for d in [heat]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                for i in range(len(extra)):
                    listTableDataStr.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)

            return mat_formatting(
                self.tmpl.format(
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class HeatGenerateRate(MatPropBase, TableHeatGenerateRate):
    tmpl = """        <HeatGenerateRate temperatureDependency=#{0}#>
            <Table Row=#{1}# Col=#{2}#>
                <Data>{3}</Data>
            </Table>
        </HeatGenerateRate>"""

    def __init__(self, heatGenerateRate: list, temperatureDependency=False, **kwargs):
        self.heatGenerateRate = heatGenerateRate
        self.temperatureDependency = temperatureDependency
        for param in heatGenerateRate:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1

    @classmethod
    def from_xml(cls, data: object) -> HeatGenerateRate:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [HEAT_GENERATE_RATE]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1

            return cls(
                heatGenerateRate=params,
                temperatureDependency=temperatureDependency,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"heatGenerateRate=[{(', '.join(listDataStr))}]")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            heat_gen_data, temp_data = self.table_data.data[0]
            heat_gen = heat_gen_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]

            for row in range(self.table_data.row[0]):
                for d in [heat_gen]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"

            return mat_formatting(
                self.tmpl.format(
                    tempDependStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class GasketMembraneElastic(MatPropBase, TableGasketMembraneElastic):
    tmpl = """        <GasketMembraneElastic temperatureDependency=#{0}# dependencies=#{1}#>
            <Table Row=#{2}# Col=#{3}#>
                <Data>{4}</Data>
            </Table>
        </GasketMembraneElastic>"""

    def __init__(
        self,
        gasketMembraneElastic: list,
        temperatureDependency=False,
        dependencies=0,
        **kwargs,
    ):
        self.gasketMembraneElastic = gasketMembraneElastic
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        for param in gasketMembraneElastic:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)

        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 2
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: object) -> GasketMembraneElastic:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [YOUNGS_MODULUS, POISSONS_RATIO]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                gasketMembraneElastic=params,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"gasketMembraneElastic=[{(', '.join(listDataStr))}]")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            young_data, poisson_data, temp_data, extra_data = self.table_data.data[0]
            young = young_data[1]  # may need conversion for unit later
            poisson = poisson_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]

            for row in range(self.table_data.row[0]):
                for d in [young, poisson]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                for i in range(len(extra)):
                    listTableDataStr.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)

            return mat_formatting(
                self.tmpl.format(
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class GasketTransverseElastic(MatPropBase, TableGasketTransverseElastic):
    tmpl = """        <GasketTransverseElastic TEUnit-H=#{0}# TEUnit-V=#{1}# TETempDepend-H=#{2}# TEDependency-H=#{3}# TETempDepend-V=#{4}# TEDependency-V=#{5}# >
            <Table Row=#{6}# Col=#{7}#>
                <Data>{8}</Data>
            </Table>
            <Table Row=#{9}# Col=#{10}#>
                <Data>{11}</Data>
            </Table>
        </GasketTransverseElastic>"""

    def __init__(
        self,
        gasketTransverseElastic: list,
        temperatureDependencyH=False,
        dependenciesH=0,
        unitH=0,
        temperatureDependencyV=False,
        dependenciesV=0,
        unitV=0,
        **kwargs,
    ):
        self.gasketTransverseElastic = gasketTransverseElastic
        self.temperatureDependencyV = temperatureDependencyV
        self.temperatureDependencyH = temperatureDependencyH
        self.dependenciesV = dependenciesV
        self.dependenciesH = dependenciesH
        self.unitV = unitV
        self.unitH = unitH
        for param in gasketTransverseElastic:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None
        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        self.table_data.col[0] = min_col
        self.table_data.col[1] = min_col

        if self.temperatureDependencyH:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependenciesH

        if self.temperatureDependencyV:
            self.table_data.col[1] += 1
        self.table_data.col[1] += self.dependenciesV

    @classmethod
    def from_xml(cls, data: object) -> GasketTransverseElastic:
        try:
            # Initialize data from object
            temperatureDependencyH = data.attrib["TETempDepend-H"] == "true"
            dependenciesH = int(data.attrib["TEDependency-H"])
            unitH = int(data.attrib["TEUnit-H"])
            temperatureDependencyV = data.attrib["TETempDepend-V"] == "true"
            dependenciesV = int(data.attrib["TEDependency-V"])
            unitV = int(data.attrib["TEUnit-V"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [SHEAR_STIFFNESS_H]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependencyH:
                params.append((TEMPERATURE_H, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE_H,
                    [],
                )
                idx += 1
            if dependenciesH:
                params.append(
                    (
                        (
                            EXTRA_FIELDS_H,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS_H, [])
                                for i in range(col - dependenciesH, col)
                            ],
                        )
                    )
                )

            [row, col], list_data = from_xml_to_list(data[1])
            idx = 0
            lst_name = [SHEAR_STIFFNESS_V]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependencyV:
                params.append((TEMPERATURE_V, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE_V,
                    [],
                )
                idx += 1
            if dependenciesV:
                params.append(
                    (
                        (
                            EXTRA_FIELDS_V,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS_V, [])
                                for i in range(col - dependenciesV, col)
                            ],
                        )
                    )
                )
            return cls(
                gasketTransverseElastic=params,
                temperatureDependencyH=temperatureDependencyH,
                temperatureDependencyV=temperatureDependencyV,
                unitH=unitH,
                dependenciesH=dependenciesH,
                dependenciesV=dependenciesV,
                unitV=unitV,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []
            for i in range(2):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"gasketTransverseElastic=[{(', '.join(listDataStr))}]")

            if self.unitH != 0:
                listStr.append(f"unitH={str(self.unitH)}")
            if self.temperatureDependencyH:
                listStr.append(
                    f"temperatureDependencyH={str(self.temperatureDependencyH)}"
                )
            if self.dependenciesH != 0:
                listStr.append(f"dependenciesH={str(self.dependenciesH)}")

            if self.unitV != 0:
                listStr.append(f"unitV={str(self.unitV)}")
            if self.temperatureDependencyV:
                listStr.append(
                    f"temperatureDependencyV={str(self.temperatureDependencyV)}"
                )
            if self.dependenciesV != 0:
                listStr.append(f"dependenciesV={str(self.dependenciesV)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            shear_data_h, temp_data_h, extra_data_h = self.table_data.data[0]
            # may need conversion for unit later
            shear_stiffness_h = shear_data_h[1]

            temp_h = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data_h[1]
            ]
            extra_h = extra_data_h[1]

            for row in range(self.table_data.row[0]):
                for d in [shear_stiffness_h]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependencyH:
                    listTableDataStr.append(
                        f"{str(temp_h[row]) if temp_h[row] is not None else ' '}"
                    ) if temp_h else listTableDataStr.append(" ")
                for i in range(len(extra_h)):
                    listTableDataStr.append(
                        f"{str(extra_h[i][row]) if extra_h[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            # Vertical information
            tableDataStrV = ""
            listTableDataStrV = []

            shear_data_v, temp_data_v, extra_data_v = self.table_data.data[1]
            # may need conversion for unit later
            shear_stiffness_v = shear_data_v[1]

            temp_v = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data_v[1]
            ]
            extra_v = extra_data_v[1]

            for row in range(self.table_data.row[1]):
                for d in [shear_stiffness_v]:
                    listTableDataStrV.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStrV.append(" ")

                if self.temperatureDependencyV:
                    listTableDataStrV.append(
                        f"{str(temp_v[row]) if temp_v[row] is not None else ' '}"
                    ) if temp_v else listTableDataStrV.append(" ")
                for i in range(len(extra_v)):
                    listTableDataStrV.append(
                        f"{str(extra_v[i][row]) if extra_v[i][row] is not None else ' '}"
                    )

            tableDataStrV = ",".join(listTableDataStrV)
            if not tableDataStrV:
                tableDataStrV = ",".join([" "] * self.table_data.col[1])

            tempDependHStr = "true" if self.temperatureDependencyH else "false"
            dependenciesHStr = str(self.dependenciesH)
            unitHStr = str(self.unitH)
            tempDependVStr = "true" if self.temperatureDependencyV else "false"
            dependenciesVStr = str(self.dependenciesV)
            unitVStr = str(self.unitV)

            return mat_formatting(
                self.tmpl.format(
                    unitHStr,
                    unitVStr,
                    tempDependHStr,
                    dependenciesHStr,
                    tempDependVStr,
                    dependenciesVStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                    str(self.table_data.row[1]) if self.table_data.row[1] else "1",
                    str(self.table_data.col[1]) if self.table_data.col[1] else "1",
                    tableDataStrV if tableDataStrV[-1] != "," else tableDataStrV[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class GasketThickness(MatPropBase, TableGasketThickness):
    tmpl = """        <GasketThickness Type=#{0}# unit=#{1}# YieldOnsetMethod=#{2}# YieldOnset=#{3}# TBTensileType=#{4}# TBTensileValue=#{5}# TBLoadingTempDepend=#{6}# TBLoadingDependency=#{7}# unloadingTemperatureDependency=#{8}# unloadingDependencies=#{9}# TBUnLoadingIncludeCurve=#{10}#>
            <LoadingCurve>
                <Table Row=#{11}# Col=#{12}#>
                    <Data>{13}</Data>
                </Table>
            </LoadingCurve>
            <UnLoadingCurve>
                <Table Row=#{14}# Col=#{15}#>
                    <Data>{16}</Data>
                </Table>
            </UnLoadingCurve>
        </GasketThickness>"""

    def __init__(
        self,
        gasketThickness: list,
        type=0,
        unit=0,
        yieldMethod=0,
        yieldValue=0.1,
        tensileType=0,
        tensileValue=0.001,
        loadingTempDepend=False,
        loadingDependency=0,
        unloadingTempDepend=False,
        unloadingDependency=0,
        unloadingIncludeCurve=False,
        **kwargs,
    ):
        self.gasketThickness = gasketThickness
        self.type = type
        self.unit = unit
        self.yieldMethod = yieldMethod
        self.yieldValue = yieldValue
        self.tensileType = tensileType
        self.tensileValue = tensileValue
        self.loadingTempDepend = loadingTempDepend
        self.loadingDependency = loadingDependency
        self.unloadingTempDepend = unloadingTempDepend
        self.unloadingDependency = unloadingDependency
        self.unloadingIncludeCurve = unloadingIncludeCurve
        for param in gasketThickness:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)
        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e
        # Re-define col of table, do when characteristic may have empty value in some required columns
        self.table_data.col[0] = 2
        self.table_data.col[1] = 3

        if self.loadingTempDepend:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.loadingDependency

        if self.unloadingTempDepend:
            self.table_data.col[1] += 1
        self.table_data.col[1] += self.unloadingDependency

    @classmethod
    def from_xml(cls, data: object) -> GasketThickness:
        try:
            # Initialize data from object
            _type = int(data.attrib["Type"])
            unit = int(data.attrib["unit"])
            yieldMethod = int(data.attrib["YieldOnsetMethod"])
            yieldValue = data.attrib["YieldOnset"]
            tensileType = int(data.attrib["TBTensileType"])
            tensileValue = data.attrib["TBTensileValue"]
            loadingTempDepend = data.attrib["TBLoadingTempDepend"] == "true"
            loadingDependency = int(data.attrib["TBLoadingDependency"])
            unloadingTempDepend = (
                data.attrib["unloadingTemperatureDependency"] == "true"
            )
            unloadingDependency = int(data.attrib["unloadingDependencies"])
            unloadingIncludeCurve = data.attrib["TBUnLoadingIncludeCurve"] == "true"

            params = []
            [row, col], list_data = from_xml_to_list(data[0][0])
            idx = 0
            lst_name = [PRESSURE_FORCE_LOADING, CLOSURE_LOADING]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if loadingTempDepend:
                params.append((TEMPERATURE_LOADING, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE_LOADING,
                    [],
                )
                idx += 1
            if loadingDependency:
                params.append(
                    (
                        (
                            EXTRA_FIELDS_LOADING,
                            [
                                list_data[i]
                                if list_data[i]
                                else (EXTRA_FIELDS_LOADING, [])
                                for i in range(col - loadingDependency, col)
                            ],
                        )
                    )
                )

            if unloadingIncludeCurve:
                [row, col], list_data = from_xml_to_list(data[1][0])
                idx = 0
                lst_name = [
                    PRESSURE_FORCE_UNLOADING,
                    CLOSURE_UNLOADING,
                    PLASTIC_MAX_CLOSURE_UNLOADING,
                ]
                for i, NAME in enumerate(lst_name):
                    params.append((NAME, list_data[i])) if len(list_data) > i else (
                        NAME,
                        [],
                    )
                idx = len(lst_name)

                if unloadingTempDepend:
                    params.append((TEMPERATURE_UNLOADING, list_data[idx])) if len(
                        list_data
                    ) > idx else (
                        TEMPERATURE_UNLOADING,
                        [],
                    )
                    idx += 1
                if unloadingDependency:
                    params.append(
                        (
                            (
                                EXTRA_FIELDS_UNLOADING,
                                [
                                    list_data[i]
                                    if list_data[i]
                                    else (EXTRA_FIELDS_UNLOADING, [])
                                    for i in range(col - unloadingDependency, col)
                                ],
                            )
                        )
                    )
            return cls(
                gasketThickness=params,
                type=_type,
                unit=unit,
                yieldMethod=yieldMethod,
                yieldValue=yieldValue,
                tensileType=tensileType,
                tensileValue=tensileValue,
                loadingTempDepend=loadingTempDepend,
                loadingDependency=loadingDependency,
                unloadingTempDepend=unloadingTempDepend,
                unloadingDependency=unloadingDependency,
                unloadingIncludeCurve=unloadingIncludeCurve,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []
            for i in range(2):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"gasketThickness=[{(', '.join(listDataStr))}]")

            if self.type != 0:
                listStr.append(f"type={str(self.type)}")
            if self.unit != 0:
                listStr.append(f"unit={str(self.unit)}")
            if self.yieldMethod != 0:
                listStr.append(f"yieldMethod={str(self.yieldMethod)}")
            listStr.append(f"yieldValue={str(self.yieldValue)}")
            if self.tensileType != 0:
                listStr.append(f"tensileType={str(self.tensileType)}")
            listStr.append(f"tensileValue={str(self.tensileValue)}")
            if self.loadingTempDepend:
                listStr.append(f"loadingTempDepend={str(self.loadingTempDepend)}")
            if self.unloadingTempDepend:
                listStr.append(f"unloadingTempDepend={str(self.unloadingTempDepend)}")
            if self.loadingDependency != 0:
                listStr.append(f"loadingDependency={str(self.loadingDependency)}")
            if self.unloadingDependency != 0:
                listStr.append(f"unloadingDependency={str(self.unloadingDependency)}")
            if self.unloadingIncludeCurve:
                listStr.append(
                    f"unloadingIncludeCurve={str(self.unloadingIncludeCurve)}"
                )
            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            (
                pressure_data,
                closure_data,
                temp_data_load,
                extra_data_load,
            ) = self.table_data.data[0]
            pressure = pressure_data[1]  # may need conversion for unit later
            closure = closure_data[1]  # may need conversion for unit later

            temp_loading = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data_load[1]
            ]
            extra_loading = extra_data_load[1]

            for row in range(self.table_data.row[0]):
                for d in [pressure, closure]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.loadingTempDepend:
                    listTableDataStr.append(
                        f"{str(temp_loading[row]) if temp_loading[row] is not None else ' '}"
                    ) if temp_loading else listTableDataStr.append(" ")
                for i in range(len(extra_loading)):
                    listTableDataStr.append(
                        f"{str(extra_loading[i][row]) if extra_loading[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            # Vertical information
            tableDataStrUnload = ""
            listTableDataStrUnload = []

            (
                pressure_data,
                closure_data,
                max_closure_data,
                temp_data_unload,
                extra_data_unload,
            ) = self.table_data.data[1]
            pressure = pressure_data[1]  # may need conversion for unit later
            closure = closure_data[1]  # may need conversion for unit later
            # may need conversion for unit later
            max_closure = max_closure_data[1]

            temp_unload = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data_unload[1]
            ]
            extra_unload = extra_data_unload[1]

            for row in range(self.table_data.row[1]):
                for d in [pressure, closure, max_closure]:
                    listTableDataStrUnload.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStrUnload.append(" ")

                if self.unloadingTempDepend:
                    listTableDataStrUnload.append(
                        f"{str(temp_unload[row]) if temp_unload[row] is not None else ' '}"
                    ) if temp_unload else listTableDataStrUnload.append(" ")
                for i in range(len(extra_unload)):
                    listTableDataStrUnload.append(
                        f"{str(extra_unload[i][row]) if extra_unload[i][row] is not None else ' '}"
                    )

            tableDataStrUnload = ",".join(listTableDataStrUnload)
            if not tableDataStrUnload:
                tableDataStrUnload = ",".join([" "] * self.table_data.col[1])

            typeStr = str(self.type)
            unitStr = str(self.unit)
            yieldMethodStr = str(self.yieldMethod)
            yieldValueStr = str(self.yieldValue)
            tensileTypeStr = str(self.tensileType)
            tensileValueStr = str(self.tensileValue)
            loadingTempDependStr = "true" if self.loadingTempDepend else "false"
            loadingDependencyStr = str(self.loadingDependency)
            unloadingTempDependStr = "true" if self.unloadingTempDepend else "false"
            unloadingDependencyStr = str(self.unloadingDependency)
            unloadingIncludeCurveStr = "true" if self.unloadingIncludeCurve else "false"
            return mat_formatting(
                self.tmpl.format(
                    typeStr,
                    unitStr,
                    yieldMethodStr,
                    yieldValueStr,
                    tensileTypeStr,
                    tensileValueStr,
                    loadingTempDependStr,
                    loadingDependencyStr,
                    unloadingTempDependStr,
                    unloadingDependencyStr,
                    unloadingIncludeCurveStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                    str(self.table_data.row[1]) if self.table_data.row[1] else "1",
                    str(self.table_data.col[1]) if self.table_data.col[1] else "1",
                    tableDataStrUnload
                    if tableDataStrUnload[-1] != ","
                    else tableDataStrUnload[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class GasketAdditionalBehavior(MatPropBase):
    tmpl = """        <GasketAdditionalBehavior InitialGap=#{0}#></GasketAdditionalBehavior>"""

    def __init__(self, initialGap=0.0, **kwargs):
        self.initialGap = initialGap
        # for param in []:
        #     kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        # super().__init__(**kwargs)
        # try:
        #     self.table_data = super().get_table_data()
        # except Exception as e:
        #     raise Exception(f"Error in get_table_data function of class {__class__.__name__}: {str(e)}") from e

    @classmethod
    def from_xml(cls, data: object) -> GasketAdditionalBehavior:
        try:
            # Initialize data from object
            initialGap = float(data.attrib["InitialGap"])

            return cls(
                initialGap=initialGap,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listStr.append(f"initialGap={str(self.initialGap)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            initialGapStr = str(self.initialGap)

            return mat_formatting(
                self.tmpl.format(
                    initialGapStr,
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class StructuralViscosity(MatPropBase, TableViscosity):
    tmpl = """        <StructuralViscosity Type=#{0}# temperatureDependency=#{1}# dependencies=#{2}#>
            <Table Row=#{3}# Col=#{4}#>
                <Data>{5}</Data>
            </Table>
        </StructuralViscosity>"""

    def __init__(
        self,
        viscosity: list,
        viscosityType=0,
        temperatureDependency=False,
        dependencies=0,
        **kwargs,
    ):
        self.viscosity = viscosity
        self.viscosityType = viscosityType
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        for param in viscosity:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)

        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 1
        self.table_data.col[0] = min_col

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: object) -> StructuralViscosity:
        try:
            # Initialize data from object
            _type = int(data.attrib["Type"])
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [VISCOSITY]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                viscosity=params,
                viscosityType=_type,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"viscosity=[{(', '.join(listDataStr))}]")

            if self.viscosityType != 0:
                listStr.append(f"viscosityType={str(self.viscosityType)}")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            viscosity_data, temp_data, extra_data = self.table_data.data[0]
            viscosity = viscosity_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]

            for row in range(self.table_data.row[0]):
                for d in [viscosity]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                for i in range(len(extra)):
                    listTableDataStr.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)
            viscosityTypeStr = str(self.viscosityType)

            return mat_formatting(
                self.tmpl.format(
                    viscosityTypeStr,
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Cohesive(MatPropBase, TableCohesive):
    tmpl = """        <Cohesive>
            {0}
            {1}
            {2}
            {3}
            {4}
            {5}
        </Cohesive>"""
    tmpl_table = """            <Table Row=#{0}# Col=#{1}# Index=#{2}#>
                <Data>{3}</Data>
            </Table>"""

    def __init__(
        self,
        cohesive: list,
        **kwargs,
    ):
        self.cohesive = cohesive
        for param in cohesive:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)

        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        min_col = 2
        self.table_data.col[0] = min_col
        self.table_data.col[1] = min_col
        self.table_data.col[2] = min_col
        self.table_data.col[3] = min_col
        self.table_data.col[4] = min_col
        self.table_data.col[5] = min_col

    @classmethod
    def from_xml(cls, data: object) -> StructuralViscosity:
        try:
            # Initialize data from object
            params = []
            tpl_lst_name = [
                [STRESS_L, STRAIN_L],
                [STRESS_T, STRAIN_T],
                [STRESS_Z, STRAIN_Z],
                [STRESS_LT, STRAIN_LT],
                [STRESS_TZ, STRAIN_TZ],
                [STRESS_ZL, STRAIN_ZL],
            ]
            for i, lst_name in enumerate(tpl_lst_name):
                [row, col], list_data = from_xml_to_list(data[i])
                for i, NAME in enumerate(lst_name):
                    params.append((NAME, list_data[i])) if len(list_data) > i else (
                        NAME,
                        [],
                    )

            return cls(
                cohesive=params,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []
            for i in range(6):
                for name, data in self.table_data.data[i]:
                    if data and not all(isinstance(val, type(None)) for val in data):
                        listDataStr.append(
                            f"({DICT_CHARACTERISTICS[name]}, {str(data)})"
                        )
            listStr.append(f"cohesive=[{(', '.join(listDataStr))}]")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            n_table = 6
            tmpl_table_format = [""] * n_table

            for i in range(n_table):
                tableDataStr = ""
                listTableDataStr = []
                stress_data, strain_data = self.table_data.data[i]
                stress = stress_data[1]  # may need conversion for unit later
                strain = strain_data[1]  # may need conversion for unit later

                for row in range(self.table_data.row[i]):
                    for d in [stress, strain]:
                        listTableDataStr.append(
                            f"{str(d[row]) if d[row] is not None else ' '}"
                        ) if d else listTableDataStr.append(" ")

                tableDataStr = ",".join(listTableDataStr)
                if not tableDataStr:
                    tableDataStr = ",".join([" "] * self.table_data.col[i])

                tmpl_table_format[i] = self.tmpl_table.format(
                    str(self.table_data.row[i]) if self.table_data.row[i] else "1",
                    str(self.table_data.col[i]) if self.table_data.col[i] else "1",
                    str(i),
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                )

            return mat_formatting(
                self.tmpl.format(*tmpl_table_format),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class Resistivity(MatPropBase, TableResistivity):
    tmpl = """        <Resistivity Type=#0# temperatureDependency=#{0}#>
        <Table Row=#{1}# Col=#{2}#>
            <Data>{3}</Data>
        </Table>
    </Resistivity>"""

    def __init__(
        self,
        resistivity: list,
        temperatureDependency=False,
        **kwargs,
    ):
        self.resistivity = resistivity
        self.temperatureDependency = temperatureDependency
        for param in resistivity:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)

        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        self.table_data.col[0] = 1

        if self.temperatureDependency:
            self.table_data.col[0] += 1

    @classmethod
    def from_xml(cls, data: object) -> FatigueLimitDiagram:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [RESISTIVITY]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1

            return cls(
                resistivity=params,
                temperatureDependency=temperatureDependency,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"resistivity=[{(', '.join(listDataStr))}]")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            resist_data, temp_data = self.table_data.data[0]
            resist = resist_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]

            for row in range(self.table_data.row[0]):
                for d in [resist]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"

            return mat_formatting(
                self.tmpl.format(
                    tempDependStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr,
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


class FatigueLimitDiagram(MatPropBase, TableFatigueLimitDiagram):
    tmpl = """        <FatigueLimitDiagram temperatureDependency=#{0}# dependencies=#{1}#>
        <Table Row=#{2}# Col=#{3}#>
            <Data>{4}</Data>
        </Table>
    </FatigueLimitDiagram>"""

    def __init__(
        self,
        limitDiagram: list,
        temperatureDependency=False,
        dependencies=0,
        **kwargs,
    ):
        self.limitDiagram = limitDiagram
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
        for param in limitDiagram:
            kwargs[DICT_CHARACTERISTICS[param[0]].lower()] = param
        for value in DICT_CHARACTERISTICS.values():
            if value.lower() not in kwargs:
                kwargs[value.lower()] = None

        super().__init__(**kwargs)

        try:
            self.table_data = super().get_table_data()
        except Exception as e:
            raise Exception(
                f"Error in get_table_data function of class {__class__.__name__}: {str(e)}"
            ) from e

        # Re-define col of table, do when characteristic may have empty value in some required columns
        self.table_data.col[0] = 2

        if self.temperatureDependency:
            self.table_data.col[0] += 1
        self.table_data.col[0] += self.dependencies

    @classmethod
    def from_xml(cls, data: object) -> FatigueLimitDiagram:
        try:
            # Initialize data from object
            temperatureDependency = data.attrib["temperatureDependency"] == "1"
            dependencies = int(data.attrib["dependencies"])
            params = []
            [row, col], list_data = from_xml_to_list(data[0])
            idx = 0
            lst_name = [MEAN_STRESS, STRESS_AMPLITUDE]
            for i, NAME in enumerate(lst_name):
                params.append((NAME, list_data[i])) if len(list_data) > i else (
                    NAME,
                    [],
                )
            idx = len(lst_name)

            if temperatureDependency:
                params.append((TEMPERATURE, list_data[idx])) if len(
                    list_data
                ) > idx else (
                    TEMPERATURE,
                    [],
                )
                idx += 1
            if dependencies:
                params.append(
                    (
                        (
                            EXTRA_FIELDS,
                            [
                                list_data[i] if list_data[i] else (EXTRA_FIELDS, [])
                                for i in range(col - dependencies, col)
                            ],
                        )
                    )
                )
            return cls(
                limitDiagram=params,
                temperatureDependency=temperatureDependency,
                dependencies=dependencies,
            )
        except Exception as e:
            raise SyntaxError(f"Error in {cls.__class__.__name__}.from_xml(): {str(e)}")

    def to_PSJ_str(self) -> str:
        try:
            strPSJ = f"{self.__class__.__name__}"
            strPSJ += "("
            listStr = []

            listDataStr = []

            for name, data in self.table_data.data[0]:
                if data and not all(isinstance(val, type(None)) for val in data):
                    listDataStr.append(f"({DICT_CHARACTERISTICS[name]}, {str(data)})")
            listStr.append(f"limitDiagram=[{(', '.join(listDataStr))}]")

            if self.temperatureDependency:
                listStr.append(
                    f"temperatureDependency={str(self.temperatureDependency)}"
                )
            if self.dependencies != 0:
                listStr.append(f"dependencies={str(self.dependencies)}")

            strPSJ += f'{", ".join(listStr)}'
            strPSJ += ")"
            return strPSJ
        except:
            raise NameError(f"Error in {self.__class__.__name__}.to_PSJ_str()")

    def toStr(self, replace_str):
        try:
            tableDataStr = ""
            listTableDataStr = []

            stress_data, ampl_data, temp_data, extra_data = self.table_data.data[0]
            stress = stress_data[1]  # may need conversion for unit later
            ampl = ampl_data[1]  # may need conversion for unit later

            temp = [
                convert_mat_value_from_doc(x, JPT.UnitType.Unit_Temperature)
                for x in temp_data[1]
            ]
            extra = extra_data[1]

            for row in range(self.table_data.row[0]):
                for d in [stress, ampl]:
                    listTableDataStr.append(
                        f"{str(d[row]) if d[row] is not None else ' '}"
                    ) if d else listTableDataStr.append(" ")

                if self.temperatureDependency:
                    listTableDataStr.append(
                        f"{str(temp[row]) if temp[row] is not None else ' '}"
                    ) if temp else listTableDataStr.append(" ")
                for i in range(len(extra)):
                    listTableDataStr.append(
                        f"{str(extra[i][row]) if extra[i][row] is not None else ' '}"
                    )

            tableDataStr = ",".join(listTableDataStr)
            if not tableDataStr:
                tableDataStr = ",".join([" "] * self.table_data.col[0])

            tempDependStr = "1" if self.temperatureDependency else "0"
            dependenciesStr = str(self.dependencies)

            return mat_formatting(
                self.tmpl.format(
                    tempDependStr,
                    dependenciesStr,
                    str(self.table_data.row[0]) if self.table_data.row[0] else "1",
                    str(self.table_data.col[0]) if self.table_data.col[0] else "1",
                    tableDataStr if tableDataStr[-1] != "," else tableDataStr[:-1],
                ),
                replace_str,
            )
        except Exception as e:
            raise NameError(f"Error in {self.__class__.__name__}.toStr(): {str(e)}")

    def __str__(self):
        return self.toStr(self.replace_str)

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    d1 = Density([(DENSITY, 8300.0)])
    p1 = Elastic([(YOUNGS_MODULUS, 110000.0), (POISSONS_RATIO, 0.34)])
    p2 = Elastic(
        [
            [(YOUNGS_MODULUS, 110000.0), (POISSONS_RATIO, 0.34), (TEMPERATURE, 20.0)],
            [(YOUNGS_MODULUS, 220000.0), (POISSONS_RATIO, 0.35), (TEMPERATURE, 100.0)],
        ],
        temperatureDependency=True,
    )
    mat1 = CMaterial("STEEL", 1, 0, [d1, p1])
    str_len = len(str(mat1))
    print(mat1)
    print(str_len)

