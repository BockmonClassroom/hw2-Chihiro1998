[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AV-xh9XP)
# HW2
DS5110  
Homework 2 - Data Collection  
Due 1/24/2025

**Author**：Yuchen(Oliva) Kuang<br>
**Detail**: Question answer for DS5110 HW2<br>

## Date Collections
### 1.Explain your data collection process
I chose to collect data from potted plants in the coffee shop where I used to study, because it is not a good season to go to the botanical garden, and the trees outside the school are too tall for me. I collected data from three different plants: Zamioculcas zamiifolia, Snake plant and Bunny ears cactus. I randomly selected 20 leaves from each plant for measurement, using the App Measure to measure distance and a regular ruler to record their leaf width and leaf length, and confirmed the plant name through the plant identification App - PictureThis. My collection work detail is mainly as follows：<br>
**Location**： K Coffee Bar<br>
**Step 1** Once I have found the plant, use the mobile app PictureThis to identify the plant species and mark the area.<br>
**Step 2** Use a ruler to measure the length and width of each leaf in millimeters.<br>
**Step 3** Record the measurements and the plant name in a notebook and then transcribe them into a spreadsheet.<br>
**Step 4** Repeat the above steps until I have collected data for all three plants.<br>
<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/user-attachments/assets/52a8347f-8416-42ca-9955-2a0945a8082e" width="200"/>
  <img src="https://github.com/user-attachments/assets/ce9562f4-5efe-4528-bc02-c2e65fd45192" width="200"/>
  <img src="https://github.com/user-attachments/assets/dacd7191-11fa-4afb-a932-d659daed120c" width="200"/>
</div>
<br>

### 2.What instrument did you use to collect data with? 
During the data collection process, I used the following tools:<br>
**Ruler**: A regular ruler. If there is a caliper, the data will be more accurate, but I didn’t buy it.<br>
**Mobile application (PictureThis and Measure)**: used to identify the species and name of plants and to preliminarily measure the length and width of plant leaves.<br>
<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/user-attachments/assets/1b438b7f-240c-448e-9e45-ecb09dd20d07" width="200"/>
  <img src="https://github.com/user-attachments/assets/dee8a8fa-01a3-4309-b55b-9fd20c0e7171" width="200"/>
  <img src="https://github.com/user-attachments/assets/9c515596-393e-4a28-9473-b307793a656f" width="200"/>
</div>
<br>

**Notebook and pen**: used to manually record measurement data and preliminarily mark the data measurement points.<br>
**Spreadsheet tool (Google Sheets)**: used to organize and store data.<br>

### 3. Argue the accuracy and precision of your instrument. 
**Ruler**: The accuracy of the caliper is 0.1 mm, but the general ruler I use has an accuracy of 1 mm. If conditions permit, I think the caliper will be better. However, the leaves are flexible and may cause some slight errors, so I will try to flatten the leaves when measuring.<br>
**Plant identification application**: The accuracy of identifying common plants is high, but there may be errors for some uncommon plants. I verified the accuracy of the name by referring to multiple identification results and comparing the pictures and real objects searched by Google.<br>
**Manual recording**: Manual recording may have transcription errors, so I checked whether the records were complete after data collection.<br>

### 4. How many data points did you collect? Why? 
I collected a total of 60 data points, 20 of which were collected for each plant (N=60, each subset n=20). The 20 data points were chosen to strike a balance between the amount of data and the workload. This sample size is sufficient for basic statistical analysis (such as mean and variance calculations). More data may yield more accurate results, but considering operability, I chose 20 data points/each plant.<br>

### 5. Define the size of your data in terms of both N (full data set size) and n (each subset size). 
**Total dataset size (N)**: 60 data.<br>
**Each subset size (n)**: Each plant corresponds to a subset, containing 20 data.<br>

### 6. Explain any problems that you ran into during the data collection process. 
During the data collection process, I encountered the following issues:<br>
**Accuracy of plant identification**: The leaves of some plants are very similar, and plant identification applications sometimes provide multiple similar results. To solve this problem, I confirmed the plant name by referring to Google search images for comparison.<br>
**Leaf shape problem**: Some leaves are naturally curled or damaged, making it difficult to obtain accurate data when measuring. I tried to choose intact and flat leaves, and unfolded them by hand when necessary.<br>
**Data precision and accuracy issues**: It is difficult to determine the widest point of the leaf and which two points are the longest value. For this, I marked the two points of measurement on a leaf with a water-based pen and measured multiple times to find the average value to determine that the data is a more accurate data.<br>

## Analysis/Visualization
Introduction：All the graphs' original format in the Graph folder.<br>
### 1. Graph histograms of your data with appropriate labels. 
<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/user-attachments/assets/187a16b9-522f-4dd6-9880-753f8e9a9eea" width="800"/>
  <img src="https://github.com/user-attachments/assets/3a7119d4-9440-43a9-83f2-4a0773968f86" width="800"/>
</div>
<br>

### 2. Graph boxplots of your data with appropriate labels. 
<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/user-attachments/assets/1f8c193c-004d-4c2c-ac77-048ff36f9e17" width="800"/>
</div>
<br>

