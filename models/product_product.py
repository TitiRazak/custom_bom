# # Copyright 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# # License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    price = fields.Float(string="", store=True)
