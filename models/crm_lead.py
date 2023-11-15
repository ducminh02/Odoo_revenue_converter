from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    planned_revenue_viet = fields.Monetary(string='Planned Revenue VND',
                                           currency_field='currency_id',
                                           compute="_compute_planned_revenue_viet",
                                           #                                     track_visibility='always'
                                           )
    currency_id = fields.Many2one('res.currency', string='Currency')



    @api.depends("planned_revenue", "currency_id")
    def _compute_planned_revenue_viet(self):
        """
        compute the VND from planned revenue
        """

        for rec in self:
            rec.planned_revenue_viet = rec.planned_revenue * rec.currency_id.rate
            print(f'rec.planned_revenue: {rec.planned_revenue} rec.currency_id.rate: {rec.currency_id.rate}')
