class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

















# class Invoice:
#   def __str__(self):
#     return "This is the invoice class!"

#     #__init__


# inv = Invoice()
# print(str(inv))

# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def __str__(self):
#     return f"Invoice from {self.client} for {self.total}"

# inv = Invoice('Google', 500)
# print(str(inv))

# __init_  #this is a dunder =__

# class string

# private/protected

# 'my name'.uppercase