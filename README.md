# Ajna
## Using Face detection and super resolution for facial feature detection and enhancement

The goal of this project was to first detect/extract faces in a frame and then apply super resolution techniques to the extracted faces to enhance the features. This project uses Keras implementations of different Residual Dense Networks for Single Image Super-Resolution (ISR) referenced through an already existing github repository, Read the full documentation at: https://idealo.github.io/image-super-resolution/. Previously I have done another project using this implementation for Video-Resolution Enhancer which can be found at : https://github.com/prateek-sibit/Video-Resolution-Enhancer

The name of the project was chosen as "Ajna" which in yogic culture corresponds to the the sixth primary chakra in the body. An activation of this chakra leads to an increase in one's perception and clarity. Going in line with this, this project uses image processing techniques to increase clarity of an input image hence the name.

## About the Files in this Project
1. Extracted : Folder containing the subdirectories of extracted faces from the input images
2. data : Contains two sub folders ->
   - input : contains the input images
   - output : contains the enhanced outputs corresponding to the input images
3. demo : folder containing a demo notebook and files for the **ISR** package
4. haarcascades : folder containing the haarcascade files which have been used for face detection
5. weights : folder containing .hdf5 weights for different models used with **ISR**
6. Ajna.ipynb : Main Notebook which is used for model creation and prediction
7. extract_faces.py : Python script responsible for extracting faces from the input images

## Results


## Applications 


## Citations

```
@misc{cardinale2018isr,
  title={ISR},
  author={Francesco Cardinale et al.},
  year={2018},
  howpublished={\url{https://github.com/idealo/image-super-resolution}},
}
```

