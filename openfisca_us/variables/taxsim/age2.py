from openfisca_us.model_api import *


class age2(Variable):
    value_type = int
    entity = TaxUnit
    label = "Age of second dependent"
    unit = "year"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_dependent = person("is_tax_unit_dependent", period)
        age = person("age", period)
        dependent_rank = person.get_rank(tax_unit, age, is_dependent)
        is_first_dependent = dependent_rank == 1
        return tax_unit.sum(age * is_first_dependent)