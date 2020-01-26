ProgressBar
===========
Draws a progress bar::

    public class NaughtyComponent : MonoBehaviour
    {
        [ProgressBar("Health", 300, EColor.Red)]
        public int health = 250;

        [ProgressBar("Mana", 100, EColor.Blue)]
        public int mana = 25;

        [ProgressBar("Stamina", 200, EColor.Green)]
        public int stamina = 150;
    }

.. image:: ../../images/ProgressBar_Inspector.png
