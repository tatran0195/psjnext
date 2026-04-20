from jupiterutils.Utility import JPT
from typing import Union
from enum import IntEnum, Enum


class ELASTIC_TYPE(IntEnum):
    ISOTROPIC = 0
    ORTHOTROPIC_2D = 1
    ORTHOTROPIC_3D_TYPE_1 = 2
    ORTHOTROPIC_3D_TYPE_2 = 3
    ANISOTROPIC_2D = 4
    ANISOTROPIC_3D = 5
    LAMINA = 6
    TRACTION = 7
    COUPLED_TRACTION = 8
    SHORT_FIBER = 9


class PLASTIC_HARDENING(IntEnum):
    ISOTROPIC = 0
    KINEMATIC = 1
    JOHNSON_COOK = 2
    USER = 3
    COMBINED = 4


class CONDUCTIVITY_TYPE(IntEnum):
    ISOTROPIC = 0
    ORTHOTROPIC = 1
    ANISOTROPIC = 2


class EXPANSION_TYPE(IntEnum):
    ISOTROPIC = 0
    ORTHOTROPIC_2D = 1
    ORTHOTROPIC_3D = 2
    ANISOTROPIC_2D = 4  # This is not typo, JPT defines like this
    ANISOTROPIC_3D = 5  # This is not typo, JPT defines like this


class HYPERELASTIC_TYPE(str, Enum):
    ARRUDA_BOYCE = "ARRUDA_BOYCE"
    MARLOW = "MARLOW"
    MOONEY_RIVLIN = "MOONEY_RIVLIN"
    NEO_HOOKE = "NEO_HOOKE"
    OGDEN = "OGDEN"
    POLYNOMIAL = "POLYNOMIAL"
    REDUCED_POLYNOMIAL = "REDUCED_POLYNOMIAL"
    USER = "USER"
    VAN_DER_WAALS = "VAN_DER_WAALS"
    YEOH = "YEOH"
    UNKNOWN = "UNKNOWN"

    def __str__(self):
        return self.value


class HYPERELASTIC_MODULI(str, Enum):
    LONG_TERM = "LONG_TERM"
    INSTANTANEOUS = "INSTANTANEOUS"

    def __str__(self):
        return self.value


class HYPERELASTIC_BETA(str, Enum):
    FITTED_VAL = "FITTED_VAL"
    SPECIFY = "SPECIFY"

    def __str__(self):
        return self.value


class HYPERELASTIC_VOLUMETRICRESPONSE(str, Enum):
    DEFAULT = "DEFAULT"
    VOLUMETRIC_DATA = "VOLUMETRIC_DATA"
    POISSON_RATIO = "POISSON_RATIO"
    LATERAL_NOMINAL_STRAIN = "LATERAL_NOMINAL_STRAIN"

    def __str__(self):
        return self.value


class HYPERELASTIC_DEVIATORICRESPONSE(str, Enum):
    UNIAXIAL = "UNIAXIAL"
    BIAXIAL = "BIAXIAL"
    PLANAR = "PLANAR"

    def __str__(self):
        return self.value


class PLASTICITY_CREEP_LAW_TYPE(IntEnum):
    STRAIN_HARDENING = 0
    TIME_HARDENING = 1
    HYPERBOLIC_SINE = 2
    USER = 3
    ADVC_LAW = 4


[
    DENSITY,
    YOUNGS_MODULUS,
    SHEAR_MODULUS,
    POISSONS_RATIO,
    NASTRAN_FAILURE_INDEX_TENSION,
    NASTRAN_FAILURE_INDEX_COMPRESSION,
    NASTRAN_FAILURE_INDEX_SHEAR,
    E1,
    E2,
    E3,
    E4,
    E5,
    E6,
    G12,
    G1Z,
    G2Z,
    G13,
    G23,
    NU12,
    NU13,
    NU23,
    XT,
    XC,
    YT,
    YC,
    S,
    F12,
    STRN,
    D1111,
    D1122,
    D2222,
    D1133,
    D2233,
    D3333,
    D1212,
    D1313,
    D2323,
    EKNN,
    G1KSS,
    G2KTT,
    STRESS,
    STRAIN,
    A,
    B,
    M,
    N,
    MELTING_TEMP,
    TRANSITION_TEMP,
    HARDENING_PROP,
    GAMMA,
    HARD_PARAM,
    CONDUCTIVITY,
    K11,
    K22,
    K33,
    K12,
    K13,
    K23,
    SPECIFIC_HEAT,
    HEAT_GENERATE_RATE,
    EQUIV_STRESS,
    EQUIV_STRAIN,
    Q_INFINITY,
    PRESSURE_FORCE_LOADING,
    CLOSURE_LOADING,
    PRESSURE_FORCE_UNLOADING,
    CLOSURE_UNLOADING,
    PLASTIC_MAX_CLOSURE_UNLOADING,
    HARDENING_B,
    ALPHA,
    ALPHA11,
    ALPHA22,
    ALPHA33,
    ALPHA12,
    ALPHA23,
    ALPHA13,
    BULK_MODULUS,
    TIME_DELAY,
    SHIFT_FACTOR,
    VISCOSITY,
    STRESS_L,
    STRAIN_L,
    STRESS_T,
    STRAIN_T,
    STRESS_Z,
    STRAIN_Z,
    STRESS_LT,
    STRAIN_LT,
    STRESS_TZ,
    STRAIN_TZ,
    STRESS_ZL,
    STRAIN_ZL,
    MU,
    LAMDA_M,
    D,
    C10,
    C01,
    D1,
    MU1,
    ALPHA1,
    BETA,
    C0,
    C1,
    C2,
    C3,
    C20,
    C30,
    D1,
    D2,
    D3,
    NOMIAL_STRESS,
    NOMIAL_STRAIN,
    LATERAL_NOMIAL_STRAIN,
    TIME,
    STRESS_COMPRESSION,
    STRESS_TENSION,
    STRAIN_COMPRESSION,
    STRAIN_TENSION,
    POWER_LAW_MULTIPLIER,
    HYPER_LAW_MULTIPLIER,
    EQ_STRESS_MULTIPLIER,
    EQ_STRESS_ORDER,
    UNIVERSAL_GAS_CONST,
    ACTIVATION_ENERGY,
    TIME_ORDER,
    MEAN_STRESS,
    STRESS_AMPLITUDE,
    DAMPING,
    RESISTIVITY,
    FREQUENCY,
    TEMPERATURE,
    TEMPERATURE_H,
    TEMPERATURE_V,
    TEMPERATURE_SUB,
    TEMPERATURE_LOADING,
    TEMPERATURE_UNLOADING,
    TEMPERATURE_UNIAXIAL,
    SHEAR_STIFFNESS_H,
    SHEAR_STIFFNESS_V,
    FREQUENCY_DEPENDENCE,
    STRAIN_RATE,
    STRAIN_RATE_COMPRESSION,
    STRAIN_RATE_TENSION,
    EXTRA_FIELDS,
    EXTRA_FIELDS_H,
    EXTRA_FIELDS_V,
    EXTRA_FIELDS_SUB,
    EXTRA_FIELDS_LOADING,
    EXTRA_FIELDS_UNLOADING,
    EXTRA_FIELDS_UNIAXIAL,
    EXTRA_FIELDS_COMPRESSION,
    EXTRA_FIELDS_TENSION,
] = CHARACTERISTICS = range(152)

DICT_CHARACTERISTICS = dict()

module_vars = dict(vars())
for name, value in module_vars.items():
    if value in CHARACTERISTICS:
        DICT_CHARACTERISTICS[value] = name


def NONE_TUPLE(n=2):
    return tuple(None for i in range(n))


class Table:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ...

    def get_table_data(**kwargs) -> None:
        return None
        ...

    def get_data(self, val):
        if isinstance(val, list):
            oo = val
        elif isinstance(val, Union[float, int]):
            oo = [val]
        else:
            raise ValueError
        return oo

    def make_backwards_compatibility(self, character: Union[tuple, None]):
        if isinstance(character, tuple) and len(character) == 2:
            if not isinstance(character[1], list):
                character = tuple((character[0], [character[1]]))
        return character
        ...


class TableData:
    def __init__(self, data: list):
        self.data: list = data
        self.col: list = []
        self.row: list = []
        for i in range(len(self.data)):
            col = 0
            listRowCount = []
            for iter in self.data[i]:
                if not all(isinstance(iter_, list) for iter_ in iter[1]):
                    col += 1
                    listRowCount.append(int(len(iter[1])))
                else:
                    col += len(iter[1])
            self.row.append(max(listRowCount) if listRowCount else 0)
            self.col.append(col)
        ...


