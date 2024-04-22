from policyengine_us.model_api import *


class ar_additional_credit(Variable):
    value_type = float
    entity = Person
    label = "Arkansas additional credit"
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2023_AR1000F_and_AR1000NR_Instructions.pdf#page=26"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR

    def formula(person, period, parameter):
        # Use individual or joint income based on filing status
        filing_separately = person.tax_unit("ar_files_separately", period)
        taxable_income_indiv = person("ar_taxable_income_indiv", period)
        taxable_income_joint = person("ar_taxable_income_joint", period)
        taxable_income = where(
            filing_separately, taxable_income_indiv, taxable_income_joint
        )
        p = parameter(period).gov.states.ar.tax.income.credits.additional
        # Only head or spouse can claim this credit
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        # The credit amount is doubled for married couples filing jointly
        amount = p.amount.calc(taxable_income)
        total_amount = where(filing_separately, amount, amount * 2)
        return total_amount * head_or_spouse
