using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting.FullSerializer;
using UnityEngine;

public class AudioForVehicles : MonoBehaviour
{
    [SerializeField] AudioSource engineSounds, engineStopAudioSource;
    [SerializeField] AudioClip engineStopSound, engineSound, engineStartSound, engineMoveSound, engineMoveIdleSound, breakSound;
    GameObject gameManager;
    private bool engineStarted = false;
    PlayerController playerController;
    Rigidbody playerRb;
    private enum CarState { IDLE, MOVING, BREAKING, IDLE_MOVE};
    private CarState carState = CarState.IDLE;
    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameObject.Find("GameManager");
        playerController = gameManager.GetComponent<GameManager>().currentPlayer.GetComponent<PlayerController>();
        playerRb = playerController.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        PlayEngineStartSound();
        PlayEngineSounds();
    }

    void PlayEngineStartSound()
    {
        if (gameManager.GetComponent<GameManager>().hasSpawned == true && engineStarted == false)
        {
            engineSounds.PlayOneShot(engineStartSound);
            engineStarted = true;
            engineSounds.clip = engineSound;
            engineSounds.loop = true;
            engineSounds.Play();
        }
        
    }

    void PlayEngineSounds() 
    {
        float verticalInput = Input.GetAxis("Vertical");
        float speed  = playerRb.velocity.magnitude;
        float forwardDot = Vector3.Dot(playerController.transform.forward, playerRb.velocity.normalized);
        CarState newState = CarState.IDLE;


        if (verticalInput < 0.0f && forwardDot > 0.0f && speed > 0.1f)
        {
            newState = CarState.BREAKING;
        }
        
        else if (verticalInput == 0.0f && forwardDot == 0.0f && speed == 0.0f)
        {
            newState = CarState.IDLE;
        }

        else if (speed > 0.0f && (verticalInput < 0.0f && forwardDot < 0.0f || verticalInput > 0.0f && forwardDot > 0.0f))
        {
            newState = CarState.MOVING;
        }

        else if (speed == 0.0f && (verticalInput < 0.0f && forwardDot < 0.0f || verticalInput > 0.0f && forwardDot > 0.0f))
        {
            newState = CarState.IDLE_MOVE;
        }

        if (newState != carState)
        {
            switch (newState)
            {
                case CarState.IDLE:
                    engineSounds.clip = engineSound;
                    break;
                case CarState.MOVING:
                    engineSounds.clip = engineMoveSound;
                    break;
                case CarState.BREAKING:
                    engineSounds.clip = breakSound;
                    break;
                case CarState.IDLE_MOVE:
                    engineSounds.clip = engineMoveIdleSound;
                    break;
                default:
                    break;
            }
            engineSounds.loop = true;
            engineSounds.Play();
            carState = newState;
        }

    }

    public IEnumerator PlayEngineStopSound()
    {
        if (gameManager.GetComponent<GameManager>().isGameOver)
        {
            engineSounds.loop = false;
            engineSounds.mute = true;
            engineSounds.Stop();
            engineStopAudioSource.mute = false;
            engineStopAudioSource.PlayOneShot(engineStopSound);
            yield return new WaitForSeconds(0.1f);
            
            
        }
    }
}
