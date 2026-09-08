#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None, previous_transactions=None):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    self.previous_transactions = previous_transactions if previous_transactions is not None else []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    if not isinstance(discount, int) or discount < 0 or discount > 100:
      raise ValueError("Not valid discount")
    else:
      self._discount = discount

  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    self.items.extend([title] * quantity)
    self.previous_transactions.append(price * quantity)

  def apply_discount(self):
    if self.discount > 0 and self.items:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      self.previous_transactions[-1] = self.total
      print(f"After the discount, the total comes to ${self.total:g}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.previous_transactions:
      last = self.previous_transactions.pop()
      self.total -= last
