.. _label-enable-disable-if:

EnableIf / DisableIf
====================
Can be used to make serialized fields or buttons ``readonly`` based on some condition.
The condition can be a ``field``, ``property`` or ``function``.

.. note::
    If you want to use it on fields that are nested inside serialized structs or classes
    you need to use the :ref:`label-allow-nesting` attribute.

::

    public class NaughtyComponent : MonoBehaviour
    {
        public bool enableMyInt;

        [EnableIf("enableMyInt")]
        public int myInt;

        [EnableIf("Enabled")]
        public float myFloat;

        [EnableIf("NotEnabled")]
        public Vector3 myVector;

        public bool Enabled() { return true; }

        public bool NotEnabled => false;
    }

.. image:: ../../images/EnableIf_Inspector.gif

You can also have more than one condition::

    public class NaughtyComponent : MonoBehaviour
    {
        public bool flag0;
        public bool flag1;

        [EnableIf(EConditionOperator.And, "flag0", "flag1")]
        public int enabledIfAll;

        [EnableIf(EConditionOperator.Or, "flag0", "flag1")]
        public int enabledIfAny;
    }
