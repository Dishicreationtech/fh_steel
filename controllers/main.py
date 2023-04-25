
from odoo import http
from odoo.http import request
import base64
import io
from PIL import Image
from datetime import datetime

class Websession(http.Controller):

    @http.route('/web/session/authenticate/api', type='json', auth="public", cors="*", csrf=False)
    def authenticate(self, db, login, password, base_location=None):
        data_auth = request.session.authenticate(db, login, password)
        if data_auth:
            data = request.env['ir.http'].session_info()
            user = request.env.user
            user_ids = request.env['res.partner'].sudo().search([("user_id", "=", user.id)])
            # ,("add_lead", "=", "dealer")
            data.update({
                'contacts': [{'id':contact.id, 'name': contact.name, 'mobile':  contact.mobile, 'email' : contact.email, 'user_id':user.id} for contact in user_ids]
                })
            return data
        else:
            return {'status_message': 200, 'contacts': {}}

    @http.route('/web/activiti/attachment/data', type='json', auth="public", cors="*", csrf=False)
    def Activiti(self, data=None):
        current_ids = request.env['res.partner'].sudo().search([('id','=', int(data.get('partner')))])
        partner_ids = request.env['res.partner'].search([('id','=', data.get('partner'))])
        partner_name = partner_ids.mapped('name')
        print('imageeeeeeeeeeee',data)
        val = False

        activty_type = request.env.ref('mail.mail_activity_data_todo').sudo()
        activity_id = request.env['mail.activity'].sudo().with_env(request.env(user=current_ids.user_id.id)).create({
                    'summary': data.get('activity_title'),
                    'note': data.get('remarks'),
                    'activity_type_id': activty_type.id,
                    'res_model_id': request.env['ir.model'].sudo().search([('model', '=', 'res.partner')],
                                                                       limit=1).id,
                    'res_model': 'res.partner',
                    'res_id' : data.get('partner'),
                    'request_partner_id' : data.get('partner'),
                    'image' : data.get('image'),
                    'user_id' : (data.get('user_id')),
                    'longitude': data.get('latitude'),
                    'latitude': data.get('longitude'),
                })
        if activity_id:
            val = True
            if data.get('images'):
                for image in data.get('images'):
                    image_data =  (image)
                    print("mmmmmmmmmmmmmmmmmmmmmm",image_data)
                    activity_id.write({'image': image_data})
            if data.get('attachment'):
                attach_data =  bytes(data.get('attachment'), encoding='utf-8')
                attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "mail.activity",
                        "res_id": activity_id.id,
                    })
                partner_attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "res.partner",
                        "res_id" : data.get('partner'),
                    })
                activity_id.attachment_id = attachment_id.id
            if data.get('attachment1'):
                attach_data =  bytes(data.get('attachment1'), encoding='utf-8')
                attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "mail.activity",
                        "res_id": activity_id.id,
                    })
                partner_attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "res.partner",
                        "res_id" : data.get('partner'),
                    })
                activity_id.attachment_id = attachment_id.id

            if data.get('attachment2'):
                attach_data =  bytes(data.get('attachment2'), encoding='utf-8')
                attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "mail.activity",
                        "res_id": activity_id.id,
                    })
                partner_attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "res.partner",
                        "res_id" : data.get('partner'),
                    })
                activity_id.attachment_id = attachment_id.id

            if data.get('attachment3'):
                attach_data =  bytes(data.get('attachment3'), encoding='utf-8')
                attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "mail.activity",
                        "res_id": activity_id.id,
                    })
                partner_attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "res.partner",
                        "res_id" : data.get('partner'),
                    })
                activity_id.attachment_id = attachment_id.id

            if data.get('attachment4'):
                attach_data =  bytes(data.get('attachment4'), encoding='utf-8')
                attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "mail.activity",
                        "res_id": activity_id.id,
                    })
                partner_attachment_id = request.env["ir.attachment"].sudo().create({
                        "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "datas":  attach_data,
                        "res_model": "res.partner",
                        "res_id" : data.get('partner'),
                    })
                activity_id.attachment_id = attachment_id.id


        return {'status_message': 200, 'activity_id': activity_id}

    #@http.route('/web/contact/create/data', type='json', auth="public", cors="*", csrf=False)
    #def Contacts(self, data=None):

    #   if data:
    #        partner_id = request.env['res.partner'].sudo().create(data)
    #        partner_id.company_type = 'company'
    #    return {'status_message': 200, 'partner_id': partner_id.name}


    @http.route('/web/contact/create/data', type='json', auth="public", cors="*")
    def Contacts(self, data=None):
        current_ids = request.env['res.partner'].sudo().search([('id','=', int(data.get('partner')))])
        partner_id = False
        if data:
            partner_id = request.env['res.partner'].sudo().with_env(request.env(user=current_ids.user_id.id)).create({
                    "name": data.get('name') or '',
                    "email": data.get('email') or '',
                    "phone": data.get('phone') or '',
                    "mobile": data.get('mobile') or '',
                    "street": data.get('street') or '',
                    "city": data.get('city') or '',
                    "add_lead": data.get('type') or '',

                })
            partner_id.company_type = 'company'
            activty_type = request.env.ref('mail.mail_activity_data_todo').sudo()
            activity_id = request.env['mail.activity'].sudo().with_env(request.env(user=current_ids.user_id.id)).create({
                    'activity_type_id': activty_type.id,
                    'res_model_id': request.env['ir.model'].sudo().search([('model', '=', 'res.partner')],
                                                                       limit=1).id,
                    'res_model': 'res.partner',
                    'res_id' : partner_id.id,
                })
            if activity_id:
                val = True
                if data.get('attachment'):
                    attach_data =  bytes(data.get('attachment'), encoding='utf-8')
                    partner_attachment_id = request.env["ir.attachment"].sudo().create({
                            "name": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "datas":  attach_data,
                            "res_model": "res.partner",
                            "res_id" : data.get('partner'),
                        })
                    activity_id.attachment_id = partner_attachment_id.id
        return {'status_message': 200, 'partner_id': partner_id.name}

