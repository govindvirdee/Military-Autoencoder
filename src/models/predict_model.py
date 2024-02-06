import numpy as np 
from tensorflow.keras.models import Model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt

def predict_model(model, threshold, test, labels):
	X_test_pred = model.predict(test)
	reconstruction_error = np.mean(np.power(test - X_test_pred, 2), axis=1)

	# Define a threshold and predict anomalies
	y_pred = [1 if e > threshold else 0 for e in reconstruction_error]

	#Calculate accuracy
	accuracy = accuracy_score(labels, y_pred)
	print(f"Accuracy: {accuracy}")

	# Calculate precision, recall, and F1-score
	precision = precision_score(labels, y_pred)
	recall = recall_score(labels, y_pred)
	f1 = f1_score(labels, y_pred)

	print(f"Precision: {precision}")
	print(f"Recall: {recall}")
	print(f"F1 Score: {f1}")

	# Optionally, print confusion matrix
	print("Confusion Matrix:")
	print(confusion_matrix(labels, y_pred))

	return reconstruction_error, y_pred

def threshold_scan(reconstruction_error, labels):
	# Define a range of thresholds
	thresholds = np.linspace(0, 1, 100)

	# Initialize lists to store metrics
	accuracies = []
	precisions = []
	recalls = []
	f1_scores = []
	false_negatives = []
	false_positives = []

	for threshold in thresholds:
	    prediction = [1 if e > threshold else 0 for e in reconstruction_error]
	    
	    accuracies.append(accuracy_score(labels, prediction))
	    precisions.append(precision_score(labels, prediction))
	    recalls.append(recall_score(labels, prediction))
	    f1_scores.append(f1_score(labels, prediction))
	    
	    # Calculate confusion matrix and extract false negatives (FN)
	    tn, fp, fn, tp = confusion_matrix(labels, prediction).ravel()
	    false_negatives.append(fn)
	    false_positives.append(fp)

	plt.figure(figsize=(12, 8))

	# Create a plot with a primary and secondary y-axis
	fig, ax1 = plt.subplots()
	#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

	# Plotting the metrics on the primary y-axis
	accuracy_line, = ax1.plot(thresholds, accuracies, label='Accuracy', color='g')
	precision_line, = ax1.plot(thresholds, precisions, label='Precision', color='b')
	recall_line, = ax1.plot(thresholds, recalls, label='Recall', color='r')
	f1_score_line, = ax1.plot(thresholds, f1_scores, label='F1 Score', color='c')

	# Plot False Negatives on the secondary y-axis
	#false_negatives_line, = ax2.plot(thresholds, false_negatives, label='False Negatives', color='y')
	#false_positives_line, = ax2.plot(thresholds, false_positives, label='False Positives', color='m')

	# Labels and titles
	ax1.set_xlabel('Threshold')
	ax1.set_ylabel('Metrics')
	#ax2.set_ylabel('False Negatives', color='y')
	#ax2.set_ylabel('False Positives', color='m')

	# Collecting handles and labels for both axes
	handles = [accuracy_line, precision_line, recall_line, f1_score_line]
	labels = [h.get_label() for h in handles]

	# Creating a single legend for both lines
	fig.legend(handles, labels, loc='lower right', bbox_to_anchor=(0.9, 0.11))

	plt.title('Model Performance Across Different Thresholds')
	plt.savefig("../reports/figures/threshold_scan.png")
	print("Plot saved to reports/figures/threshold_scan.png")

def plot_losses(history):
	# Plot training & validation loss values
	plt.figure(figsize=(8, 6))
	plt.plot(history.history['loss'], label='Train Loss')
	plt.plot(history.history['val_loss'], label='Validation Loss')
	plt.title('Model Loss Over Epochs')
	plt.ylabel('Loss')
	plt.xlabel('Epoch')
	plt.legend(loc='upper right')
	plt.savefig("../reports/figures/losses.png")
	print("Plot saved to reports/figures/losses.png")

def plot_reco_error(reconstruction_error, labels):
	plt.figure(figsize=(10, 6))
	plt.scatter(range(len(reconstruction_error)), reconstruction_error, c=labels, cmap='coolwarm', label=['Normal', 'Anomaly'], alpha=0.7, s=2)
	plt.colorbar()
	plt.xlabel('Data Point Index')
	plt.ylabel('Reconstruction Error')
	plt.title('Reconstruction Error of Each Data Point')
	plt.savefig("../reports/figures/reco_error.png")
	print("Plot saved to reports/figures/reco_error.png")




