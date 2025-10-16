using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HumanMove : MonoBehaviour
{
    private bool isMovingRight = true;
    private float xLeft = -30.0f;
    private float xRight = 30.0f;
    public float speed = 10.0f;
    private bool hasStarted = false;
    Animator animator;
    GameObject gameManager;


    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        gameManager = GameObject.Find("GameManager");
    }

    public void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            gameManager.GetComponent<GameManager>().GameOver(false);
        }
    }

    // Update is called once per frame
    IEnumerator MoveRightLeft()
    {
        animator.SetBool("isRunning", false);
        yield return new WaitForSeconds(Random.Range(3, 5));
        animator.SetBool("isRunning", true);

        while (true)
        {
            if (GameObject.Find("GameManager").GetComponent<GameManager>().isGameOver)
            {
                animator.SetBool("isRunning", false);
                yield break;
            }

            if (isMovingRight)
            {
                transform.Translate(Vector3.forward * Time.deltaTime * gameManager.GetComponent<GameManager>().humanSpeed);
                if (transform.position.x >= xRight)
                {
                    isMovingRight = false;
                    transform.Rotate(new Vector3(0.0f, 180.0f, 0.0f));
                    animator.SetBool("isRunning", false);
                    yield return new WaitForSeconds(Random.Range(1, 3));
                    animator.SetBool("isRunning", true);
                }
            }
            else
            {
                transform.Translate(Vector3.forward * Time.deltaTime * gameManager.GetComponent<GameManager>().humanSpeed);
                if (transform.position.x <= xLeft)
                {
                    isMovingRight = true;
                    transform.Rotate(new Vector3(0.0f, 180.0f, 0.0f));
                    animator.SetBool("isRunning", false);
                    yield return new WaitForSeconds(Random.Range(1, 3));
                    animator.SetBool("isRunning", true);
                }
            }

            yield return null;
        }
    }


    void Update()
    {
        if (!hasStarted && gameManager.GetComponent<GameManager>().currentPlayer != null && gameManager.GetComponent<GameManager>().hasSpawned == true)
        {
            hasStarted = true;
            StartCoroutine(MoveRightLeft());
            Debug.Log("Elindult!");
        }
    }
}
