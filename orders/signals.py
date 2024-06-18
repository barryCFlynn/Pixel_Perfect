from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create.

    This function is a signal receiver that updates the total of an order
    whenever a line item associated with the order is updated or created.

    Args:
    - sender: The model class that sends the signal.
    - instance: The instance of the model that triggered the signal.
    - created: Boolean indicating if the instance was created.
    - **kwargs: Additional keyword arguments.

    Returns:
    - None
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line item deletion.

    This function is a signal receiver that updates the total of an order
    whenever a line item associated with the order is deleted.

    Args:
    - sender: The model class that sends the signal.
    - instance: The instance of the model that triggered the signal.
    - **kwargs: Additional keyword arguments.

    Returns:
    - None
    """
    print('delete signal received!')
    instance.order.update_total()