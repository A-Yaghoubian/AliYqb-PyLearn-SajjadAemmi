# Face Recognition 😀
> Ability to distinguish 12 famous people from each other using **TensorFlow**. [Check in](https://drive.google.com/drive/folders/1WGSotRtFPYGuxPEGkWWRsBPlVXFSvl7p?usp=sharing)

This code uses a network that I designed myself, called _AliNet_.

| Model  | Train Acc | Train Loss | Val Acc | Val Loss | Epochs |
|  :-:   |   :-:     |     :-:    |   :-:   |   :-:    |  :-:   |
| AliNet |  98.22%   |   0.0046   |   89%   |  0.0204  |   24   |

### Charts
> You can access charts via [WandB](https://wandb.ai/aliyaghoubian/Face%20Recognition?workspace=user-aliyaghoubian)

### Inference
````shell
  usage: python3 inference.py [Image Path] [Weights Path]
````