class TableDensity(Table):
    def __init__(
        self,
        density: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.density = self.make_backwards_compatibility(density) if density else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None
        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        rho = temp = extra_fields = []
        name, val = self.density if self.density else NONE_TUPLE()
        if name == DENSITY:
            rho = self.get_data(val)

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        return TableData(
            [[(DENSITY, rho), (TEMPERATURE, temp), (EXTRA_FIELDS, extra_fields)]]
        )


class TableElasticity(Table):
    def __init__(
        self,
        elasticType: int,
        youngs_modulus: Union[tuple, None],
        shear_modulus: Union[tuple, None],
        poissons_ratio: Union[tuple, None],
        nastran_failure_index_tension: Union[tuple, None],
        nastran_failure_index_compression: Union[tuple, None],
        nastran_failure_index_shear: Union[tuple, None],
        e1: Union[tuple, None],
        e2: Union[tuple, None],
        e3: Union[tuple, None],
        e4: Union[tuple, None],
        e5: Union[tuple, None],
        e6: Union[tuple, None],
        g12: Union[tuple, None],
        g1z: Union[tuple, None],
        g2z: Union[tuple, None],
        g13: Union[tuple, None],
        g23: Union[tuple, None],
        nu12: Union[tuple, None],
        nu13: Union[tuple, None],
        nu23: Union[tuple, None],
        xt: Union[tuple, None],
        xc: Union[tuple, None],
        yt: Union[tuple, None],
        yc: Union[tuple, None],
        s: Union[tuple, None],
        f12: Union[tuple, None],
        strn: Union[tuple, None],
        d1111: Union[tuple, None],
        d1122: Union[tuple, None],
        d2222: Union[tuple, None],
        d1133: Union[tuple, None],
        d2233: Union[tuple, None],
        d3333: Union[tuple, None],
        d1212: Union[tuple, None],
        d1313: Union[tuple, None],
        d2323: Union[tuple, None],
        eknn: Union[tuple, None],
        g1kss: Union[tuple, None],
        g2ktt: Union[tuple, None],
        temperature: Union[tuple, None],
        frequency_dependence: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.elasticType = elasticType
        if self.elasticType == ELASTIC_TYPE.ISOTROPIC:
            self.youngs_modulus = (
                self.make_backwards_compatibility(youngs_modulus)
                if youngs_modulus
                else None
            )
            self.shear_modulus = shear_modulus if shear_modulus else None
            self.poissons_ratio = (
                self.make_backwards_compatibility(poissons_ratio)
                if poissons_ratio
                else None
            )
            self.nastran_failure_index_tension = (
                nastran_failure_index_tension if nastran_failure_index_tension else None
            )
            self.nastran_failure_index_compression = (
                nastran_failure_index_compression
                if nastran_failure_index_compression
                else None
            )
            self.nastran_failure_index_shear = (
                nastran_failure_index_shear if nastran_failure_index_shear else None
            )
        elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_2D:
            self.e1 = e1 if e1 else None
            self.e2 = e2 if e2 else None
            self.g12 = g12 if g12 else None
            self.g1z = g1z if g1z else None
            self.g2z = g2z if g2z else None
            self.nu12 = nu12 if nu12 else None
            self.xt = xt if xt else None
            self.xc = xc if xc else None
            self.yt = yt if yt else None
            self.yc = yc if yc else None
            self.s = s if s else None
            self.f12 = f12 if f12 else None
            self.strn = strn if strn else None
        elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_1:
            self.e1 = e1 if e1 else None
            self.e2 = e2 if e2 else None
            self.e3 = e3 if e3 else None
            self.g12 = g12 if g12 else None
            self.g13 = g13 if g13 else None
            self.g23 = g23 if g23 else None
            self.nu12 = nu12 if nu12 else None
            self.nu13 = nu13 if nu13 else None
            self.nu23 = nu23 if nu23 else None
        elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_2:
            self.d1111 = d1111 if d1111 else None
            self.d1122 = d1122 if d1122 else None
            self.d2222 = d2222 if d2222 else None
            self.d1133 = d1133 if d1133 else None
            self.d2233 = d2233 if d2233 else None
            self.d3333 = d3333 if d3333 else None
            self.d1212 = d1212 if d1212 else None
            self.d1313 = d1313 if d1313 else None
            self.d2323 = d2323 if d2323 else None
        elif self.elasticType == ELASTIC_TYPE.ANISOTROPIC_2D:
            self.e1 = e1 if e1 else None
            self.e2 = e2 if e2 else None
            self.e3 = e3 if e3 else None
            self.nastran_failure_index_tension = (
                nastran_failure_index_tension if nastran_failure_index_tension else None
            )
            self.nastran_failure_index_compression = (
                nastran_failure_index_compression
                if nastran_failure_index_compression
                else None
            )
            self.nastran_failure_index_shear = (
                nastran_failure_index_shear if nastran_failure_index_shear else None
            )
        elif self.elasticType == ELASTIC_TYPE.ANISOTROPIC_3D:
            self.e1 = e1 if e1 else None
            self.e2 = e2 if e2 else None
            self.e3 = e3 if e3 else None
            self.e4 = e4 if e4 else None
            self.e5 = e5 if e5 else None
            self.e6 = e6 if e6 else None
        elif self.elasticType == ELASTIC_TYPE.TRACTION:
            self.eknn = eknn if eknn else None
            self.g1kss = g1kss if g1kss else None
            self.g2ktt = g2ktt if g2ktt else None
            ...
        elif (
            self.elasticType == ELASTIC_TYPE.LAMINA
            or self.elasticType == ELASTIC_TYPE.COUPLED_TRACTION
            or self.elasticType == ELASTIC_TYPE.SHORT_FIBER
        ):
            # Lamina, Coupled Traction, Short Fiber do not have any specific table
            ...

        self.temperature = temperature if temperature else None
        self.frequency_dependence = (
            frequency_dependence if frequency_dependence else None
        )
        self.extra_fields = extra_fields if extra_fields else None
        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        if self.elasticType == ELASTIC_TYPE.ISOTROPIC:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.youngs_modulus,
                    self.shear_modulus,
                    self.poissons_ratio,
                ]
            ]
            lst_name = [YOUNGS_MODULUS, SHEAR_MODULUS, POISSONS_RATIO]
            e, g, nu = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.nastran_failure_index_tension,
                    self.nastran_failure_index_compression,
                    self.nastran_failure_index_shear,
                ]
            ]
            lst_name = [
                NASTRAN_FAILURE_INDEX_TENSION,
                NASTRAN_FAILURE_INDEX_COMPRESSION,
                NASTRAN_FAILURE_INDEX_SHEAR,
            ]
            tension, compression, shear = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.temperature,
                    self.frequency_dependence,
                    self.extra_fields,
                ]
            ]
            lst_name = [TEMPERATURE, FREQUENCY_DEPENDENCE, EXTRA_FIELDS]
            temp, frequency_dependence, extra_fields = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            return TableData(
                [
                    [
                        (YOUNGS_MODULUS, e),
                        (SHEAR_MODULUS, g),
                        (POISSONS_RATIO, nu),
                        (TEMPERATURE, temp),
                        (FREQUENCY_DEPENDENCE, frequency_dependence),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                    [
                        (NASTRAN_FAILURE_INDEX_TENSION, tension),
                        (NASTRAN_FAILURE_INDEX_COMPRESSION, compression),
                        (NASTRAN_FAILURE_INDEX_SHEAR, shear),
                    ],
                ]
            )
            ...
        elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_2D:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.e1, self.e2, self.g12, self.g1z, self.g2z, self.nu12]
            ]
            lst_name = [E1, E2, G12, G1Z, G2Z, NU12]
            e1, e2, g12, g1z, g2z, nu12 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.xt,
                    self.xc,
                    self.yt,
                    self.yc,
                    self.s,
                    self.f12,
                    self.strn,
                ]
            ]
            lst_name = [XT, XC, YT, YC, S, F12, STRN]
            xt, xc, yt, yc, s, f12, strn = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.temperature,
                    self.frequency_dependence,
                    self.extra_fields,
                ]
            ]
            lst_name = [TEMPERATURE, FREQUENCY_DEPENDENCE, EXTRA_FIELDS]
            temp, frequency_dependence, extra_fields = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            return TableData(
                [
                    [
                        (E1, e1),
                        (E2, e2),
                        (G12, g12),
                        (G1Z, g1z),
                        (G2Z, g2z),
                        (NU12, nu12),
                        (TEMPERATURE, temp),
                        (FREQUENCY_DEPENDENCE, frequency_dependence),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                    [
                        (XT, xt),
                        (XC, xc),
                        (YT, yt),
                        (YC, yc),
                        (S, s),
                        (F12, f12),
                        (STRN, strn),
                    ],
                ]
            )
            ...
        elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_1:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.e1,
                    self.e2,
                    self.e3,
                    self.g12,
                    self.g13,
                    self.g23,
                    self.nu12,
                    self.nu13,
                    self.nu23,
                ]
            ]
            lst_name = [E1, E2, E3, G12, G13, G23, NU12, NU13, NU23]
            e1, e2, e3, g12, g13, g23, nu12, nu13, nu23 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.temperature,
                    self.frequency_dependence,
                    self.extra_fields,
                ]
            ]
            lst_name = [TEMPERATURE, FREQUENCY_DEPENDENCE, EXTRA_FIELDS]
            temp, frequency_dependence, extra_fields = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            return TableData(
                [
                    [
                        (E1, e1),
                        (E2, e2),
                        (E3, e3),
                        (NU12, nu12),
                        (NU13, nu13),
                        (NU23, nu23),
                        (G12, g12),
                        (G13, g13),
                        (G23, g23),
                        (TEMPERATURE, temp),
                        (FREQUENCY_DEPENDENCE, frequency_dependence),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
            ...
        elif self.elasticType == ELASTIC_TYPE.ORTHOTROPIC_3D_TYPE_2:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.d1111,
                    self.d1122,
                    self.d2222,
                    self.d1133,
                    self.d2233,
                    self.d3333,
                    self.d1212,
                    self.d1313,
                    self.d2323,
                ]
            ]
            lst_name = [D1111, D1122, D2222, D1133, D2233, D3333, D1212, D1313, D2323]
            d1111, d1122, d2222, d1133, d2233, d3333, d1212, d1313, d2323 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.temperature,
                    self.frequency_dependence,
                    self.extra_fields,
                ]
            ]
            lst_name = [TEMPERATURE, FREQUENCY_DEPENDENCE, EXTRA_FIELDS]
            temp, frequency_dependence, extra_fields = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (D1111, d1111),
                        (D1122, d1122),
                        (D2222, d2222),
                        (D1133, d1133),
                        (D2233, d2233),
                        (D3333, d3333),
                        (D1212, d1212),
                        (D1313, d1313),
                        (D2323, d2323),
                        (TEMPERATURE, temp),
                        (FREQUENCY_DEPENDENCE, frequency_dependence),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
            ...
        elif self.elasticType == ELASTIC_TYPE.ANISOTROPIC_2D:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.e1, self.e2, self.e3]
            ]
            lst_name = [E1, E2, E3]
            e1, e2, e3 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.nastran_failure_index_tension,
                    self.nastran_failure_index_compression,
                    self.nastran_failure_index_shear,
                ]
            ]
            lst_name = [
                NASTRAN_FAILURE_INDEX_TENSION,
                NASTRAN_FAILURE_INDEX_COMPRESSION,
                NASTRAN_FAILURE_INDEX_SHEAR,
            ]
            tension, compression, shear = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            return TableData(
                [
                    [
                        (E1, e1),
                        (E2, e2),
                        (E3, e3),
                    ],
                    [
                        (NASTRAN_FAILURE_INDEX_TENSION, tension),
                        (NASTRAN_FAILURE_INDEX_COMPRESSION, compression),
                        (NASTRAN_FAILURE_INDEX_SHEAR, shear),
                    ],
                ]
            )
            ...
        elif self.elasticType == ELASTIC_TYPE.ANISOTROPIC_3D:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6]
            ]
            lst_name = [E1, E2, E3, E4, E5, E6]
            e1, e2, e3, e4, e5, e6 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            return TableData(
                [
                    [
                        (E1, e1),
                        (E2, e2),
                        (E3, e3),
                        (E4, e4),
                        (E5, e5),
                        (E6, e6),
                    ],
                ]
            )
            ...
        elif self.elasticType == ELASTIC_TYPE.TRACTION:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.eknn, self.g1kss, self.g2ktt]
            ]
            lst_name = [EKNN, G1KSS, G2KTT]
            eknn, g1kss, g2ktt = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.temperature,
                    self.frequency_dependence,
                    self.extra_fields,
                ]
            ]
            lst_name = [TEMPERATURE, FREQUENCY_DEPENDENCE, EXTRA_FIELDS]
            temp, frequency_dependence, extra_fields = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]

            return TableData(
                [
                    [
                        (EKNN, eknn),
                        (G1KSS, g1kss),
                        (G2KTT, g2ktt),
                        (TEMPERATURE, temp),
                        (FREQUENCY_DEPENDENCE, frequency_dependence),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
            ...
        elif (
            self.elasticType == ELASTIC_TYPE.LAMINA
            or self.elasticType == ELASTIC_TYPE.COUPLED_TRACTION
            or self.elasticType == ELASTIC_TYPE.SHORT_FIBER
        ):
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.temperature,
                    self.extra_fields,
                ]
            ]
            lst_name = [TEMPERATURE, EXTRA_FIELDS]
            temp, frequency_dependence, extra_fields = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ]
                ]
            )
            ...


