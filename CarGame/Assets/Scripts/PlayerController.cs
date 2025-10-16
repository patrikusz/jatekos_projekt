using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed, rotationSpeed;
    Rigidbody rb;


    private void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.maxLinearVelocity = speed;
    }

    void FixedUpdate()
    {
        float verticalInput = Input.GetAxis("Vertical");
        rb.AddForce(transform.forward * speed * Time.deltaTime * verticalInput, ForceMode.Impulse);

        //float horizontalInput = Input.GetAxis("Horizontal");
        //rb.AddTorque(transform.up * rotationSpeed * Time.deltaTime * horizontalInput, ForceMode.Impulse);
    }

    void Update()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        transform.Rotate(Vector3.up, horizontalInput * rotationSpeed * Time.deltaTime);

        //float verticalInput = Input.GetAxis("Vertical");
        //transform.Translate(Vector3.forward * speed * Time.deltaTime * verticalInput);

    }


}


