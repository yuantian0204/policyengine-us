from policyengine_us.model_api import *


class mt_gross_household_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Montana Gross Household Income"
    defined_for = StateCode.MT
    unit = USD
    definition_period = YEAR
