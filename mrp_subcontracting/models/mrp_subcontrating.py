
# -*- encoding: utf-8 -*-
##############################################################################
#
#    Incaser Informatica (incaser@incaser.es) Date: 17/10/2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from openerp import models, fields


class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    external = fields.Boolean('External', help="Is Subcontract Operation")
    semifinished_id = fields.Many2one(
            'product.product', 'Semifinished Subcontracting',
            domain=[('type','=','product')])
    picking_type_id = fields.Many2one('stock.picking.type', 'Picking Type',
                                      domain[('code','=','outgoing')])
    virtual_subcontracting_location_id = fields.Many2one('stock.location',
                                    'Virtual Subcontrating Location')
    out_subcontracting_location_id = fields.Many2one('stock.location',
                                    'Consumption Subcontrating Location')
    in_subcontracting_location_id = fields.Many2one('stock.location',
                                    'Destination Subcontrating Location')

class MrpProductionWorkcenterLine(models.Model):
    _inherit = 'mrp.production.workcenter.line'

    sale_order_id = fields.Many2one('sale.order', 'Sale Order')
    out_picking_id = fields.Many2one('stock.picking', 'Out Picking')
    in_picking_id = fields.Many2one('stock.picking', 'In Picking')

