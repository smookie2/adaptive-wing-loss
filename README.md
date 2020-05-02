# adaptive-wing-loss
Keras Implementation of Adaptive Wing Loss for Robust Face Alignment via Heatmap Regression

>[Paper](https://arxiv.org/abs/1904.07399)
>
>[Official Implementation in Pytorch](https://github.com/protossw512/AdaptiveWingLoss)

## Installation
Install system requirements
- Python 3.7

Install python dependencies

```bash
pip install -r requirements.txt
```

## Dataset preparation
Dowload [WFLW dataset and annotaion](https://wywu.github.io/projects/LAB/WFLW.html), extract and place them under directory `dataset` as below:

```bash
adaptive-wing-loss
├── dataset
   ├── WFLW_annotations
   └── WFLW_images
```
