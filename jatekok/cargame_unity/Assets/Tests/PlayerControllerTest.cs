using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class PlayerControllerTest
{
    // A Test behaves as an ordinary method
    [Test]
    public void PlayerControllerTestSimplePasses()
    {
        // Use the Assert class to test conditions
    }

    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator PlayerControllerTestWithEnumeratorPasses()
    {
        var go = new GameObject("Player");
        var rb = go.AddComponent<Rigidbody>();
        var controller = go.AddComponent<PlayerController>();
        controller.speed = 10f;

        // Input nem mockolható, ezért kézzel adunk neki erõt
        rb.AddForce(Vector3.forward * controller.speed, ForceMode.Force);

        yield return new WaitForSeconds(0.5f);

        Assert.Greater(rb.velocity.z, 0.1f, "Player should move forward due to physics.");

    }
}
