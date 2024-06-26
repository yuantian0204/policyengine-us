from policyengine_us.model_api import *


class spm_unit_wic_reported(Variable):
    value_type = float
    entity = SPMUnit
    label = "SPM unit reported WIC"
    definition_period = YEAR
    unit = USD
