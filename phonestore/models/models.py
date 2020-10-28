# -*- coding: utf-8 -*-

from odoo import models, fields


class Manufacturer(models.Model):
    _name = 'phonestore.manufacturer'
    _description = 'Manufacturers of Phones'

    name = fields.Char(string="Name", required=True)
    model_ids = fields.One2many('phonestore.model',
                                'manufacturer_id',
                                string="Models")


class Model(models.Model):
    _name = 'phonestore.model'
    _description = 'Models of Phones'

    name = fields.Char(string="Name", required=True)
    manufacturer_id = fields.Many2one('phonestore.manufacturer',
                                      string='Manufacturer',
                                      ondelete='cascade',
                                      required=True,)


class Phone(models.Model):
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one('phonestore.manufacturer',
                                      string='Manufacturer',
                                      ondelete='cascade')
    model_id = fields.Many2one('phonestore.model',
                               string='Model',
                               ondelete='cascade')
