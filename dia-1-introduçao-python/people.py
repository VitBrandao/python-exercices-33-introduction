import area  # poderia também ser: 'from area import rectangle'

PEOPLE_PER_SQUARE_METER = 2  # numero de pessoas por metro quadrado em média
FIELD_LENGTH = 60  # em metros
FIELD_WIDTH = 45  # em metros

formula = area.rectangle(FIELD_LENGTH, FIELD_WIDTH) * PEOPLE_PER_SQUARE_METER
people_at_concert = formula


print("Estão presentes no show aproximadamente", people_at_concert, "pessoas.")
