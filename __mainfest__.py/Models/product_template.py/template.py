                from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _check_low_stock_and_notify(self):
        low_stock_products = self.env['product.product'].search([
            ('qty_available', '<', 10),
            ('type', '=', 'product'),  # Filter out services
        ])
        sales_users = self.env['res.users'].search([('groups_id.name', '=', 'Sales')])

        for product in low_stock_products:
            message = f"สินค้า '{product.name}' มีสต็อกเหลือน้อยกว่า 10 ชิ้น ({int(product.qty_available)} ชิ้น)."
            for user in sales_users:
                self.env['mail.message'].create({
                    'model': 'product.product',
                    'res_id': product.id,
                    'message_type': 'notification',
                    'subtype_id': self.env.ref('mail.mt_note').id,
                    'body': message,
                                'partner_ids': [(...