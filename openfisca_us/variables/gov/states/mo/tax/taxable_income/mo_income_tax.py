from openfisca_us.model_api import *



class mo_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "MO income tax"
    unit = USD
    definition_period = YEAR
    reference = "https://dor.mo.gov/forms/MO-1040%20Instructions_2021.pdf"

    def formula(tax_unit, period, parameters):
        mo_income_tax_before_credits = tax_unit("mo_income_tax_before_credits", period)
        mo_property_tax_credit = tax_unit("mo_property_tax_credit", period)
        return where(mo_income_tax_before_credits > mo_property_tax_credit, mo_income_tax_before_credits - mo_property_tax_credit, 0)
