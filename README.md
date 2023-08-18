# cvdl_ss23

## Project: Vision-Based Approach to Noisy Text Recognition

Member: Han Yang, Yian Yu

### Requirements
 * python 3.6, pip

### Structure: 

Dataset: [link](dataset)

Train file (also contains evaluation code): [link](model/CNN_train.ipynb)

Evaluation file: [link](model/CNN_evaluate.ipynb)

Result of model trained with Noto-Sans: [link](model/CNN_noto_sans)

Result of model trained with mandatory: [link](model/CNN_08_11_18_28_03_mandatory)

Result of model trained with Turok: [link](model/CNN_08_11_18_17_53_turok)

Result of model trained with Typographer: [link](model/CNN_08_11_18_04_00_typographer)

Slide: [link](report/SS23CV&DL-HanYANG-YianYU-Slide.pdf)

Report: [link](report/Report-HanYANG-YianYU.pdf)

Our trained model: [link](https://drive.google.com/drive/folders/1xBEqIwnwxeQifTPyx4qfNNKoSe4PJdJ9)

Our video: [link](https://drive.google.com/file/d/1-JUROBlSOLcN5M21Ci_TEvUzzm_RNmI0/view)

*Update:*

For Your Interest: We also updated our intermediate images, which are generated in step **image rendering** by `pygame`.

intermediate images: [link](https://1drv.ms/u/s!AqR9pJ12LnwoiZg0lu90_BiJ6pw_mA?e=VH2PIk)

### Architechture
![Alt text](doc/CNN_structure.png)

### Progress

- [x] Dictionary \{word : id\}

- [x] Dictionary \{id : word\}

- [x] word frequency \{word : num\}

- [x] Dataset and Dataloader: [Tutorial 1](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html), [Tutorial 2](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)

- [x] Training

    - Train loss

    - ![Alt text](doc/example_CNN_1_train_loss.png)

    1. Test without noise

        ![Alt text](doc/example_CNN_1_1.png)


    2. Test with 1 noise

        ![Alt text](doc/example_CNN_1_2.png)

    3. Test with many noise

        ![Alt text](doc/example_CNN_1_3.png)
        
        ![Alt text](doc/example_CNN_1_4.png)

- [x] loss, acc

- [x] eval: automatic noise, parameters, proportion, noise type

- [x] eval: dataset / dataloader for noised data

- [x] eval: noise function

- [x] eval: test accuracy

- [x] eval: test accuracy with different noise, proportion

- [x] eval: move evaluation to a seperate file

- [x] optimize: to_image() better file name, contains original word

- [x] optimize: file name, contains font, noise name

- [x] automatic, clean code, automatic read and save config files


### Done Experiments

1. 4 Models with 4 Fonts

2. For each model

    1. accuracy without noise, 4 results in total

    2. accuracy with 3 different noise
   
    3. accuracy with 5 different noise level (0.1, 0.2, 0.3, 0.4, 0.5)

    In total: $4  \text{model(fonts)} * 3 \text{type of noise} * 5 \text{noise level}  + 4 \text{accuracy without noise}  = 64$
