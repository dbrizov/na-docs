ShowNativeProperty
==================
Shows native C# properties in the inspector.
It supports only certain types ``bool``, ``int``, ``long``, ``float``, ``double``, ``string``,
``Vector2``, ``Vector3``, ``Vector4``, ``Color``, ``Bounds``, ``Rect``, ``UnityEngine.Object``.

.. warning::
    Doesn't work on properties that are nested inside serialized structs of classes.

::

    public class NaughtyComponent : MonoBehaviour
    {
        public List<Transform> transforms;

        [ShowNativeProperty]
        public int TransformsCount => transforms.Count;
    }

.. image:: ../../images/ShowNativeProperty_Inspector.png
