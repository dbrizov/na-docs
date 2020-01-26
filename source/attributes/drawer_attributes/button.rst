Button
======
A method can be marked as a button. A button appears in the inspector and executes the method if clicked.
Works both with instance and static methods::

    public class NaughtyComponent : MonoBehaviour
    {
        [Button]
        private void MethodOne() { }

        [Button("Button Text")]
        private void MethodTwo() { }
    }

.. image:: ../../images/Button_Inspector.png

.. warning::
    The Button attribute cannot be nested inside serialized structs or classes.