class TableHyperElastic(Table):
    def __init__(
        self,
        hyperElasticType: HYPERELASTIC_TYPE,
        mu: Union[tuple, None],
        lamda_m: Union[tuple, None],
        d: Union[tuple, None],
        c10: Union[tuple, None],
        c01: Union[tuple, None],
        d1: Union[tuple, None],
        mu1: Union[tuple, None],
        alpha1: Union[tuple, None],
        alpha: Union[tuple, None],
        beta: Union[tuple, None],
        c0: Union[tuple, None],
        c20: Union[tuple, None],
        c30: Union[tuple, None],
        d2: Union[tuple, None],
        d3: Union[tuple, None],
        temperature: Union[tuple, None],
        # extra_fields: Union[tuple, None],
        nomial_stress: Union[tuple, None],
        nomial_strain: Union[tuple, None],
        lateral_nomial_strain: Union[tuple, None],
        temperature_uniaxial: Union[tuple, None],
        extra_fields_uniaxial: Union[tuple, None],
        stress: Union[tuple, None],
        time: Union[tuple, None],
        **kwargs,
    ):
        self.hyperElasticType = hyperElasticType
        self.temperature = temperature if temperature else None
        # self.extra_fields = extra_fields if extra_fields else None

        self.nomial_stress = nomial_stress if nomial_stress else None
        self.nomial_strain = nomial_strain if nomial_strain else None
        self.lateral_nomial_strain = (
            lateral_nomial_strain if lateral_nomial_strain else None
        )
        self.temperature_uniaxial = (
            temperature_uniaxial if temperature_uniaxial else None
        )
        self.extra_fields_uniaxial = (
            extra_fields_uniaxial if extra_fields_uniaxial else None
        )
        self.stress = stress if stress else None
        self.time = time if time else None
        if hyperElasticType in [HYPERELASTIC_TYPE.ARRUDA_BOYCE]:
            self.mu = mu if mu else None
            self.lamda_m = lamda_m if lamda_m else None
            self.d = d if d else None
        elif hyperElasticType in [
            HYPERELASTIC_TYPE.MOONEY_RIVLIN,
            HYPERELASTIC_TYPE.POLYNOMIAL,
        ]:
            self.c10 = c10 if c10 else None
            self.c01 = c01 if c01 else None
            self.d1 = d1 if d1 else None
        elif hyperElasticType in [
            HYPERELASTIC_TYPE.NEO_HOOKE,
            HYPERELASTIC_TYPE.REDUCED_POLYNOMIAL,
        ]:
            self.c10 = c10 if c10 else None
            self.d1 = d1 if d1 else None
        elif hyperElasticType in [HYPERELASTIC_TYPE.OGDEN]:
            self.mu1 = mu1 if mu1 else None
            self.alpha1 = alpha1 if alpha1 else None
            self.d1 = d1 if d1 else None
        elif hyperElasticType in [HYPERELASTIC_TYPE.VAN_DER_WAALS]:
            self.mu = mu if mu else None
            self.lamda_m = lamda_m if lamda_m else None
            self.alpha = alpha if alpha else None
            self.beta = beta if beta else None
            self.d = d if d else None
        elif hyperElasticType in [HYPERELASTIC_TYPE.YEOH]:
            self.c0 = c0 if c0 else None
            self.c20 = c20 if c20 else None
            self.c30 = c30 if c30 else None
            self.d1 = d1 if d1 else None
            self.d2 = d2 if d2 else None
            self.d3 = d3 if d3 else None
        elif hyperElasticType in [
            HYPERELASTIC_TYPE.MARLOW,
            HYPERELASTIC_TYPE.USER,
            HYPERELASTIC_TYPE.UNKNOWN,
        ]:
            ...
        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        temp_uniaxial = lateral_strain = extra_fields_uniaxial = []

        name, val = (
            self.lateral_nomial_strain if self.lateral_nomial_strain else NONE_TUPLE()
        )
        if name == LATERAL_NOMIAL_STRAIN:
            lateral_strain = self.get_data(val)

        name, val = (
            self.temperature_uniaxial if self.temperature_uniaxial else NONE_TUPLE()
        )
        if name == TEMPERATURE_UNIAXIAL:
            temp_uniaxial = self.get_data(val)

        name, val = (
            self.extra_fields_uniaxial if self.extra_fields_uniaxial else NONE_TUPLE()
        )
        if name == EXTRA_FIELDS_UNIAXIAL:
            extra_fields_uniaxial = self.get_data(val)

        lst_var = []
        lst_name = []
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.nomial_stress, self.nomial_strain]
        ]
        lst_name = [NOMIAL_STRESS, NOMIAL_STRAIN]
        (nomial_stress, nomial_strain) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        uniaixal_table = [
            (NOMIAL_STRESS, nomial_stress),
            (NOMIAL_STRAIN, nomial_strain),
            (LATERAL_NOMIAL_STRAIN, lateral_strain),
            (TEMPERATURE_UNIAXIAL, temp_uniaxial),
            (EXTRA_FIELDS_UNIAXIAL, extra_fields_uniaxial),
        ]

        lst_var = []
        lst_name = []
        lst_var = [val if val else NONE_TUPLE() for val in [self.stress, self.time]]
        lst_name = [STRESS, TIME]
        (stress, time) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        relaxation_table = [
            (STRESS, stress),
            (TIME, time),
        ]

        temp = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        lst_var = []
        lst_name = []
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.nomial_stress, self.nomial_strain]
        ]
        lst_name = [NOMIAL_STRESS, NOMIAL_STRAIN]
        (nomial_stress, nomial_strain) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        if self.hyperElasticType in [HYPERELASTIC_TYPE.ARRUDA_BOYCE]:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.mu, self.lamda_m, self.d]
            ]
            lst_name = [MU, LAMDA_M, D]
            (mu, lamda_m, d) = [
                self.get_data(val) if itr == name else []
                for itr, (name, val) in zip(lst_name, lst_var)
            ]
            coefficient_table = [
                (MU, mu),
                (LAMDA_M, lamda_m),
                (D, d),
                (TEMPERATURE, temp),
            ]
        elif self.hyperElasticType in [
            HYPERELASTIC_TYPE.MOONEY_RIVLIN,
            HYPERELASTIC_TYPE.POLYNOMIAL,
        ]:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.c10, self.c01, self.d1]
            ]
            lst_name = [C10, C01, D1]
            (c10, c01, d1) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            coefficient_table = [
                (C10, c10),
                (C01, c01),
                (D1, d1),
                (TEMPERATURE, temp),
            ]
        elif self.hyperElasticType in [
            HYPERELASTIC_TYPE.NEO_HOOKE,
            HYPERELASTIC_TYPE.REDUCED_POLYNOMIAL,
        ]:
            lst_var = [val if val else NONE_TUPLE() for val in [self.c10, self.d1]]
            lst_name = [C10, D1]
            (c10, d1) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            coefficient_table = [
                (C10, c10),
                (D1, d1),
                (TEMPERATURE, temp),
            ]
        elif self.hyperElasticType in [HYPERELASTIC_TYPE.OGDEN]:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.mu1, self.alpha1, self.d1]
            ]
            lst_name = [MU1, ALPHA1, D1]
            (mu1, alpha1, d1) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            coefficient_table = [
                (MU1, mu1),
                (ALPHA1, alpha1),
                (D1, d1),
                (TEMPERATURE, temp),
            ]
        elif self.hyperElasticType in [HYPERELASTIC_TYPE.VAN_DER_WAALS]:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.mu, self.lamda_m, self.alpha, self.beta, self.d]
            ]
            lst_name = [MU, LAMDA_M, ALPHA, BETA, D]
            (mu, lamda_m, alpha, beta, d) = [
                self.get_data(val) if itr == name else []
                for itr, (name, val) in zip(lst_name, lst_var)
            ]
            coefficient_table = [
                (MU, mu),
                (LAMDA_M, lamda_m),
                (ALPHA, alpha),
                (BETA, beta),
                (D, d),
                (TEMPERATURE, temp),
            ]
        elif self.hyperElasticType in [HYPERELASTIC_TYPE.YEOH]:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.c0, self.c20, self.c30, self.d1, self.d2, self.d3]
            ]
            lst_name = [C0, C20, C30, D1, D2, D3]
            (c0, c20, c30, d1, d2, d3) = [
                self.get_data(val) if itr == name else []
                for itr, (name, val) in zip(lst_name, lst_var)
            ]
            coefficient_table = [
                (C0, c0),
                (C20, c20),
                (C30, c30),
                (D1, d1),
                (D2, d2),
                (D3, d3),
                (TEMPERATURE, temp),
            ]
        elif self.hyperElasticType in [
            HYPERELASTIC_TYPE.MARLOW,
            HYPERELASTIC_TYPE.USER,
            HYPERELASTIC_TYPE.UNKNOWN,
        ]:
            coefficient_table = []

        return TableData(
            [
                coefficient_table,
                uniaixal_table,
                relaxation_table,
            ]
        )


