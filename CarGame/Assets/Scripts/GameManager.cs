using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public AudioSource coinPickUpSource;
    public AudioClip coinPickUpSound;
    [SerializeField] TextMeshProUGUI carOrBusText, scoreText, timeText, gameOverText;
    [SerializeField] List<GameObject> vehicle, obstacles;
    [SerializeField] FollowPlayer cameraFollow;
    [SerializeField] GameObject coin, difficulty;
    [SerializeField] Button buttonRestart;
    CapsuleCollider coinCollider;
    public GameObject currentPlayer;
    private int maxCoin = 5, countCoin = 0, timeCounter = 0, index = -1, carOrBusNum, randomNum;
    public bool hasSpawned = false, isGameOver = false, isChoosing, cursorLocked = false;
    public float humanSpeed;
    private bool hasStarted = false;


    void Start()
    {

        isChoosing = false;
        isGameOver = false;

        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;

        // Mindig jelenjenek meg a nehézségi gombok a játék elején
        difficulty.gameObject.SetActive(true);

        // Minden más UI elem legyen elrejtve
        carOrBusText.gameObject.SetActive(false);
        scoreText.gameObject.SetActive(false);
        buttonRestart.gameObject.SetActive(false);
        timeText.gameObject.SetActive(false);
        gameOverText.gameObject.SetActive(false);

        if (cameraFollow == null)
        {
            cameraFollow = FindObjectOfType<FollowPlayer>();
        }
    }



    void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            RestartGame();
        }
        
        if (isGameOver) return;

        if (carOrBusText.gameObject.activeSelf == false)
        {
            return;
        }
        else
        {
            SpawnCarBus();
        }


        if (!hasStarted && hasSpawned)
        {
            hasStarted = true;
            StartCoroutine(TimeCounter());
        }
    }



    public void DiffButtonHandler()
    {
        difficulty.gameObject.SetActive(false);
        carOrBusText.gameObject.SetActive(true);
    }

    public void EasyDiff()
    {
        Vector3 newPosition;
        float xC;
        float zC;
        for (int i = 0; i < 35; i++)
        {
            do
            {
                xC = Random.Range(-28, 28);
                zC = Random.Range(-8, 184);
            }
            while (xC > -7 && xC < 7 && zC > -7 && zC < 7);
            randomNum = Random.Range(0, 4);
            newPosition = new Vector3(xC, 0, zC);
            Instantiate(obstacles[randomNum], newPosition, Quaternion.identity);
            humanSpeed = 10.0f;
        }
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
        cursorLocked = true;
        SpawnCoin();
    }

    public void MediumDiff()
    {
        Vector3 newPosition;
        float xC;
        float zC;
        for (int i = 0; i < 65; i++)
        {
            do
            {
                xC = Random.Range(-28, 28);
                zC = Random.Range(-8, 184);
            }
            while (xC > -7 && xC < 7 && zC > -7 && zC < 7);
            randomNum = Random.Range(0, 4);
            newPosition = new Vector3(xC, 0, zC);
            Instantiate(obstacles[randomNum], newPosition, Quaternion.identity);
            humanSpeed = 15.0f;
        }
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
        cursorLocked = true;
        SpawnCoin();
    }

    public void HardDiff()
    {
        Vector3 newPosition;
        float xC;
        float zC;
        for (int i = 0; i < 85; i++)
        {
            do
            {
                xC = Random.Range(-28, 28);
                zC = Random.Range(-8, 184);
            }
            while (xC > -7 && xC < 7 && zC > -7 && zC < 7);

            randomNum = Random.Range(0, 4);
            newPosition = new Vector3(xC, 0, zC);
            Instantiate(obstacles[randomNum], newPosition, Quaternion.identity);
        }
        humanSpeed = 20.0f;
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
        cursorLocked = true;
        SpawnCoin();
    }

    private bool IsPositionOccupied(Vector3 position, LayerMask mask)
    {
        Collider[] colliders = Physics.OverlapSphere(position, 0.5f, mask);
        return colliders.Length > 0;
    }



    void SpawnCarBus()
    {
        if (isGameOver) return;

        if (hasSpawned)
        {
            carOrBusText.gameObject.SetActive(false);
            scoreText.gameObject.SetActive(true);
            timeText.gameObject.SetActive(true);
            scoreText.SetText("Coins: {0}/{1}", countCoin, maxCoin);
            return;
        }

        //Choose Car or Bus

        if (!isChoosing)
        {
            if (Input.GetKeyDown(KeyCode.Alpha2) || Input.GetKeyDown(KeyCode.Keypad2))
            {
                carOrBusText.SetText("Press 1 for Bus or press 2 for Van");
                isChoosing = true;
                carOrBusNum = 2;
                return;
            }

            else if (!isChoosing && (Input.GetKeyDown(KeyCode.Alpha1) || Input.GetKeyDown(KeyCode.Keypad1)))
            {
                carOrBusText.SetText("Press 1 for Blue Car or press 2 for Red Car");
                isChoosing = true;
                carOrBusNum = 1;
                return;
            }
        }


        //CarSpawn


        if (isChoosing && carOrBusNum == 1)
        {
            if (Input.GetKeyDown(KeyCode.Alpha1) || Input.GetKeyDown(KeyCode.Keypad1))
            {
                index = 0;

            }

            else if (Input.GetKeyDown(KeyCode.Alpha2) || Input.GetKeyDown(KeyCode.Keypad2))
            {
                index = 1;
            }
            if (index != -1)
            {
                currentPlayer = Instantiate(vehicle[index], vehicle[index].transform.position, vehicle[index].transform.rotation);
                currentPlayer.name = vehicle[index].name;
                cameraFollow.SetPlayer(currentPlayer);
                currentPlayer.GetComponent<PlayerController>().enabled = true;
                Debug.Log("SPAWNOLT AUTÓ ÉS ÁTADTA A CAMERÁNAK: " + currentPlayer.name);
                hasSpawned = true;

            }

        }


        //BusSpawn


        if (isChoosing && carOrBusNum == 2)
        {
            if (Input.GetKeyDown(KeyCode.Alpha1) || Input.GetKeyDown(KeyCode.Keypad1))
            {
                index = 2;
            }
            else if (Input.GetKeyDown(KeyCode.Alpha2) || Input.GetKeyDown(KeyCode.Keypad2))
            {
                index = 3;
            }
            if (index != -1)
            {
                currentPlayer = Instantiate(vehicle[index], vehicle[index].transform.position, vehicle[index].transform.rotation);
                currentPlayer.name = vehicle[index].name;
                cameraFollow.SetPlayer(currentPlayer);
                currentPlayer.GetComponent<PlayerController>().enabled = true;
                Debug.Log("SPAWNOLT BUSZ ÉS ÁTADTA A CAMERÁNAK: " + currentPlayer.name);
                hasSpawned = true;
            }
        }
    }

    IEnumerator TimeCounter()
    {
        while (!isGameOver)
        {
            yield return new WaitForSeconds(1);
            timeCounter++;
            timeText.SetText("Time: {0}", timeCounter);
        }
    }

    public void SpawnCoin()
    {
        if (isGameOver) return;
        Vector3 newPosition;
        float xC;
        float zC;

        if (countCoin >= maxCoin)
        {
            return;
        }
        else
        {
            LayerMask mask = LayerMask.GetMask("Obstacles", "Coins");

            do
            {
                do
                {
                    xC = Random.Range(-28, 28);
                    zC = Random.Range(-8, 184);
                }
                while (xC > -7 && xC < 7 && zC > -7 && zC < 7);
                newPosition = new Vector3(xC, 1, zC);

            }
            while (IsPositionOccupied(newPosition, mask));
            GameObject newCoin = Instantiate(coin, newPosition, coin.transform.rotation);
            coinCollider = newCoin.GetComponent<CapsuleCollider>();
            coinCollider.isTrigger = true;
        }
    }

    public void CoinCollector()
    {
        if (isGameOver) return;

        countCoin++;
        scoreText.SetText("Coins: {0}/{1}", countCoin, maxCoin);

        if (countCoin == maxCoin)
        {
            GameOver(true);
        }
    }

    public void RestartGame()
    {
        buttonRestart.gameObject.SetActive(false);
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void GameOver(bool isWin)
    {
        if (isGameOver) return;
        isGameOver = true;
        StartCoroutine(GameOverSequence(isWin));
        
    }

    private IEnumerator GameOverSequence(bool isWin)
    {
        var audioForVehicles = currentPlayer.GetComponent<AudioForVehicles>();

        if (audioForVehicles != null)
        {
            yield return StartCoroutine(audioForVehicles.PlayEngineStopSound());
            timeText.gameObject.SetActive(false);
            scoreText.gameObject.SetActive(false);

            if (isWin)
            {
                gameOverText.SetText("Your time : {0} sec", timeCounter);
            }
            else
            {
                gameOverText.SetText("You lost!");
            }

            gameOverText.gameObject.SetActive(true);
            buttonRestart.gameObject.SetActive(true);
            cursorLocked = false;
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
        }



        yield return new WaitForSeconds(0.1f);
        StopAllCoroutines();
        currentPlayer.GetComponent<PlayerController>().enabled = false;
    }
}
