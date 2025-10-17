using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed, rotationSpeed;
    Rigidbody rb;
    AudioForVehicles audioForVehicles;
    float verticalInput;

    private void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.maxLinearVelocity = speed;
    }

    void FixedUpdate()
    {
        verticalInput = Input.GetAxis("Vertical");
        rb.AddForce(transform.forward * speed * verticalInput, ForceMode.Force);

        //float horizontalInput = Input.GetAxis("Horizontal");
        //rb.AddTorque(transform.up * rotationSpeed * Time.deltaTime * horizontalInput, ForceMode.Impulse);
    }

    void Update()
    {
        if (rb.velocity.magnitude > 0.5f)
        {
            float horizontalInput = Input.GetAxis("Horizontal");
            transform.Rotate(Vector3.up, horizontalInput * rotationSpeed * Time.deltaTime);
        }
        

        //float verticalInput = Input.GetAxis("Vertical");
        //transform.Translate(Vector3.forward * speed * Time.deltaTime * verticalInput);

    }


}


