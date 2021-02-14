									Sentimental Analysis Using LSTM
									¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
Date : 08-02-2021															Author : unKNOWN-G

In this project I aim to perform a basic Multi Class Sentimental Analysis using LSTM. The reviews can be good, bad and average
In sentimental analysis we basically classify the reviews into multi classes

Language Used : Python


  Update Count	   Date							Description
  ¯¯¯¯¯¯¯¯¯¯¯¯	   ¯¯¯¯							¯¯¯¯¯¯¯¯¯¯¯

	1	11-01-2021		A basic file containing preprocessing stages of the text file is prepared
	2	12-01-2021		The Dataset requires Larger computation. Shifting to Colab
	3	13-01-2021		The previous dataset is huge and rquires high compitation which we dont have right currently. Shifting to Small size tweet dataset and did setup an architecture in Colab
					The code is working but the Neural net isnt learning anything. The Validation accuracy is at constant level.
	4	15-01-2021		Found the mistake. It was a mistake in One-Hot Encoding. Hence the network wasnt able to learn anything. Now its working fine
					Formatted the Colab Notebook	
					Wrote in python file too
	
 
Advancements that can be made
1) The present Accuracy can be improved very much by using enhanced preprocessing stages and Using proper LSTM architecture
2) The Architecture can be implemented with Different Classifiers like Bidirectional LSTM, Naive Bias Classifier and 1D Convolution Neural Network
3) Graphs can be plotted to see the training of the model, Model saving techniques can be explored, Loading model