### 3. Graph a scatter plot of your entire data set with each subset different color and a ledger.
<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/user-attachments/assets/5f16303a-6a2f-401e-b4b9-dc63f29e4430" width="800"/>
</div>
<br>

### 4. Explain each graph in terms of variance, mean, median, and standard deviation. 
#### 4.1 Histograms
Histograms show the frequency distribution of leaf width and leaf length for all plants and each plant species.<br>
**Leaf Width**:<br>
Zamioculcas zamiifolia: The histogram shows a concentrated distribution around 3 cm. This aligns with the mean 3.10and the median 3.15, as they are close, indicating symmetry in the distribution. The standard deviation 0.48and variance 0.23suggest that the data points are tightly clustered.<br>
Snake Plant: The data is concentrated around 6 cm. The mean 6.04 and median 6.20suggest the distribution is slightly skewed toward larger values. The small standard deviation 0.49indicates low dispersion.<br>
Bunny Ears Cactus: The histogram shows a wider spread of data, with the most frequent values near 3-4 cm. The mean 3.85 is larger than the median 3.20, indicating a right-skewed distribution. The standard deviation 1.46 and variance 2.12 indicate high variability compared to the other plants.<br>
All: The histogram shows a bimodal distribution caused by the separation of Snake Plant (higher leaf width) and the other two plants (lower leaf width). The large variance 2.41 and standard deviation 1.55 reflect this broad spread.<br>
**Leaf Length**:<br>
Zamioculcas zamiifolia: The histogram indicates data concentrated between 7-8 cm, which matches the mean 7.35 and median 7.50. The variance 0.56 and standard deviation 0.75 confirm a narrow distribution.<br>
Snake Plant: The data ranges widely from 14 to 26 cm. The mean 19.39 and median 18.25 indicate a slight left skew. The high variance 16.25 and standard deviation 4.03 reflect the data's spread.<br>
Bunny Ears Cactus: The histogram shows peaks around 6-8 cm. The mean 7.21 and median 6.80 are close, suggesting symmetry, but the higher variance 7.57 and standard deviation 2.75 suggest a wider spread.<br>
All: The histogram shows a multimodal distribution, reflecting the distinct characteristics of each plant. The large variance 41.01 and standard deviation 6.40 reflect the data's diversity.<br>
#### 4.2 Boxplots
Box plots summarize the distribution of leaf width and leaf length for all plants and each species, highlighting the central tendency, spread, and outliers.<br>
**Leaf Width:** <br>
Zamioculcas zamiifolia: The box is narrow, indicating concentrated data. The median is near the center, aligning with the mean 3.10. The whiskers (range) are short, confirming the small variance 0.23 and standard deviation 0.48.<br>
Snake Plant: The boxplot shows a tight distribution around 6 cm. The median is slightly above the mean, consistent with the data's slight right skew.<br>
Bunny Ears Cactus: The box is wider, with a longer whisker on the right side, reflecting the higher variance 2.12 and a few outliers. The median 3.20 cm is smaller than the mean 3.85 cm, indicating right skewness.<br>
All Plants: The overall boxplot shows a large spread, with multiple modes corresponding to each plant's characteristics.<br>


**statistics:**
<blockquote>
  <strong>Statistics for Leaf Width:</strong><br>
  <blockquote>
    <strong>Zamioculcas zamiifolia:</strong><br>
    Mean: 3.10<br>
    Variance: 0.23<br>
    Median: 3.15<br>
    Standard Deviation: 0.48<br>
  </blockquote>
  <blockquote>
    <strong>Snake Plant:</strong><br>
    Mean: 6.04<br>
    Variance: 0.24<br>
    Median: 6.20<br>
    Standard Deviation: 0.49<br>
  </blockquote>
  <blockquote>
    <strong>Bunny Ears Cactus:</strong><br>
    Mean: 3.85<br>
    Variance: 2.12<br>
    Median: 3.20<br>
    Standard Deviation: 1.46<br>
  </blockquote>
  <blockquote>
    <strong>All Plants:</strong><br>
    <blockquote>
      Mean: 4.33<br>
      Variance: 2.41<br>
      Median: 3.80<br>
      Standard Deviation: 1.55<br>
    </blockquote>
  </blockquote>
</blockquote>

<blockquote>
  <strong>Statistics for Leaf Length:</strong><br>
  <blockquote>
    <strong>Zamioculcas zamiifolia:</strong><br>
    Mean: 7.35<br>
    Variance: 0.56<br>
    Median: 7.50<br>
    Standard Deviation: 0.75<br>
  </blockquote>
  <blockquote>
    <strong>Snake Plant:</strong><br>
    Mean: 19.39<br>
    Variance: 16.25<br>
    Median: 18.25<br>
    Standard Deviation: 4.03<br>
  </blockquote>
  <blockquote>
    <strong>Bunny Ears Cactus:</strong><br>
    Mean: 7.21<br>
    Variance: 7.57<br>
    Median: 6.80<br>
    Standard Deviation: 2.75<br>
  </blockquote>
  <blockquote>
    <strong>All Plants:</strong><br>
    <blockquote>
      Mean: 11.31<br>
      Variance: 41.01<br>
      Median: 8.20<br>
      Standard Deviation: 6.40<br>
    </blockquote>
  </blockquote>
</blockquote>





