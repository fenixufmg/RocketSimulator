def critical_reynolds_number(material_roughness: float, rocket_length: float) -> float:
    return 51 * (material_roughness / rocket_length) ** -1.039