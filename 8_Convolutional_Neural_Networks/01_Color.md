# Color

Structure helps learning

If your data has some structure, and your network doesn't have to learn that structure from scratch, it's going to perform better

Example: You are trying to classify letters, and you know that color is really not a factor in what makes an "A" an "A". 

If color doesn't matter, it might help to reduce the complexity of the problem by combining color channels into a single monochromatic channel (grayscale)

Taking the average (R+G+B)/3  is one way of doing it; however there are other transformations that might be more effective/closer to how human's perceive color (e.g. converting to YUV and using the Y channel)