class TableLowDensityFoam(Table):
    def __init__(
        self,
        stress_compression: Union[tuple, None],
        strain_compression: Union[tuple, None],
        strain_rate_compression: Union[tuple, None],
        stress_tension: Union[tuple, None],
        strain_tension: Union[tuple, None],
        strain_rate_tension: Union[tuple, None],
        extra_fields_compression: Union[tuple, None],
        extra_fields_tension: Union[tuple, None],
        **kwargs,
    ):
        self.stress_comp = stress_compression if stress_compression else None
        self.strain_comp = strain_compression if strain_compression else None
        self.stress_tens = stress_tension if stress_tension else None
        self.strain_tens = strain_tension if strain_tension else None
        self.strain_rate_tense = strain_rate_tension if strain_rate_tension else None
        self.strain_rate_comp = (
            strain_rate_compression if strain_rate_compression else None
        )
        self.strain_tens = strain_tension if strain_tension else None
        self.extra_fields_comp = (
            extra_fields_compression if extra_fields_compression else None
        )
        self.extra_fields_tens = extra_fields_tension if extra_fields_tension else None
        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        extra_fields_comp = extra_fields_tense = []

        name, val = self.extra_fields_comp if self.extra_fields_comp else NONE_TUPLE()
        if name == EXTRA_FIELDS_COMPRESSION:
            extra_fields_comp = self.get_data(val)

        lst_var = []
        lst_name = []
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.stress_comp, self.strain_comp, self.strain_rate_comp]
        ]
        lst_name = [STRESS_COMPRESSION, STRAIN_COMPRESSION, STRAIN_RATE_COMPRESSION]
        (stress_comp, strain_comp, strain_rate_comp) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        compression_table = [
            (STRESS_COMPRESSION, stress_comp),
            (STRAIN_COMPRESSION, strain_comp),
            (STRAIN_RATE_COMPRESSION, strain_rate_comp),
            (EXTRA_FIELDS_COMPRESSION, extra_fields_comp),
        ]

        name, val = self.extra_fields_tens if self.extra_fields_tens else NONE_TUPLE()
        if name == EXTRA_FIELDS_TENSION:
            extra_fields_tense = self.get_data(val)

        lst_var = []
        lst_name = []
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.stress_tens, self.strain_tens, self.strain_rate_tense]
        ]
        lst_name = [STRESS_TENSION, STRAIN_TENSION, STRAIN_RATE_TENSION]
        (stress_tense, strain_tense, strain_rate_tense) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        tension_table = [
            (STRESS_TENSION, stress_tense),
            (STRAIN_TENSION, strain_tense),
            (STRAIN_RATE_TENSION, strain_rate_tense),
            (EXTRA_FIELDS_TENSION, extra_fields_tense),
        ]

        return TableData(
            [
                tension_table,
                compression_table,
            ]
        )


