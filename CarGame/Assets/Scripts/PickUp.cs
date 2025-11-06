using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PickUp : MonoBehaviour
{
    GameObject gameManager;
    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameObject.Find("GameManager");
    }

    private void OnTriggerEnter(Collider other) { 
        gameManager.GetComponent<GameManager>().coinPickUpSource.PlayOneShot(gameManager.GetComponent<GameManager>().coinPickUpSound);
        gameManager.GetComponent<GameManager>().CoinCollector();
        gameManager.GetComponent<GameManager>().SpawnCoin();
        Destroy(this.gameObject); }

    // Update is called once per frame
    void Update()
    {

    }
}
