from odoo import api, fields, models, _


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    price_unit = fields.Float('Prix Unitaire', compute='_compute_price', store=True)
    price_subtotal = fields.Float('Sous-total', compute='_compute_subtotal', store=True)

    @api.depends('price_unit', 'product_qty')
    def _compute_subtotal(self):
        if self.product_id:
            for line in self:
                line.price_subtotal = line.price_unit * line.product_qty

    @api.onchange('product_id')
    def onchange_product_id(self):
        return super(MrpBomLine, self).onchange_product_id() and self._compute_price()

    @api.depends('product_id')
    def _compute_price(self):
        for rec in self:
            rec.price_unit = rec.product_id.lst_price


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    price_total = fields.Float('Prix', compute='_compute_total_price', store=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        return super(MrpBom, self)._onchange_product_id() and self._compute_total_price()

    @api.depends('bom_line_ids')
    def _compute_total_price(self):
        for bom in self:
            total_price = 0.0
            for line in bom.bom_line_ids:
                total_price += line.price_subtotal
            bom.update({'price_total': total_price})
