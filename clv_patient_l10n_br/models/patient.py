# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class Patient(models.Model):
    _inherit = 'clv.patient'

    def do_patient_clear_address_data(self):

        for address in self:

            data_values = {}

            data_values['street_name'] = False
            data_values['street'] = False
            data_values['street_number'] = False
            data_values['street_number2'] = False
            data_values['street2'] = False
            data_values['zip'] = False
            data_values['city'] = False
            data_values['city_id'] = False
            data_values['state_id'] = False
            data_values['country_id'] = False
            # data_values['phone'] = False
            # data_values['mobile'] = False

            address.write(data_values)
