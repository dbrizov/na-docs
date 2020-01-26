.. _label-enable-disable-if:

EnableIf / DisableIf
====================
Can be used to make serialized fields ``readonly`` based on some condition.
The condition can be a ``field``, ``property`` or ``function``::

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

.. note::
    If you want to use it on serialized fields that are nested inside serialized structs or classes
    you need to use the :ref:`label-allow-nesting` attribute::

        public class EnableIfTest : MonoBehaviour
        {
            public EnableIfNest nest;
        }

        [System.Serializable]
        public struct EnableIfNest
        {
            public bool enableFlag;

            [EnableIf("enableFlag")]
            [AllowNesting] // Because it's nested we need to explicitly allow nesting
            public int integer;
        }
