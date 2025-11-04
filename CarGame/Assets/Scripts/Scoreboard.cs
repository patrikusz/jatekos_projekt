using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class Scoreboard : MonoBehaviour
 
{
    GameObject gameManager;
    List<float> time;
    GameManager gameManagerScript;
    [SerializeField] public Button scoreboardButton;
    [SerializeField] Button backButton;
    [SerializeField] TextMeshProUGUI scoreText;
    private string allTimes = "";
    // Start is called before the first frame update
    void Start()
    {
        backButton.gameObject.SetActive(false);
        scoreText.gameObject.SetActive(false);
        gameManager = GameObject.Find("GameManager");
        gameManagerScript = gameManager.GetComponent<GameManager>();
        scoreboardButton.gameObject.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {
        if (gameManagerScript.isGameOver)
        {
           time.Add(gameManagerScript.timeCounter);
           time.Sort();
        }
    }

    public void ShowScoreboard()
    {
        backButton.gameObject.SetActive(true);
        scoreboardButton.gameObject.SetActive(false);
        gameManagerScript.difficulty.gameObject.SetActive(false);
       
        
        for (int i = 0; i < time.Count; i++)
        {
            allTimes += $"Your time: {time[i]:F2}\n";
        }
        scoreText.SetText(allTimes);
        scoreText.gameObject.SetActive(true);
    }

    public void BackButton()
    {
        gameManagerScript.RestartGame();
    }
}
