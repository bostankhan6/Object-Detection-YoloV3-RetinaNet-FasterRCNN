## A Shout out to Experiencor for creating this repo!

#### Note: This is an edited part of the the original readme file provided by Experiencor for using this repo. The link for the original repo is given below:
https://github.com/experiencor/keras-yolo3

## YOLO3 (Detection, Training, and Evaluation)

## Installing

To install the dependencies, run
```bash
pip install -r requirements.txt
```
And for the GPU to work, make sure you've got the drivers installed beforehand (CUDA).

It has been tested to work with Python 2.7.13 and 3.5.3.

**You may directly go to the "Detection" section for using the trained model (download link given below) for using it on your own Aerial Images.**

![Download the trained Yolo Model](https://drive.google.com/open?id=1BGqg6ilnZDJDpogyk-3Nxyhy2gNAiQWZ)

## Training

### 1. Data preparation 

Organize your dataset into 4 folders:

+ train_image_folder <= the folder that contains the train images.

+ train_annot_folder <= the folder that contains the train annotations in VOC format.

+ valid_image_folder <= the folder that contains the validation images.

+ valid_annot_folder <= the folder that contains the validation annotations in VOC format.
    
There is a one-to-one correspondence by file name between images and annotations. If the validation set is empty, the training set will be automatically splitted into the training set and validation set using the ratio of 0.8.

Also, if you've got the dataset split into 2 folders such as one for images and the other one for annotations and you need to set a custom size for the validation set, use `create_validation_set.sh` script to that. The script expects the following parameters in the following order:
```bash
./create_validation_set.sh $param1 $param2 $param3 $param4
# 1st param - folder where the images are found
# 2nd param - folder where the annotations are found
# 3rd param - number of random choices (aka the size of the validation set in absolute value)
# 4th param - folder where validation images/annots end up (must have images/annots folders inside the given directory as the 4th param)
```

### 2. Edit the configuration file
The configuration file is a json file, which looks like this:

```python
{
    "model" : {
        "min_input_size":       352,
        "max_input_size":       448,
        "anchors":              [16,21, 21,45, 25,79, 35,27, 42,54, 62,32, 76,95, 135,184, 238,302],
        "labels":               [
                                "Airliner",
                                "Boat",
                                "Bus",
                                "Car",
                                "CharteredAircraft",
                                "FighterAircraft",
                                "Helicopter",
                                "LongVehicle",
                                "Others",
                                "PropellerAircraft",
                                "PushbackTruck",
                                "StairTruck",
                                "TrainerAircraft",
                                "Truck",
                                "Van"
                                ]
    },

    "train": {
        "train_image_folder":   "./SIMS_Images/content/SIMS_Dataset/train_images/",
        "train_annot_folder":   "./SIMS_VOC_Annotations2/content/SIMS_VOC_Annotations2/train_annotations/",
        "cache_name":           "SIMS.pkl",

        "train_times":          2,
        "batch_size":           8,
        "learning_rate":        1e-4,
        "nb_epochs":            147,
        "warmup_epochs":        3,
        "ignore_thresh":        0.5,
        "gpus":                 "0",

        "grid_scales":          [1,1,1],
        "obj_scale":            5,
        "noobj_scale":          1,
        "xywh_scale":           1,
        "class_scale":          1,

        "tensorboard_dir":      "logs",
        "saved_weights_name":   "SIMS.h5",
        "debug":                true
    },

    "valid": {
        "valid_image_folder":   "./SIMS_Images/content/SIMS_Dataset/test_images/",
        "valid_annot_folder":   "./SIMS_VOC_Annotations2/content/SIMS_VOC_Annotations2/test_annotations/",
        "cache_name":           "SIMS_val.pkl",

        "valid_times":          1
    }
}
```

The ```labels``` setting lists the labels to be trained on. Only images, which has labels being listed, are fed to the network. The rest images are simply ignored. By this way, a Dog Detector can easily be trained using VOC or COCO dataset by setting ```labels``` to ```['dog']```.

#### Download pretrained weights for backend at:

![Download the Backend Yolo Model weights](https://drive.google.com/file/d/1huTZhkx3S7oLakaNeguaV98lleE8oYeF/view?usp=sharing)

**This weights must be put in the root folder of the repository. They are the pretrained weights for the backend only and will be loaded during model creation. The code does not work without this weights.**

### 3. Generate anchors for your dataset (optional)

`python gen_anchors.py -c config.json`

Copy the generated anchors printed on the terminal to the ```anchors``` setting in ```config.json```.

### 4. Start the training process

`python train.py -c config.json`

By the end of this process, the code will write the weights of the best model to file best_weights.h5 (or whatever name specified in the setting "saved_weights_name" in the config.json file). The training process stops when the loss on the validation set is not improved in 3 consecutive epoches.

## Perform detection using trained weights on image, set of images, video, or webcam
`python predict.py -c config.json -i /path/to/image/or/video`

It carries out detection on the image and write the image with detected bounding boxes to the same folder.

If you wish to change the object threshold or IOU threshold, you can do it by altering `obj_thresh` and `nms_thresh` variables. By default, they are set to `0.5` and `0.45` respectively.

## Evaluation

`python evaluate.py -c config.json`

Compute the mAP performance of the model defined in `saved_weights_name` on the validation dataset defined in `valid_image_folder` and `valid_annot_folder`.