class TablePlastic(Table):
    def __init__(
        self,
        harden: int,
        dataType: Union[int, None],  # for combined harden type
        curve_ForCombined: Union[int, None],  # for combined harden type
        stress: Union[tuple, None],
        strain: Union[tuple, None],
        a: Union[tuple, None],
        b: Union[tuple, None],
        n: Union[tuple, None],
        m: Union[tuple, None],
        melting_temp: Union[tuple, None],
        transition_temp: Union[tuple, None],
        hardening_prop: Union[tuple, None],
        gamma: Union[tuple, None],
        hard_param: Union[tuple, None],
        strain_rate: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        equiv_stress: Union[tuple, None],
        equiv_strain: Union[tuple, None],
        q_infinity: Union[tuple, None],
        hardening_b: Union[tuple, None],
        extra_fields_sub: Union[tuple, None],
        temperature_sub: Union[tuple, None],
        **kwargs,
    ):
        self.harden = harden
        self.dataType = dataType
        self.curve_ForCombined = curve_ForCombined

        if harden in [PLASTIC_HARDENING.ISOTROPIC, PLASTIC_HARDENING.KINEMATIC]:
            self.stress = stress if stress else None
            self.strain = strain if strain else None
        elif harden == PLASTIC_HARDENING.JOHNSON_COOK:
            self.a = a if a else None
            self.b = b if b else None
            self.m = m if m else None
            self.n = n if n else None
            self.melt_temp = melting_temp if melting_temp else None
            self.trans_temp = transition_temp if transition_temp else None
        elif harden == PLASTIC_HARDENING.USER:
            self.hardening_prop = hardening_prop if hardening_prop else None
        elif harden == PLASTIC_HARDENING.COMBINED:
            if self.dataType == 0:
                if self.curve_ForCombined in [0, 1]:
                    self.stress = stress if stress else None
                    self.strain = strain if strain else None
                elif self.curve_ForCombined == 2:
                    self.gamma = gamma if gamma else None
                    self.hard_param = hard_param if hard_param else None
            elif self.dataType == 1:
                self.stress = stress if stress else None
                self.gamma = gamma if gamma else None
                self.hard_param = hard_param if hard_param else None
            elif self.dataType == 2:
                self.stress = stress if stress else None
                self.strain = strain if strain else None

        self.strain_rate = strain_rate if strain_rate else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        self.equiv_stress = equiv_stress if equiv_stress else None
        self.equiv_strain = equiv_strain if equiv_strain else None
        self.q_infinity = q_infinity if q_infinity else None
        self.hardening_b = hardening_b if hardening_b else None
        self.extra_fields_sub = extra_fields_sub if extra_fields_sub else None
        self.temperature_sub = temperature_sub if temperature_sub else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        table_main = []
        if self.harden in [PLASTIC_HARDENING.ISOTROPIC, PLASTIC_HARDENING.KINEMATIC]:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.stress, self.strain]
            ]
            lst_name = [STRESS, STRAIN]
            stress, strain = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            strain_rate = temp = extra_fields = []

            name, val = self.strain_rate if self.strain_rate else NONE_TUPLE()
            if name == STRAIN_RATE:
                strain_rate = self.get_data(val)

            name, val = self.temperature if self.temperature else NONE_TUPLE()
            if name == TEMPERATURE:
                temp = self.get_data(val)

            name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
            if name == EXTRA_FIELDS:
                extra_fields = self.get_data(val)

            table_main = [
                (STRESS, stress),
                (STRAIN, strain),
                (STRAIN_RATE, strain_rate),
                (TEMPERATURE, temp),
                (EXTRA_FIELDS, extra_fields),
            ]
        elif self.harden == PLASTIC_HARDENING.JOHNSON_COOK:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.a,
                    self.b,
                    self.m,
                    self.n,
                    self.melt_temp,
                    self.trans_temp,
                ]
            ]
            lst_name = [A, B, M, N, MELTING_TEMP, TRANSITION_TEMP]
            a, b, m, n, melt, trans = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            table_main = [
                (A, a),
                (B, b),
                (M, m),
                (N, n),
                (MELTING_TEMP, melt),
                (TRANSITION_TEMP, trans),
            ]
        elif self.harden == PLASTIC_HARDENING.USER:
            lst_var = [val if val else NONE_TUPLE() for val in [self.hardening_prop]]
            lst_name = [HARDENING_PROP]
            (harden_prop,) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            table_main = [
                (HARDENING_PROP, harden_prop),
            ]
        elif self.harden == PLASTIC_HARDENING.COMBINED:
            table_main = []
            strain_rate = temp = extra_fields = []

            name, val = self.strain_rate if self.strain_rate else NONE_TUPLE()
            if name == STRAIN_RATE:
                strain_rate = self.get_data(val)

            name, val = self.temperature if self.temperature else NONE_TUPLE()
            if name == TEMPERATURE:
                temp = self.get_data(val)

            name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
            if name == EXTRA_FIELDS:
                extra_fields = self.get_data(val)

            if self.dataType == 0:
                if self.curve_ForCombined in [0, 1]:
                    lst_var = [
                        val if val else NONE_TUPLE()
                        for val in [self.stress, self.strain]
                    ]
                    lst_name = [STRESS, STRAIN]
                    stress, strain = [
                        self.get_data(val) if d == name else []
                        for d, (name, val) in zip(lst_name, lst_var)
                    ]
                    table_main = [
                        (STRESS, stress),
                        (STRAIN, strain),
                        (STRAIN_RATE, strain_rate),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ]
                elif self.curve_ForCombined == 2:
                    lst_var = [
                        val if val else NONE_TUPLE()
                        for val in [self.gamma, self.hard_param]
                    ]
                    lst_name = [GAMMA, HARD_PARAM]
                    gamma, hard_param = [
                        self.get_data(val) if d == name else []
                        for d, (name, val) in zip(lst_name, lst_var)
                    ]
                    table_main = [
                        (GAMMA, gamma),
                        (HARD_PARAM, hard_param),
                        (STRAIN_RATE, strain_rate),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ]
            elif self.dataType == 1:
                lst_var = [
                    val if val else NONE_TUPLE()
                    for val in [self.stress, self.gamma, self.hard_param]
                ]
                lst_name = [STRESS, GAMMA, HARD_PARAM]
                stress, gamma, hard_param = [
                    self.get_data(val) if d == name else []
                    for d, (name, val) in zip(lst_name, lst_var)
                ]
                table_main = [
                    (STRESS, stress),
                    (GAMMA, gamma),
                    (HARD_PARAM, hard_param),
                    (STRAIN_RATE, strain_rate),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ]
            elif self.dataType == 2:
                lst_var = [
                    val if val else NONE_TUPLE() for val in [self.stress, self.strain]
                ]
                lst_name = [STRESS, STRAIN]
                stress, strain = [
                    self.get_data(val) if d == name else []
                    for d, (name, val) in zip(lst_name, lst_var)
                ]
                table_main = [
                    (STRESS, stress),
                    (STRAIN, strain),
                    (STRAIN_RATE, strain_rate),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ]

        # For suboption
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [
                self.equiv_stress,
                self.equiv_strain,
                self.q_infinity,
                self.hardening_b,
            ]
        ]
        lst_name = [EQUIV_STRESS, EQUIV_STRAIN, Q_INFINITY, HARDENING_B]
        equiv_stress, equiv_strain, q_infty, harden_b = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        strain_rate = temp_sub = extra_fields_sub = []

        name, val = self.temperature_sub if self.temperature_sub else NONE_TUPLE()
        if name == TEMPERATURE_SUB:
            temp_sub = self.get_data(val)

        name, val = self.extra_fields_sub if self.extra_fields_sub else NONE_TUPLE()
        if name == EXTRA_FIELDS_SUB:
            extra_fields_sub = self.get_data(val)

        return TableData(
            [
                table_main,
                [
                    (EQUIV_STRESS, equiv_stress),
                    (EQUIV_STRAIN, equiv_strain),
                    (Q_INFINITY, q_infty),
                    (HARDENING_B, harden_b),
                    (EXTRA_FIELDS_SUB, extra_fields_sub),
                    (TEMPERATURE_SUB, temp_sub),
                ],
            ]
        )


