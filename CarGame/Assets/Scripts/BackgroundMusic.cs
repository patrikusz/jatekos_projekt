using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BackgroundMusic : MonoBehaviour
{
    [SerializeField] AudioSource musicSource;
    [SerializeField] AudioClip musicSound;
    // Start is called before the first frame update
    public void Start()
    {
        musicSource.clip = musicSound;
        musicSource.volume = 0.5f;
        musicSource.loop = true;
        musicSource.Play();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
