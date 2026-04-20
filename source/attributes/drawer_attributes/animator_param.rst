AnimatorParam
=============
Select an Animator paramater via dropdown interface::

    public class NaughtyComponent : MonoBehaviour
    {
        public Animator someAnimator;

        [AnimatorParam(nameof(someAnimator))]
        public int paramHash;

        [AnimatorParam(nameof(someAnimator))]
        public string paramName;
    }

.. image:: ../../images/AnimatorParam_Inspector.png