class TableCreep(Table):
    def __init__(
        self,
        lawType: PLASTICITY_CREEP_LAW_TYPE,
        power_law_multiplier: Union[tuple, None],
        hyper_law_multiplier: Union[tuple, None],
        eq_stress_multiplier: Union[tuple, None],
        activation_energy: Union[tuple, None],
        universal_gas_const: Union[tuple, None],
        c0: Union[tuple, None],
        c1: Union[tuple, None],
        c2: Union[tuple, None],
        c3: Union[tuple, None],
        eq_stress_order: Union[tuple, None],
        time_order: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.lawType = lawType
        if lawType in [
            PLASTICITY_CREEP_LAW_TYPE.STRAIN_HARDENING,
            PLASTICITY_CREEP_LAW_TYPE.TIME_HARDENING,
        ]:
            self.power_law_multiplier = (
                power_law_multiplier if power_law_multiplier else None
            )
            self.eq_stress_order = eq_stress_order if eq_stress_order else None
            self.time_order = time_order if time_order else None
        elif lawType in [PLASTICITY_CREEP_LAW_TYPE.HYPERBOLIC_SINE]:
            self.power_law_multiplier = (
                power_law_multiplier if power_law_multiplier else None
            )
            self.hyper_law_multiplier = (
                hyper_law_multiplier if hyper_law_multiplier else None
            )
            self.eq_stress_multiplier = (
                eq_stress_multiplier if eq_stress_multiplier else None
            )
            self.activation_energy = activation_energy if activation_energy else None
            self.universal_gas_const = (
                universal_gas_const if universal_gas_const else None
            )
        elif lawType in [PLASTICITY_CREEP_LAW_TYPE.ADVC_LAW]:
            self.c0 = c0 if c0 else None
            self.c1 = c1 if c1 else None
            self.c2 = c2 if c2 else None
            self.c3 = c3 if c3 else None
        else:
            pass
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None
        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        extra_fields = temp = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        lst_var = []
        lst_name = []
        if self.lawType in [
            PLASTICITY_CREEP_LAW_TYPE.STRAIN_HARDENING,
            PLASTICITY_CREEP_LAW_TYPE.TIME_HARDENING,
        ]:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.power_law_multiplier,
                    self.eq_stress_order,
                    self.time_order,
                ]
            ]
            lst_name = [POWER_LAW_MULTIPLIER, EQ_STRESS_ORDER, TIME_ORDER]
            (power_law_multiplier, eq_stress_order, time_order) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            table = [
                (POWER_LAW_MULTIPLIER, power_law_multiplier),
                (EQ_STRESS_ORDER, eq_stress_order),
                (TIME_ORDER, time_order),
                (TEMPERATURE, temp),
                (EXTRA_FIELDS, extra_fields),
            ]
        elif self.lawType in [PLASTICITY_CREEP_LAW_TYPE.HYPERBOLIC_SINE]:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.power_law_multiplier,
                    self.hyper_law_multiplier,
                    self.eq_stress_multiplier,
                    self.activation_energy,
                    self.universal_gas_const,
                ]
            ]
            lst_name = [
                POWER_LAW_MULTIPLIER,
                HYPER_LAW_MULTIPLIER,
                EQ_STRESS_MULTIPLIER,
                ACTIVATION_ENERGY,
                UNIVERSAL_GAS_CONST,
            ]
            (
                power_law_multiplier,
                hyper_law_multiplier,
                eq_stress_multiplier,
                activation_energy,
                universal_gas_const,
            ) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            table = [
                (POWER_LAW_MULTIPLIER, power_law_multiplier),
                (HYPER_LAW_MULTIPLIER, hyper_law_multiplier),
                (EQ_STRESS_MULTIPLIER, eq_stress_multiplier),
                (ACTIVATION_ENERGY, activation_energy),
                (UNIVERSAL_GAS_CONST, universal_gas_const),
                (TEMPERATURE, temp),
                (EXTRA_FIELDS, extra_fields),
            ]
        elif self.lawType in [PLASTICITY_CREEP_LAW_TYPE.ADVC_LAW]:
            self.c0 = c0 if c0 else None
            self.c1 = c1 if c1 else None
            self.c2 = c2 if c2 else None
            self.c3 = c3 if c3 else None

            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.c0, self.c1, self.c2, self.c3]
            ]
            lst_name = [C0, C1, C2, C3]
            (c0, c1, c2, c3) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            table = [
                (C0, c0),
                (C1, c1),
                (C2, c2),
                (C3, c3),
            ]
        else:
            table = []

        return TableData(
            [
                table,
            ]
        )


