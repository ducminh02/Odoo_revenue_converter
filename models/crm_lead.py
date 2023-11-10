from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    planned_revenue_viet = fields.Float('Planned Revenue VND',
                                       default="Ask me tomorrow",
                                       compute="_compute_planned_revenue_viet",
                                       track_visibility='always')

    @api.depends("planned_revenue")
    def _compute_planned_revenue_viet(self):
        """
        compute the VND from planned revenue
        """
        for rec in self:
            rec.planned_revenue_viet = rec.planned_revenue * 26088

