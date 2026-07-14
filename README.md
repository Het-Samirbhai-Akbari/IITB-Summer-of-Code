# IITB Summer of Code

Tracking my weekly progress, code, and notes for the IITB Summer of Code. I am updating this repo as I work through the program!

## Weekly Progress

### Week 1: Setup & Python Fundamentals
Kicked off the program by setting up the development environment and mastering core Python programming concepts.
* **Environment:** Set up the local Linux (WSL) environment, Jupyter Notebooks, and established a clean Git/GitHub workflow.
* **Core Syntax:** Covered the building blocks of Python, including variables, dynamic data types, and control flow logic (`if/else` statements, loops).
* **Data Structures:** Learned built-in structures like lists and tuples to store, organize, and manipulate data.


### Week 2: Machine Learning
Got into the meat of Machine Learning, covering the math and implementation behind the core algorithms.
* **The Basics:** Understanding what ML actually is, defining Cost Functions, and optimizing them with Gradient Descent.
* **Data Prep & Feature Engineering:** Handling categorical data using Dummy Variables and One-Hot Encoding, plus reducing dimensions using PCA.
* **Supervised Learning:** Built models using Linear Regression, Logistic Regression, Support Vector Machines (SVM), and Naive Bayes.
* **Tree-Based Models:** Explored Decision Trees and Random Forests, alongside ensemble techniques like Bagging.
* **Unsupervised Learning:** Grouped data using K-Means Clustering.
* **Evaluation & Tuning:** Tested model reliability with K-Fold Cross Validation and prevented overfitting using L1/L2 Regularization.

### Week 3: Deep Learning
Transitioned from traditional ML to Deep Learning, building neural networks from scratch and diving heavy into Computer Vision.
* **Foundations & Frameworks:** What Deep Learning is, the core Python stack (TensorFlow & Keras), and the math behind the magic (Matrices, Derivatives, and the Chain Rule).
* **Neural Network Core:** Designing Neural Networks, understanding Activation Functions, defining Loss/Cost Functions, and optimizing with Stochastic vs. Batch Gradient Descent.
* **Tuning & Tooling:** Handled Imbalanced Datasets, applied Dropout Regularization to fight overfitting, and worked on a Customer Churn prediction model. Also tracked training with TensorBoard and ran GPU Benchmarking.
* **Computer Vision & CNNs:** Tackled Image Classification using Convolutional Neural Networks (CNNs). Explored the mechanics of Convolution (Padding and Stride), used Data Augmentation to address overfitting, and leveraged Transfer Learning to speed up training.
* **Advanced Vision Concepts:** Explored spatial mapping with Image Segmentation and Object Detection, comparing Sliding Window Object Detection against modern architectures like YOLO.
* *(Note: The raw datasets used this week were massive, so they are excluded via `.gitignore` to keep the repo fast and clean!)*

##  Tools & Libraries
* Python & Jupyter Notebooks
* Pandas, NumPy, Matplotlib
* Scikit-Learn
* TensorFlow & Keras

## Week 4: Intro to LLMs

This week was focused on learning the basics of large language models — understanding what LLMs are and how they work.

## Week 5: Exploratory Data Analysis

This week I learned about EDA and data cleaning techniques in Python, understanding the basic concepts and workflow involved in preparing data.

## Week 6: Training the YOLOv8 Model

This was the core computer vision week. I trained a YOLOv8 model to detect surface defects on steel — things like scratches, patches, pitted surfaces, and rolled-in scale. I converted the dataset's annotations into the format YOLO needs, set up the training configuration, and ran several training experiments to find the best-performing setup. At the end of it, I had a trained model saved as `best.pt` that could reliably detect these defect types in new images.

## Weeks 7 & 8: Building the Final Application — DeFekt.AI

For the final project, I built a complete web application called **DeFekt.AI** using Streamlit. Here's what it does:

- A user uploads an image of a steel surface
- My trained YOLOv8 model runs and detects any defects in the image
- The app shows the original image next to the same image with bounding boxes drawn around each detected defect
- The detected defects are sent to a locally running LLM (Llama 3.2, through Ollama) which writes a professional inspection report — including a summary, severity rating, and recommended actions
- Everything is displayed cleanly in the web app

I also added something extra beyond what was required: a chatbot at the bottom of the report where I can ask follow-up questions about the defects that were found, and it answers based on the actual results from that specific image.

---
Built by [Het Samirbhai Akbari](https://github.com/Het-Samirbhai-Akbari)
