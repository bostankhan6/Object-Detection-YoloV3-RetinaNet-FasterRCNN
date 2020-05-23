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

## Results
The hypermeters that have been used for trainings of the 3 architecture models can be found in their respective repos. Different Epochs and learning rates have been used for different architectures. The batch size of 4, however, was consitent for all because the models were trained either on Colab or a VM both of which had Tesla K80 (12GB GPU Memory).

### Quantitative Results
Mean Average Precision (mAP) has been used as the performance metric for quantitative results given below.

| Model      | Validation mAP       | Test mAP             |
|------------|----------------------|----------------------|
| YoloV3     | 0.6453               | 0.6307               |
| RetinaNet  | 0.6706               | 0.6613               |
| FasterRCNN | 0.6590               | 0.6853               |

The detailed mAP values for each class of the dataset are in the respective folders of the detection methods.

### Qualitative Results:

#### YoloV3

![YoloV3Result](/YoloV3%20SIMS/results/0122.jpg)

#### RetinaNet

![RetinaNetResult](/Retinanet/results/Retinanet%20result1.png)

![RetinaNetResult](/Retinanet/results/Retinanet%20result.png)

#### Faster RCNN

![FRCNN Result](https://github.com/bostankhan6/Object-Detection-YoloV3-RetinaNet-FasterRCNN/blob/master/Faster%20RCNN/images/1.png)

![FRCNN Result](https://github.com/bostankhan6/Object-Detection-YoloV3-RetinaNet-FasterRCNN/blob/master/Faster%20RCNN/images/2.png)

### Training Graphs

#### YoloV3 Loss Graph
![YoloV3Loss](/YoloV3%20SIMS/results/loss_graph.jpg)

#### RetinaNet Classification Loss Graph
![RetinaNetClassificationLoss](/Retinanet/results/classification_loss.jpg)

#### RetinaNet Regression Loss Graph
![RetinaNetRegressionLoss](/Retinanet/results/regression_loss.jpg)

## Contact
Bostan Khan (bostankhan6@gmail.com)

## Acknowledgements
[Implementation of YoloV3 in Keras by Experiencor](https://github.com/experiencor/keras-yolo3)

[Implementation of Retinanet in Keras by Fizyr](https://github.com/fizyr/keras-retinanet)

