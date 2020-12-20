Ordered Set
###########
A dead simple set that preserves insertion order, internally using the
python's 3.7 dict, which preserves order.

``pip install ordered-set-37``

This class subclasses and implements all the methods of ``MutableSet``.

.. code-block:: python

   from ordered_set_37 import OrderedSet
   x = OrderedSet([1, 2, -1, "bar"])
   x.add(0)
   assert list(x) == [1, 2, -1, "bar", 0]


This library uses the typing system, so feel free to do:

.. code-block:: python

  x: OrderedSet[str] = OrderedSet(("foo", "bar"))
  x.add(1)  # type checkers won't like this as it is not a string



As an extra, you can access a value by index (although the speed is at worst O(n)):

.. code-block:: python

  x = OrderedSet(["foo", "bar", "baz"])
  assert x[1] == "bar"

For obvious reasons, this library is only Python 3.7+ compatible.

Feel free to contribute, fork, etc.
