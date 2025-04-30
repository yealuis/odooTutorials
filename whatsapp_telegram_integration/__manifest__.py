{
    'name': "WhatsApp & Telegram Integration",
    'version': '1.0',
    'summary': "Módulo para integrar las APIs de WhatsApp y Telegram en Odoo.",
    'description': """
        Este módulo permite la integración de Odoo con las APIs de WhatsApp (Business API o vía Twilio)
        y Telegram ( mediante un bot creado con BotFather), facilitando el envío y recepción de mensajes.
    """,
    'author': "yealuisia",
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        # Definir vistas, menús y acciones de configuración
        'views/whatsapp_telegram_config_views.xml',
    ],
    'installable': True,
    'application': True,
}