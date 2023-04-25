# See README.rst file on addons root folder for license details

from odoo import api, fields, models
from geopy.geocoders import Nominatim


class MailActivity(models.Model):
    _inherit = "mail.activity"
    _rec_name = "user_id"

    # notes = fields.Text(string="Notes")
    image = fields.Binary('Image', attachment=True)
    filename = fields.Char('filename')
    attachment_id = fields.Many2one('ir.attachment', string="Attachment", index=True)
    longitude = fields.Char(string="longitude")
    latitude =  fields.Char(string="latitude")
    date_deadline = fields.Date('Date', index=True, required=True, default=fields.Date.context_today)
    location = fields.Char(string="Location", compute='_compute_location')

    @api.depends('longitude', 'latitude')
    def _compute_location(self):
        for activity in self:
            geolocator = Nominatim(user_agent="geoapiExercises")
            if activity.longitude and activity.latitude:
                activity.location = geolocator.geocode(activity.longitude + "," + activity.latitude)
            else:
                activity.location = ''

class Users(models.Model):
    _inherit = 'res.users'

    notification_type = fields.Selection([
        ('email', 'Handle by Emails'),
        ('inbox', 'Handle in System')],
        'Notification', required=True, default='email',
        help="Policy on how to handle Chatter notifications:\n"
             "- Handle by Emails: notifications are sent to your email address\n"
             "- Handle in System: notifications appear in your System Inbox")

    hierarchy_map = fields.Selection([
        ('management', 'Management'), 
        ('gm', 'GM'), 
        ('bm', 'BM'), 
        ('asm', 'ASM'), 
        ('aso', 'ASO')], string="Hierarchy Mapping")


class ResPartner(models.Model):
    _inherit = 'res.partner'


    add_lead = fields.Selection([
        ('customer', 'Customer'), 
        ('fabricator', 'Fabricator'), 
        ('dealer', 'Dealer'),], string="Type")


    dealer = fields.Many2one('res.partner',string="Dealer")



    image = fields.Binary('Image', attachment=True)
    filename = fields.Char('filename')
    attachment_id = fields.Many2one('ir.attachment', string="Attachment", index=True)
    longitude = fields.Char(string="longitude")
    latitude =  fields.Char(string="latitude")
    date_deadline = fields.Date('Date', index=True, required=True, default=fields.Date.context_today)
    location = fields.Char(string="Location", compute='_compute_location')






    # @api.onchange('add_lead')
    # def onchange_terms_id(self):
    #     self.dealer = self.dealer.add_lead.id





