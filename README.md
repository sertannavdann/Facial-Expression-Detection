# Facial Expression Recognition

This project implements a facial expression recognition system using Convolutional Neural Networks (CNN) and Visual Transformers (Multi-Head Attention). The FER2013 dataset is augmented using various image processing techniques to improve the model's performance. The final model is exported as an ONNX file for deployment.

## Description
This facial expression recognition system combines the strengths of Convolutional Neural Networks (CNN) and Visual Transformers (Multi-Head Attention). The FER2013 dataset is used as the basis for training and testing, with multiple augmentation techniques applied to improve the model's generalization capabilities.

<p align="center">
  <img src="https://i0.wp.com/developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png?fit=1200%2C564&ssl=1" width="400" alt="Image">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*inc9Sty8xMFNNYlNVn9iBQ.png" width="400" alt="Image">
</p>

### Live Deployment

The live deployment takes the ONNX file and applies it to a live video stream. Faces are detected using Haar cascades, resized to match the model's input dimensions, and then passed through the model. The output is the class (emotion) with the highest probability.

<p align="center">
  <img src="Accuracy&LossMaps/take1.png" alt="Powell Project Outline" width="600" />
</p>

### CPP Version

A C++ version of the project compiles everything into a 4 MB executable. It generates a graph of the detected emotions and saves it in JSON format.

<p align="center">
  <img src="Accuracy&LossMaps/elon.png" alt="Elon Musk" width="600" />
  <img src="Accuracy&LossMaps/jim.png" alt="Jim Carrey" width="600" />
  <img src="Accuracy&LossMaps/trump.png" alt="Donald Trump" width="600" />
</p>

### Accuracies & Architecture
<h3> CNN & Multi-Head Attention </h3>
<p>
  Multi-head attention is a technique that allows a neural network to attend to different parts of the input sequence simultaneously, enabling it to capture complex relationships between different parts of the input. In the context of CNNs used for facial expression detection, multi-head attention can be applied to the sequential layer, allowing the network to focus on different parts of the face at the same time. This can improve the network's ability to capture subtle changes in facial expressions that may be indicative of different emotions. Overall, the combination of CNNs and multi-head attention can be a powerful tool for accurately detecting facial expressions.
</p>
<p align="center">
  <img src="Accuracy&LossMaps/accuracy_graph_Adam.png" alt="MobileNet2 accuracy" width="500" />
  <img src="Accuracy&LossMaps/loss_graph_Adam.png" alt="MobileNet2 loss" width="500" />
</p>

### Copyright 2023 @CC - Sertan Avdan

<h3>This work is licensed under a Creative Commons Attribution 4.0 International License. </h3>
<p> <strong> Commercial Use Must Contact - Sertan Avdan </strong> </p> 
sertan.avdan@outlook.com
