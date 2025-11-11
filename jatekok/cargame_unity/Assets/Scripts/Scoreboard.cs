using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class Scoreboard : MonoBehaviour
 
{
    public float highScore = 0;
    GameObject gameManager;
    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameObject.Find("GameManager");

        if (gameManager == null)
        {
            Debug.LogWarning("GameManager not found in scene — using DummyGameManager for testing.");
            gameManager = new GameObject("GameManager");
            gameManager.AddComponent<DummyGameManager>();
        }
    }

    public void Update()
    {
        if (gameManager == null)
            return;

        var gm = gameManager.GetComponent<GameManager>();
        if (gm != null)
        {
            HighScore(gm.win, gm.score);
            return;
        }

        var dummy = gameManager.GetComponent<DummyGameManager>();
        if (dummy == null)
        {
            dummy = gameManager.AddComponent<DummyGameManager>();
        }

        HighScore(dummy.win, dummy.score);
    }


    public void HighScore(bool isWin, float score)
    {
        if (isWin == true)
        {
            if (highScore <= score)
            {
                highScore = score;
            }
        }
    }

 
}
