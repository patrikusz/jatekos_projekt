using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class FollowPlayerTest
{
    // A Test behaves as an ordinary method
    [Test]
    public void FollowPlayerTestSimplePasses()
    {
        // Use the Assert class to test conditions
    }

    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator FollowPlayerTestWithEnumeratorPasses()
    {
        var gameManagerObj = new GameObject("GameManager");
        var gm = gameManagerObj.AddComponent<DummyGameManager>();  // Dummy verzió a cursorLocked-hoz
        gm.cursorLocked = true;

        var cameraObj = new GameObject("Camera");
        var followPlayer = cameraObj.AddComponent<FollowPlayer>();

        var playerObj = new GameObject("Player");
        playerObj.transform.position = Vector3.zero;

        followPlayer.SetPlayer(playerObj);

        // --- Teszt: alap offset beállítás ---
        Assert.NotNull(followPlayer.player, "A player referencia nincs beállítva.");
        Assert.AreEqual(playerObj.transform, followPlayer.player, "A SetPlayer nem állította be helyesen a playert.");

        // --- Teszt: kamera követi a playert ---
        Vector3 oldPosition = cameraObj.transform.position;

        // Mozgatjuk a playert kicsit
        playerObj.transform.position = new Vector3(0, 0, 10);

        // LateUpdate hívás szimulálása
        followPlayer.LateUpdate();

        yield return null;

        Vector3 newPosition = cameraObj.transform.position;
        Assert.AreNotEqual(oldPosition, newPosition, "A kamera pozíciója nem változott, pedig a player elmozdult.");

        // --- Teszt: kamera nézze a playert ---
        Vector3 lookDir = (playerObj.transform.position + Vector3.up * 2.5f) - cameraObj.transform.position;
        Assert.That(Vector3.Dot(cameraObj.transform.forward.normalized, lookDir.normalized), Is.GreaterThan(0.9f),
            "A kamera nem a player felé néz.");
    }
}
