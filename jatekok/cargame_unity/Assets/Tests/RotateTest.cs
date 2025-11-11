using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class RotateTest
{
    // A Test behaves as an ordinary method
    [Test]
    public void RotateTestSimplePasses()
    {
        var go = new GameObject("RotatingObject");
        var rotate = go.AddComponent<Rotate>();

        Quaternion start = go.transform.rotation;

        // Manuálisan meghívjuk az Update()-et párszor
        for (int i = 0; i < 5; i++)
        {
            rotate.Update();
        }

        Quaternion end = go.transform.rotation;

        Assert.AreNotEqual(start, end, "Rotation should change after multiple Update() calls.");
    }

    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator RotateTestWithEnumeratorPasses()
    {
        // Use the Assert class to test conditions.
        // Use yield to skip a frame.
        yield return null;
    }
}
