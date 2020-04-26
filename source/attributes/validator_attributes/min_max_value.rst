MinValue / MaxValue
===================
Clamps integer and float fields.

.. note::
    If you want to use it on fields that are nested inside serialized structs or classes
    you need to use the :ref:`label-allow-nesting` attribute.

::

    public class NaughtyComponent : MonoBehaviour
    {
        [MinValue(0), MaxValue(10)]
        public int myInt;

        [MinValue(0.0f)]
        public float myFloat;
    }

.. image:: ../../images/MinValueMaxValue_Inspector.gif
