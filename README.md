# Object-Detection-YoloV3-RetinaNet-FasterRCNN
Object Detection In Satellite Images Using Deep Learning (Retinanet-YOLO-Faster-FRCNN). The models have been trained on a private datset.

# About the Dataset:
Satellite Imagery Multi-vehicles Dataset (SIMD) contains 5,000 images of 1024 x 768 resolution and collectively contains 45,303 objects in 15 different classes of vehicles. The source images are taken from public satellite imagery available in Google Earth and contain images of multiple locations from seven countries. The classes are as follows:

| Classes     | Classes       | Classes           |
|-------------|---------------|-------------------|
| Car         | Others        | Airliner          |
| Truck       | StairTruck    | PropellerAircraft |
| Van         | PushbackTruck | TrainerAircraft   |
| LongVehicle | Helicopter    | CharteredAircraft |
| Bus         | Boat          | FighterAircraft   |

#### Project Status: [Active]

## Architectures and Network Diagrams

### RetinaNet:
![Retinanet](/Retinanet/images/The-network-architecture-of-RetinaNet-RetinaNet-uses-the-Feature-Pyramid-Network-FPN.png)

### YoloV3:
![YoloV3](/YoloV3%20SIMS/images/The-framework-of-YOLOv3-neural-network-for-ship-detection.jpg)

### Faster RCNN:
![FasterRCNN](/Faster%20RCNN/images/Faster%20RCNN.png)

## Deep Learning Libraries:
The above implementations are dependent upon **Keras** and **Tensorflow** deep learning libraries.

## Usage of Repos:
Working instructions of the three architectures are given in their respective folders in this repo. The dependencies are mentioned along with how to train, evaluate and predict. The links of the trained models have also been provided and can be used to predict on your own setellite imagery.

