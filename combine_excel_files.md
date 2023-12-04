# useful_research_tools/combine_excel_rows
### by: [Allyson Pfeil](https://github.com/allysonpfeil)

Sometimes, our data is not as clean and intuitive as we might hope for. One common problem I experience in medical research is that medical intervention is often indicated by multiple diagnosis codes. For instance, a surgical patient might have diabetes, arthritis, and osteoporosis. All of these conditions together necessitate surgery for the patient. 

_Note: I am describing the instance to which this code most directly serves me, but it can have other purposes and applications as well._

Storing this data becomes complicated. In the database, the patient's surgery instance is associated with multiple diagnoses as I previously mentioned. This means that a database query will pull several duplicate surgical instances to accompany the patient's diagnoses. This is unfavorable, but also, each diagnosis that leads the patient to surgery is important. Thus, the program exists to combine the diagnoses based on the patient's identification number into one column. From there, Excel's "_Text to column_" feature can handle the rest. 

## Code Overview:
The code is somewhat straightforward; however, someone unfamiliar to Python syntax may have some minor comprehension issues. In general, this code:
1. Defines a function called `combine_values`
2. Uses column A data to find matches
3. Combines column AE data based on exact column A matches
4. Prints the data

### Using the Code:
1. Install the necessary library:
   ```
   pip install openpyxl
   ```
3. Replace `"your/path/here"` with the path to the excel file with the data. Do not define the path anywhere else. Data must start on row 2, with an assumed header in row 1. Otherwise, replace `min_row=2` with `min_row=1`
4. Determine which columns (and indexes) are the lookup value and the match value. For this example, column A [Index 0] is the lookup value, and column AE [Index 30] is the match value. Your data might look different, so adjust accordingly. 

That's it! Like most programming and data problems, the setup is the hardest part. I would provide a debugging section, but I truly cannot think of a reason the code wouldn't work if you follow the directions. It is a very simple program. However, please contact me if you do find error or issues. 
