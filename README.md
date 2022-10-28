# sensor-fault-detection
### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections
![193536736-5ccff349-d1fb-486e-b920-02ad7974d089](https://user-images.githubusercontent.com/48283027/198582102-040fb4d2-0a3e-4fdd-94ca-4af4a5c1951b.png)

## Project Archietecture
![193536768-ae704adc-32d9-4c6c-b234-79c152f756c5](https://user-images.githubusercontent.com/48283027/198582316-2af90173-e5e5-472a-8617-1bca070ba70f.png)

## Deployment Archietecture
![193536973-4530fe7d-5509-4609-bfd2-cd702fc82423](https://user-images.githubusercontent.com/48283027/198581576-16d96b75-3abc-4c98-a2d5-45384b4ef02b.png)
