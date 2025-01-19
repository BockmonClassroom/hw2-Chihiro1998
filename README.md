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
Histograms show the frequency distribution of leaf width and leaf length for all plants and each plant species.

**Leaf Width**:<br>
- **Zamioculcas zamiifolia**:  
  Most leaf widths are around 3 cm, which matches the mean 3.10 and median 3.15. The data is very consistent, as shown by the small standard deviation 0.48 and variance 0.23.  
- **Snake Plant**:  
  The majority of leaf widths are near 6 cm, with a mean of 6.04 and median of 6.20. The distribution is slightly skewed toward larger values, but overall the data is consistent, with a standard deviation of 0.49.  
- **Bunny Ears Cactus**:  
  The data is more spread out, with leaf widths mostly between 3 and 4 cm. The mean is 3.85, higher than the median 3.20, indicating some larger leaf widths pulling the average up. The standard deviation 1.46 and variance 2.12 are higher, reflecting greater variability.  
- **All Plants**:  
  The histogram shows two peaks, one near 3 cm (for Zamioculcas and Bunny Ears) and another near 6 cm (for Snake Plant). The large variance 2.41 and standard deviation 1.55 reflect the broad spread of data across different species.

**Leaf Length**:<br>
- **Zamioculcas zamiifolia**:  
  Most leaf lengths fall between 7 and 8 cm, with a mean of 7.35 and median of 7.50. This shows a symmetric and consistent distribution. The standard deviation 0.75 is small, indicating little variation.  
- **Snake Plant**:  
  Leaf lengths range from 14 to 26 cm, with a mean of 19.39 and median of 18.25. The data shows a wide spread, with a standard deviation of 4.03 and variance of 16.25.  
- **Bunny Ears Cactus**:  
  Most leaf lengths are between 6 and 8 cm, with a mean of 7.21 and median of 6.80. While the data is generally consistent, there are some longer leaves that increase the spread, as reflected in the standard deviation 2.75 and variance 7.57.  
- **All Plants**:  
  The data shows a wide range of leaf lengths due to the differences between plant species. The variance 41.01 and standard deviation 6.40 are much higher, reflecting the diversity in leaf length.

#### 4.2 Boxplots
Box plots summarize the distribution of leaf width and leaf length for all plants and each species. They show the spread of the data, the middle range, and any unusual values.

**Leaf Width:** <br>
- **Zamioculcas zamiifolia**:  
  The box is narrow, showing that leaf widths are very consistent. The median is 3.15, close to the mean 3.10, and the data has a small range.  
- **Snake Plant**:  
  The boxplot shows a tight distribution near 6 cm, with the median slightly above the mean, 6.20 compared to 6.04.  
- **Bunny Ears Cactus**:  
  The box is wider, indicating greater variation in leaf widths. Some very wide leaves extend the range. The median is 3.20, smaller than the mean 3.85, showing that larger values affect the average.  
- **All Plants**:  
  The overall boxplot reflects the combined data of all plants, showing that the spread is larger due to the differences between species.

**Leaf Length:** <br>
- **Zamioculcas zamiifolia**:  
  The box is narrow, and the data is centered around the median 7.50, indicating that most leaf lengths are very similar.  
- **Snake Plant**:  
  The box is much wider, showing a greater range of leaf lengths. Some particularly long leaves extend the range.  
- **Bunny Ears Cactus**:  
  The box is moderate in width, with most values between 6 and 8 cm.  
- **All Plants**:  
  The combined boxplot shows the wide range of leaf lengths across all plants, with notable differences between species.


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





