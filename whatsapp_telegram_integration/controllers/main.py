from odoo import http
import json
import logging

_logger = logging.getLogger(__name__)

class WhatsAppTelegramController(http.Controller):

    @http.route('/whatsapp_telegram/webhook', type='json', auth='public', csrf=False, methods=['POST'])
    def webhook(self, **kwargs):
        # Puedes validar la autenticidad de la petición aquí (por ejemplo, comprobando tokens)
        _logger.info("Webhook recibido: %s", json.dumps(kwargs))
        # Procesa la información recibida y actualiza los registros en Odoo según corresponda
        return {"status": "ok"}
