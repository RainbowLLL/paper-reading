### 2020-ECCV-Local Correlation Consistency for Knowledge Distillation

## 概述

​		知识蒸馏，现有方法主要考虑样本层面特征及它们之间的关系的一致性，忽视了局部特征与关系。

​		本文探究局部关系用于知识蒸馏。对三种局部知识进行建模，样本间局部关系、样本内相同位置局部关系、样本内不同位置局部关系。此外，为了使学生专注于教师特征图的那些信息丰富的局部区域，提出了一个新颖的类感知注意模块，以突出显示与类别相关的区域，并消除与类别无关的区域，这使局部相关知识更加丰富、准确而有价值。在CIFAR100和ImageNet上进行了实验。

 

​    Hinton提出的蒸馏

![img](imgs\clip_image002.png)

  基于特征关系的蒸馏

​		![img](imgs\clip_image004.png)

二元相似度关系

![img](imgs\clip_image006.jpg)

---



## 局部关系构建

​    把教师和学生网络分成几个阶段，用三种不同的方式建立相似度矩阵，然后最小化学生和教师之间的相似度

​    

​    ![img](imgs\clip_image008.jpg)

* 样本内不同位置：一种比较松弛的方式来表征单张图像特征间的关系
* 样本间相同位置：一个mini-batch中不同图像相同位置间关系， 比全局关系更严格
* 样本间不现位置：与第二种方式相比包含更丰富的知识

​    

![img](imgs\clip_image010.jpg)

![img](imgs\clip_image012.jpg) ![img](imgs\clip_image014.jpg)

![img](imgs\clip_image016.jpg)

 

 

三种关系联合起来作为最后的损失函数。

 

**这种基于局部相关性的关系主要有两个优点**

* 一是局部特征有这一类别更多的细节信息，因此能引入有利于蒸馏的更多的判别知识。例如ImageNet中许多类都属于一个大类，只有小的局部区域不同，其他区域都很相似。本文这种基于局部特征的方法，能够较好的捕获并迁移这种局部的模式。

* 二是，本文的方法探究了不同种类的关系，比之前的方法更加充分。

---



### 类别注意力（Class-Aware Attention）

原图中有一些无关信息，对最终的预测没有效果甚至有负作用，为提取高度相关和语义信息，引入class-aware attenetion module来过滤无关信息。

 

此模块包括两部分：一个mask生成器和一个辅助分类器。CAAT用ground-truth作为监督，产生pixel级别的attention mask。

 

![img](imgs\clip_image017.png)

外层函数为Mask生成网络，由一些conv-bn-relu层加上sigmoid层，因此第个值都在0-1之间，每个值反映了该位置对最终预测的贡献，对于不同通道的同一位置，使用相同的mask

对mask重复排列C次，可以让mask与feature map的维度相同。然后逐点相乘得到带有类别注意力的feature map。

![img](imgs\clip_image019.jpg)

为了引导mask生成网络的训练，进一步引入了一个辅助分类器，它以带注意力的feature map作为输入，用ground truth作为label进行监督学习。

![img](imgs\clip_image021.jpg)

 ## 实验部分

