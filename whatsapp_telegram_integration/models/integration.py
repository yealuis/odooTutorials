from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class WhatsAppTelegramConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    whatsapp_api_token = fields.Char(string="Token API WhatsApp", help="Token para la API de WhatsApp.")
    whatsapp_phone_id = fields.Char(string="Phone ID", help="Identificador del teléfono para la API de WhatsApp.")
    telegram_bot_token = fields.Char(string="Token Bot Telegram", help="Token del bot de Telegram.")

    def send_whatsapp_message(self, to_number, message):
        """Ejemplo de función para enviar mensaje mediante la API de WhatsApp Business"""
        api_url = f"https://graph.facebook.com/v13.0/{self.whatsapp_phone_id}/messages"
        headers = {'Authorization': f'Bearer {self.whatsapp_api_token}', 'Content-Type': 'application/json'}
        payload = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {"body": message}
        }
        try:
            response = requests.post(api_url, json=payload, headers=headers)
            response.raise_for_status()
            _logger.info("Mensaje de WhatsApp enviado correctamente.")
            return response.json()
        except Exception as e:
            _logger.error("Error al enviar mensaje de WhatsApp: %s", e)
            return {'error': str(e)}

    def send_telegram_message(self, chat_id, message):
        """Ejemplo de función para enviar mensaje desde Telegram Bot API"""
        api_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        try:
            response = requests.post(api_url, data=payload)
            response.raise_for_status()
            _logger.info("Mensaje de Telegram enviado correctamente.")
            return response.json()
        except Exception as e:
            _logger.error("Error al enviar mensaje de Telegram: %s", e)
            return {'error': str(e)}