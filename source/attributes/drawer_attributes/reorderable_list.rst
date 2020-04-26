ReorderableList
===============
Provides array type fields with an interface for easy reordering of elements.

.. warning::
    Doesn't work on lists that are nested inside serialized structs of classes.

::

    public class NaughtyComponent : MonoBehaviour
    {
        [ReorderableList]
        public int[] intArray;

        [ReorderableList]
        public List<float> floatArray;
    }

.. image:: ../../images/ReorderableList_Inspector.gif
