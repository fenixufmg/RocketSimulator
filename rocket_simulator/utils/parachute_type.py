import enum


class ParachuteType(enum.Enum):
    """ Tipo geométrico do paraquedas.
    """
    ANNULAR = "annular"
    BICONICAL = "biconical"
    CONICAL = "conical"
    CROSS = "cross"
    CRUCIFORM = "cruciform"
    FLAT_CIRCULAR = "flat_circular"
    HEMISPHERICAL = "hemispherical"
    TRICONICAL = "triconical"