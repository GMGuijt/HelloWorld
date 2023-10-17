import pandas as pd

prediction = pd.read_excel("week6/homework data/predictions_training.xlsx")
training = pd.read_excel("week6/homework data/training.xlsx")

training['opp'] = (training['max_r']-training['min_r'])*(training['max_c']-training['min_c'])
prediction['opp'] = (prediction['max_r']-prediction['min_r'])*(prediction['max_c']-prediction['min_c'])
merge = pd.merge(training,prediction, left_index=True, right_index=True)
merge['intercept'] = max(0,merge[['min_c_x','min_c_y']].min(axis=1) - merge[['max_c_x','max_c_y']].max(axis=1)) * max(0,merge[['min_r_x','min_r_y']].min(axis=1) - merge[['max_r_x','max_r_y']].min(axis = 1))
print(merge.head())
# IOU calculation algorithm
# 𝐼 = original image with dimensions (𝑟, 𝑐)
# 𝐴 = empty image (zeros matrix) with same dimensions as 𝐼
# 𝑇 = list of the true bounding boxes
# 𝑃 = list of the predicted bounding boxes
# Procedure:
# 1. For all 𝒕 in 𝑻:
# 2. Fill the region of 𝑡 with 𝐴𝑡 = 1
# 3. End
# 4. For all 𝒑 in 𝑷:
# 5. Add 2 to the region of 𝑝 with 𝐴𝑝 = 𝐴𝑝 +2
# 6. End
# 7. intersection = the number of pixels in 𝐴 with value equal to 3
# 8. union = the number of pixels in 𝐴 with value 1, 2, or 3
# Note: this is not the actual IOU algorithm but a simplified version. Normally, you would have to
# match a predicted box to an actual box. But we’ll ignore that for this exercise.
