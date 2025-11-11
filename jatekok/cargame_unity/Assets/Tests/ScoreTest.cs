using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEditor.Build.Content;
using UnityEngine;
using UnityEngine.TestTools;

public class ScoreTest
{
    // A Test behaves as an ordinary method
    [Test]
    public void ScoreTestSimplePasses()
    {
        // Use the Assert class to test conditions
    }

    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator ScoreTestWithEnumeratorPasses()
    {
        var gameManager = new GameObject("GameManager");
        var scoreBoard = new GameObject("Scoreboard");
        var gm = gameManager.AddComponent<DummyGameManager>();
        var sb = scoreBoard.AddComponent<Scoreboard>();
        gm.win = false;
        gm.score = 50.0f;

        yield return null;

        sb.Update();
        Assert.AreEqual(0f, sb.highScore, "HighScore should not update while game is over, but you not win.");
        gm.win = false;

        gm.score = 50.0f;
        gm.win = true;
        yield return null;

        sb.Update();
        Assert.AreEqual(50f, sb.highScore, "HighScore should update when game is over and you win.");
        gm.win = false;

        gm.score = 100.0f;
        gm.win = true;
        yield return null;

        sb.Update();
        Assert.AreEqual(100f, sb.highScore, "HighScore should update when game is over and you win.");
        gm.win = false;

        gm.score = 75.0f;
        gm.win = true;
        yield return null;  

        sb.Update();
        Assert.AreEqual(100f, sb.highScore, "HighScore should not update when game is over and you win.");
        gm.win = false;
    }
}