class TableDamping(Table):
    def __init__(
        self,
        damping: Union[tuple, None],
        frequency: Union[tuple, None],
        **kwargs,
    ):
        self.damping = damping if damping else None
        self.frequency = frequency if frequency else None
        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [
            val if val else NONE_TUPLE() for val in [self.damping, self.frequency]
        ]
        lst_name = [DAMPING, FREQUENCY]
        (
            damping,
            frequency,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        return TableData(
            [
                [
                    (DAMPING, damping),
                    (FREQUENCY, frequency),
                ]
            ]
        )


class TableViscoElastic(Table):
    def __init__(
        self,
        shear_modulus: Union[tuple, None],
        bulk_modulus: Union[tuple, None],
        time_delay: Union[tuple, None],
        shift_factor: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.shear = shear_modulus if shear_modulus else None
        self.bulk = bulk_modulus if bulk_modulus else None
        self.time_delay = time_delay if time_delay else None
        self.shift_factor = shift_factor if shift_factor else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        temp = extra_fields = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        lst_var = []
        lst_name = []

        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.shear, self.bulk, self.time_delay]
        ]
        lst_name = [SHEAR_MODULUS, BULK_MODULUS, TIME_DELAY]
        (shear, bulk, time_delay) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        # time shift information
        lst_var = []
        lst_name = []

        lst_var = [val if val else NONE_TUPLE() for val in [self.shift_factor]]
        lst_name = [SHIFT_FACTOR]
        (shift,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        return TableData(
            [
                [
                    (SHEAR_MODULUS, shear),
                    (BULK_MODULUS, bulk),
                    (TIME_DELAY, time_delay),
                ],
                [
                    (SHIFT_FACTOR, shift),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ],
            ]
        )


class TableExpansion(Table):
    def __init__(
        self,
        expansionType: int,
        alpha: Union[tuple, None],
        alpha11: Union[tuple, None],
        alpha22: Union[tuple, None],
        alpha33: Union[tuple, None],
        alpha12: Union[tuple, None],
        alpha13: Union[tuple, None],
        alpha23: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.expansionType = expansionType
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        if self.expansionType == EXPANSION_TYPE.ISOTROPIC:
            self.alpha = alpha if alpha else None
        elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_2D:
            self.alpha11 = alpha11 if alpha11 else None
            self.alpha22 = alpha22 if alpha22 else None
        elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_3D:
            self.alpha11 = alpha11 if alpha11 else None
            self.alpha22 = alpha22 if alpha22 else None
            self.alpha33 = alpha33 if alpha33 else None
        elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_2D:
            self.alpha11 = alpha11 if alpha11 else None
            self.alpha22 = alpha22 if alpha22 else None
            self.alpha12 = alpha12 if alpha12 else None
        elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_3D:
            self.alpha11 = alpha11 if alpha11 else None
            self.alpha22 = alpha22 if alpha22 else None
            self.alpha33 = alpha33 if alpha33 else None
            self.alpha12 = alpha12 if alpha12 else None
            self.alpha13 = alpha13 if alpha13 else None
            self.alpha23 = alpha23 if alpha23 else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        temp = extra_fields = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        lst_var = []
        lst_name = []
        if self.expansionType == EXPANSION_TYPE.ISOTROPIC:
            lst_var = [val if val else NONE_TUPLE() for val in [self.alpha]]
            lst_name = [ALPHA]
            (alpha,) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (ALPHA, alpha),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_2D:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.alpha11, self.alpha22]
            ]
            lst_name = [ALPHA11, ALPHA22]
            (
                alpha11,
                alpha22,
            ) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (ALPHA11, alpha11),
                        (ALPHA22, alpha22),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        elif self.expansionType == EXPANSION_TYPE.ORTHOTROPIC_3D:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.alpha11, self.alpha22, self.alpha33]
            ]
            lst_name = [ALPHA11, ALPHA22, ALPHA33]
            alpha11, alpha22, alpha33 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (ALPHA11, alpha11),
                        (ALPHA22, alpha22),
                        (ALPHA33, alpha33),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_2D:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.alpha11, self.alpha22, self.alpha12]
            ]
            lst_name = [ALPHA11, ALPHA22, ALPHA12]
            alpha11, alpha22, alpha12 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (ALPHA11, alpha11),
                        (ALPHA22, alpha22),
                        (ALPHA12, alpha12),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        elif self.expansionType == EXPANSION_TYPE.ANISOTROPIC_3D:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [
                    self.alpha11,
                    self.alpha22,
                    self.alpha33,
                    self.alpha12,
                    self.alpha13,
                    self.alpha23,
                ]
            ]
            lst_name = [ALPHA11, ALPHA22, ALPHA33, ALPHA12, ALPHA13, ALPHA23]
            alpha11, alpha22, alpha33, alpha12, alpha13, alpha23 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            return TableData(
                [
                    [
                        (ALPHA11, alpha11),
                        (ALPHA22, alpha22),
                        (ALPHA33, alpha33),
                        (ALPHA12, alpha12),
                        (ALPHA13, alpha13),
                        (ALPHA23, alpha23),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        else:
            raise NotImplementedError()


class TableConductivity(Table):
    def __init__(
        self,
        conductivityType: int,
        conductivity: Union[tuple, None],
        k11: Union[tuple, None],
        k12: Union[tuple, None],
        k22: Union[tuple, None],
        k13: Union[tuple, None],
        k23: Union[tuple, None],
        k33: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.conductivityType = conductivityType
        if self.conductivityType == CONDUCTIVITY_TYPE.ISOTROPIC:
            self.conductivity = conductivity if conductivity else None
        elif self.conductivityType == CONDUCTIVITY_TYPE.ORTHOTROPIC:
            self.k11 = k11 if k11 else None
            self.k22 = k22 if k22 else None
            self.k33 = k33 if k33 else None
        elif self.conductivityType == CONDUCTIVITY_TYPE.ANISOTROPIC:
            self.k11 = k11 if k11 else None
            self.k22 = k22 if k22 else None
            self.k33 = k33 if k33 else None
            self.k12 = k12 if k12 else None
            self.k13 = k13 if k13 else None
            self.k23 = k23 if k23 else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        if self.conductivityType == CONDUCTIVITY_TYPE.ISOTROPIC:
            lst_var = [val if val else NONE_TUPLE() for val in [self.conductivity]]
            lst_name = [CONDUCTIVITY]
            (conductivity,) = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            temp = extra_fields = []

            name, val = self.temperature if self.temperature else NONE_TUPLE()
            if name == TEMPERATURE:
                temp = self.get_data(val)

            name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
            if name == EXTRA_FIELDS:
                extra_fields = self.get_data(val)

            return TableData(
                [
                    [
                        (CONDUCTIVITY, conductivity),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        elif self.conductivityType == CONDUCTIVITY_TYPE.ORTHOTROPIC:
            lst_var = [
                val if val else NONE_TUPLE() for val in [self.k11, self.k22, self.k33]
            ]
            lst_name = [K11, K22, K33]
            k11, k22, k33 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            temp = extra_fields = []

            name, val = self.temperature if self.temperature else NONE_TUPLE()
            if name == TEMPERATURE:
                temp = self.get_data(val)

            name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
            if name == EXTRA_FIELDS:
                extra_fields = self.get_data(val)

            return TableData(
                [
                    [
                        (K11, k11),
                        (K22, k22),
                        (K33, k33),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )
        elif self.conductivityType == CONDUCTIVITY_TYPE.ANISOTROPIC:
            lst_var = [
                val if val else NONE_TUPLE()
                for val in [self.k11, self.k12, self.k22, self.k13, self.k23, self.k33]
            ]
            lst_name = [K11, K12, K22, K13, K23, K33]
            k11, k12, k22, k13, k23, k33 = [
                self.get_data(val) if d == name else []
                for d, (name, val) in zip(lst_name, lst_var)
            ]
            temp = extra_fields = []

            name, val = self.temperature if self.temperature else NONE_TUPLE()
            if name == TEMPERATURE:
                temp = self.get_data(val)

            name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
            if name == EXTRA_FIELDS:
                extra_fields = self.get_data(val)

            return TableData(
                [
                    [
                        (K11, k11),
                        (K12, k12),
                        (K22, k22),
                        (K13, k13),
                        (K23, k23),
                        (K33, k33),
                        (TEMPERATURE, temp),
                        (EXTRA_FIELDS, extra_fields),
                    ],
                ]
            )


class TableSpecificHeat(Table):
    def __init__(
        self,
        specific_heat: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.specificHeat = specific_heat if specific_heat else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [val if val else NONE_TUPLE() for val in [self.specificHeat]]
        lst_name = [SPECIFIC_HEAT]
        (specificHeat,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp = extra_fields = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        return TableData(
            [
                [
                    (SPECIFIC_HEAT, specificHeat),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ],
            ]
        )


class TableHeatGenerateRate(Table):
    def __init__(
        self,
        heat_generate_rate: Union[tuple, None],
        temperature: Union[tuple, None],
        **kwargs,
    ):
        self.heat_generate_rate = heat_generate_rate if heat_generate_rate else None
        self.temperature = temperature if temperature else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [val if val else NONE_TUPLE() for val in [self.heat_generate_rate]]
        lst_name = [HEAT_GENERATE_RATE]
        (heat_generate_rate,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        return TableData(
            [
                [
                    (HEAT_GENERATE_RATE, heat_generate_rate),
                    (TEMPERATURE, temp),
                ],
            ]
        )


class TableGasketMembraneElastic(Table):
    def __init__(
        self,
        youngs_modulus: Union[tuple, None],
        poissons_ratio: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.youngs_modulus = youngs_modulus if youngs_modulus else None
        self.poissons_ratio = poissons_ratio if poissons_ratio else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.youngs_modulus, self.poissons_ratio]
        ]
        lst_name = [YOUNGS_MODULUS, POISSONS_RATIO]
        youngs_modulus, poissons_ratio = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp = extra_fields = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        return TableData(
            [
                [
                    (YOUNGS_MODULUS, youngs_modulus),
                    (POISSONS_RATIO, poissons_ratio),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ],
            ]
        )


class TableGasketTransverseElastic(Table):
    def __init__(
        self,
        shear_stiffness_h: Union[tuple, None],
        shear_stiffness_v: Union[tuple, None],
        temperature_h: Union[tuple, None],
        temperature_v: Union[tuple, None],
        extra_fields_h: Union[tuple, None],
        extra_fields_v: Union[tuple, None],
        **kwargs,
    ):
        self.shear_stiffness_h = shear_stiffness_h if shear_stiffness_h else None
        self.shear_stiffness_v = shear_stiffness_v if shear_stiffness_v else None
        self.temperature_h = temperature_h if temperature_h else None
        self.temperature_v = temperature_v if temperature_v else None
        self.extra_fields_h = extra_fields_h if extra_fields_h else None
        self.extra_fields_v = extra_fields_v if extra_fields_v else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [val if val else NONE_TUPLE() for val in [self.shear_stiffness_h]]
        lst_name = [SHEAR_STIFFNESS_H]
        (shear_stiffness_h,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp_h = extra_fields_h = []

        name, val = self.temperature_h if self.temperature_h else NONE_TUPLE()
        if name == TEMPERATURE_H:
            temp_h = self.get_data(val)

        name, val = self.extra_fields_h if self.extra_fields_h else NONE_TUPLE()
        if name == EXTRA_FIELDS_H:
            extra_fields_h = self.get_data(val)

        # Vertical information
        lst_var = [val if val else NONE_TUPLE() for val in [self.shear_stiffness_v]]
        lst_name = [SHEAR_STIFFNESS_V]
        (shear_stiffness_v,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp_v = extra_fields_v = []

        name, val = self.temperature_v if self.temperature_v else NONE_TUPLE()
        if name == TEMPERATURE_V:
            temp_v = self.get_data(val)

        name, val = self.extra_fields_v if self.extra_fields_v else NONE_TUPLE()
        if name == EXTRA_FIELDS_V:
            extra_fields_v = self.get_data(val)

        return TableData(
            [
                [
                    (SHEAR_STIFFNESS_H, shear_stiffness_h),
                    (TEMPERATURE_H, temp_h),
                    (EXTRA_FIELDS_H, extra_fields_h),
                ],
                [
                    (SHEAR_STIFFNESS_V, shear_stiffness_v),
                    (TEMPERATURE_V, temp_v),
                    (EXTRA_FIELDS_V, extra_fields_v),
                ],
            ]
        )


class TableGasketThickness(Table):
    def __init__(
        self,
        pressure_force_loading: Union[tuple, None],
        closure_loading: Union[tuple, None],
        pressure_force_unloading: Union[tuple, None],
        closure_unloading: Union[tuple, None],
        plastic_max_closure_unloading: Union[tuple, None],
        temperature_loading: Union[tuple, None],
        temperature_unloading: Union[tuple, None],
        extra_fields_loading: Union[tuple, None],
        extra_fields_unloading: Union[tuple, None],
        **kwargs,
    ):
        self.pressure_force_loading = (
            pressure_force_loading if pressure_force_loading else None
        )
        self.closure_loading = closure_loading if closure_loading else None
        self.pressure_force_unloading = (
            pressure_force_unloading if pressure_force_unloading else None
        )
        self.closure_unloading = closure_unloading if closure_unloading else None
        self.max_closure_unloading = (
            plastic_max_closure_unloading if plastic_max_closure_unloading else None
        )
        self.temperature_loading = temperature_loading if temperature_loading else None
        self.temperature_unloading = (
            temperature_unloading if temperature_unloading else None
        )
        self.extra_fields_loading = (
            extra_fields_loading if extra_fields_loading else None
        )
        self.extra_fields_unloading = (
            extra_fields_unloading if extra_fields_unloading else None
        )

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.pressure_force_loading, self.closure_loading]
        ]
        lst_name = [PRESSURE_FORCE_LOADING, CLOSURE_LOADING]
        pressure_force_loading, closure_loading = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp_loading = extra_fields_loading = []

        name, val = (
            self.temperature_loading if self.temperature_loading else NONE_TUPLE()
        )
        if name == TEMPERATURE_LOADING:
            temp_loading = self.get_data(val)

        name, val = (
            self.extra_fields_loading if self.extra_fields_loading else NONE_TUPLE()
        )
        if name == EXTRA_FIELDS_LOADING:
            extra_fields_loading = self.get_data(val)

        # Unloading information
        lst_var = [
            val if val else NONE_TUPLE()
            for val in [
                self.pressure_force_unloading,
                self.closure_unloading,
                self.max_closure_unloading,
            ]
        ]
        lst_name = [
            PRESSURE_FORCE_UNLOADING,
            CLOSURE_UNLOADING,
            PLASTIC_MAX_CLOSURE_UNLOADING,
        ]
        pressure_force_unloading, closure_unloading, max_closure_unloading = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temperature_unloading = extra_fields_unloading = []

        name, val = (
            self.temperature_unloading if self.temperature_unloading else NONE_TUPLE()
        )
        if name == TEMPERATURE_UNLOADING:
            temperature_unloading = self.get_data(val)

        name, val = (
            self.extra_fields_unloading if self.extra_fields_unloading else NONE_TUPLE()
        )
        if name == EXTRA_FIELDS_UNLOADING:
            extra_fields_unloading = self.get_data(val)

        return TableData(
            [
                [
                    (PRESSURE_FORCE_LOADING, pressure_force_loading),
                    (CLOSURE_LOADING, closure_loading),
                    (TEMPERATURE_LOADING, temp_loading),
                    (EXTRA_FIELDS_LOADING, extra_fields_loading),
                ],
                [
                    (PRESSURE_FORCE_UNLOADING, pressure_force_unloading),
                    (CLOSURE_UNLOADING, closure_unloading),
                    (PLASTIC_MAX_CLOSURE_UNLOADING, max_closure_unloading),
                    (TEMPERATURE_UNLOADING, temperature_unloading),
                    (EXTRA_FIELDS_UNLOADING, extra_fields_unloading),
                ],
            ]
        )


class TableViscosity(Table):
    def __init__(
        self,
        viscosity: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.viscosity = viscosity if viscosity else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [val if val else NONE_TUPLE() for val in [self.viscosity]]
        lst_name = [VISCOSITY]
        (viscosity,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        temp = extra_fields = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        return TableData(
            [
                [
                    (VISCOSITY, viscosity),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ],
            ]
        )


class TableCohesive(Table):
    def __init__(
        self,
        stress_l: Union[tuple, None],
        strain_l: Union[tuple, None],
        stress_t: Union[tuple, None],
        strain_t: Union[tuple, None],
        stress_z: Union[tuple, None],
        strain_z: Union[tuple, None],
        stress_lt: Union[tuple, None],
        strain_lt: Union[tuple, None],
        stress_tz: Union[tuple, None],
        strain_tz: Union[tuple, None],
        stress_zl: Union[tuple, None],
        strain_zl: Union[tuple, None],
        **kwargs,
    ):
        self.stress_L = stress_l if stress_l else None
        self.strain_L = strain_l if strain_l else None
        self.stress_T = stress_t if stress_t else None
        self.strain_T = strain_t if strain_t else None
        self.stress_Z = stress_z if stress_z else None
        self.strain_Z = strain_z if strain_z else None
        self.stress_LT = stress_lt if stress_lt else None
        self.strain_LT = strain_lt if strain_lt else None
        self.stress_TZ = stress_tz if stress_tz else None
        self.strain_TZ = strain_tz if strain_tz else None
        self.stress_ZL = stress_zl if stress_zl else None
        self.strain_ZL = strain_zl if strain_zl else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        lst_var = [
            val if val else NONE_TUPLE() for val in [self.stress_L, self.strain_L]
        ]
        lst_name = [STRESS_L, STRAIN_L]
        (
            stress_L,
            strain_L,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        lst_var = [
            val if val else NONE_TUPLE() for val in [self.stress_T, self.strain_T]
        ]
        lst_name = [STRESS_T, STRAIN_T]
        (
            stress_T,
            strain_T,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        lst_var = [
            val if val else NONE_TUPLE() for val in [self.stress_Z, self.strain_Z]
        ]
        lst_name = [STRESS_Z, STRAIN_Z]
        (
            stress_Z,
            strain_Z,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        lst_var = [
            val if val else NONE_TUPLE() for val in [self.stress_LT, self.strain_LT]
        ]
        lst_name = [STRESS_LT, STRAIN_LT]
        (
            stress_LT,
            strain_LT,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        lst_var = [
            val if val else NONE_TUPLE() for val in [self.stress_TZ, self.strain_TZ]
        ]
        lst_name = [STRESS_TZ, STRAIN_TZ]
        (
            stress_TZ,
            strain_TZ,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        lst_var = [
            val if val else NONE_TUPLE() for val in [self.stress_ZL, self.strain_ZL]
        ]
        lst_name = [STRESS_ZL, STRAIN_ZL]
        (
            stress_ZL,
            strain_ZL,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]
        return TableData(
            [
                [
                    (STRESS_L, stress_L),
                    (STRAIN_L, strain_L),
                ],
                [
                    (STRESS_T, stress_T),
                    (STRAIN_T, strain_T),
                ],
                [
                    (STRESS_Z, stress_Z),
                    (STRAIN_Z, strain_Z),
                ],
                [
                    (STRESS_LT, stress_LT),
                    (STRAIN_LT, strain_LT),
                ],
                [
                    (STRESS_TZ, stress_TZ),
                    (STRAIN_TZ, strain_TZ),
                ],
                [
                    (STRESS_ZL, stress_ZL),
                    (STRAIN_ZL, strain_ZL),
                ],
            ]
        )


class TableResistivity(Table):
    def __init__(
        self,
        resistivity: Union[tuple, None],
        temperature: Union[tuple, None],
        **kwargs,
    ):
        self.resistivity = resistivity if resistivity else None
        self.temperature = temperature if temperature else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        temp = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        lst_var = [val if val else NONE_TUPLE() for val in [self.resistivity]]
        lst_name = [RESISTIVITY]
        (resistivity,) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        return TableData(
            [
                [
                    (RESISTIVITY, resistivity),
                    (TEMPERATURE, temp),
                ]
            ]
        )


class TableFatigueLimitDiagram(Table):
    def __init__(
        self,
        mean_stress: Union[tuple, None],
        stress_amplitude: Union[tuple, None],
        temperature: Union[tuple, None],
        extra_fields: Union[tuple, None],
        **kwargs,
    ):
        self.mean_stress = mean_stress if mean_stress else None
        self.stress_amplitude = stress_amplitude if stress_amplitude else None
        self.temperature = temperature if temperature else None
        self.extra_fields = extra_fields if extra_fields else None

        kwargs.clear()  # This is a necessary line
        super().__init__(**kwargs)

    def get_table_data(self) -> TableData:
        temp = extra_fields = []

        name, val = self.temperature if self.temperature else NONE_TUPLE()
        if name == TEMPERATURE:
            temp = self.get_data(val)

        name, val = self.extra_fields if self.extra_fields else NONE_TUPLE()
        if name == EXTRA_FIELDS:
            extra_fields = self.get_data(val)

        lst_var = [
            val if val else NONE_TUPLE()
            for val in [self.mean_stress, self.stress_amplitude]
        ]
        lst_name = [MEAN_STRESS, STRESS_AMPLITUDE]
        (
            mean_stress,
            stress_amplitude,
        ) = [
            self.get_data(val) if d == name else []
            for d, (name, val) in zip(lst_name, lst_var)
        ]

        return TableData(
            [
                [
                    (MEAN_STRESS, mean_stress),
                    (STRESS_AMPLITUDE, stress_amplitude),
                    (TEMPERATURE, temp),
                    (EXTRA_FIELDS, extra_fields),
                ]
            ]
        )
