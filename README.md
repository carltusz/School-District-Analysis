# school-district-analysis
Analytics Bootcamp Module 4

## Overview
School districts were analysed to understand the association between school type, size and spending, and student performance at different grade levels. The grades submitted for Grade 9 students at Thomas High School were suspected to be invalid. A secondary analysis was completed excluding the grade 9 scores from Thomas High School to determine the impact of including the potentially erroneous data on the district summary, school summary, and how the math and reading scores change by grade, and school size, spending and type.

## Results
### - Impact to District Summary

As shown below, 461 grade 9 students were excluded from Thomas High School.

![](Resources/excluded-student-count.png)

Removing the Grade 9 students from Thomas High School did not make a significant impact to the overall district grade performance. Exclusion of the students lead to a 0.1% drop on the Average Math Score,and no change to the average reading score. 0.2% less students were found to pass math, and 0.1% less students were found to be passing reading. 0.3% less students were found to be passing both courses.



![](Resources\district-summary-original.png)

![](Resources\district-summary-updated.png)

### - Impact to School Summary

The changed results makes no difference to the school summary, with the exception of Thomas High School's performance. This is covered in the next section.

### - Impact to Thomas High School Performance

Excluding the grade nine students made a much more significant impact on the metrics out of Thomas High School than the entire district. When all records are included, Thomas High had a pass rate of 66.9% and 69.7% for math and reading, respectively. 65.1% of students were found to be passing both math and reading. Exclusion of the grade nine results concluded in pass rates of 93.2% and 97.0% for math and reading, respectively; and 90.6% for students passing both math and reading.

Original data set:
![](Resources\school-summary-original.png)

Excluding Thomas High School Grade 9:
![](Resources\school-summary-updated.png)

### - Impact to Scores by Grade

Excluding the grade nine students from Thomas High does not impact the remaining analysis by grade and school, with the obvious exception of the grade nine scores which were excluded from Thomas High. Examples are shown below with the reading scores.

Original data set:

![](Resources\reading-scores-school-grade-original.png)

Excluding Thomas High School Grade 9:

![](Resources\reading-scores-school-grade-updated.png)

### - Impact to Scores by School Spending

Inclusion or exclusion of the grade nine scores makes very little difference to student scores when considered by school spending. The % Passing Reading and % Overall Passing were reduced from 84.4% to 84.3% and 62.9% to 62.8%, respectively, when the Thomas High grade nine student scores were removed.

Original data set:
![](Resources\scores-by-spending-original.png)

Excluding Thomas High School Grade 9:
![](Resources\scores-by-spending-updated.png)

### - Impact to Scores by School Size

The exclusion of the Thomas High grade 9 students made virtually no impact to student scores when analyzed by school size.

Original data set:
![](Resources\school-size-original.png)
Excluding Thomas High School Grade 9:
![](Resources\school-size-updated.png)

### - Impact to Scores by School Type

The exclusion of the Thomas High grade 9 students made virtually no impact to student scores when analyzed by school type.

Original data set:
![](Resources\school-type-original.png)

Excluding Thomas High School Grade 9:
![](Resources\school-type-updated.png)

## Summary

The district summary, school summary, and summaries by grade and school and by spending saw changes in passing rates and average scores when the grade nine scores from Thomas High School were excluded from the data set.

Other areas of analysis were not impacted because the number of records excluded was so small that the average values calculated on blarge populations were not impacted.
