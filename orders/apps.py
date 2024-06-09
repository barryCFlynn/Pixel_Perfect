from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'orders'

    def ready(self):
        import orders.signals
