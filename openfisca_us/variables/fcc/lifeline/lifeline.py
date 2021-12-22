from openfisca_us.model_api import *


class lifeline(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Lifeline benefit amount"
    documentation = "Amount of Lifeline phone and broadband benefit"
    definition_period = YEAR
    unit = "currency-USD"

    def formula(spm_unit, period, parameters):
        max_amount = parameters(period).fcc.lifeline.amount * 12
        phone_broadband_cost = add(
            spm_unit, period, ["phone_cost", "broadband_cost"]
        )
        amount_if_eligible = min_(phone_broadband_cost, max_amount)
        eligible = spm_unit("is_lifeline_eligible", period)
        return where(eligible, amount_if_eligible, 0)
