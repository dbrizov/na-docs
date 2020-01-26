.. _label-min-max-slider:

MinMaxSlider
============
A double slider. The **min value** is saved to the **X** property, and the **max value** is saved to the **Y** property of a **Vector2** field::

    public class NaughtyComponent : MonoBehaviour
    {
        [MinMaxSlider(0.0f, 100.0f)]
        public Vector2 minMaxSlider;
    }

.. image:: ../../images/MinMaxSlider_Inspector.png
