from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.regularizers import l1, l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping 
# import visualkeras 
# from PIL import ImageFont

def build_model(input_dim, encoding_dim=8, activation_type='relu', include_dropout=False, dropout_rate=0.5): 
	input_layer = Input(shape=(input_dim,))
	encoder = Dense(64, activation=activation_type)(input_layer)

	if include_dropout: 
		encoder = Dropout(0.5)(encoder)

	encoder = Dense(32, activation="relu")(encoder)
	encoder = Dense(encoding_dim, activation=activation_type)(encoder)  # Bottleneck layer

	# Decoder
	decoder = Dense(32, activation=activation_type)(encoder)
	decoder = Dense(64, activation=activation_type)(decoder)
	decoder = Dense(input_dim, activation='sigmoid')(decoder)


	autoencoder = Model(inputs=input_layer, outputs=decoder)
	return autoencoder 


def train_model(model, train, val, learning_rate=0.01, epochs=20, batch_size=256, shuffle=True):
	# Create and compile the model with the specified learning rate
	optimizer = Adam(learning_rate=learning_rate)

	model.compile(optimizer=optimizer, loss='mean_squared_error')

    # Initialize EarlyStopping callback
	early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1, mode='min', restore_best_weights=True)

	history = model.fit(train, train,
	                epochs=epochs,
	                batch_size=batch_size,
	                shuffle=shuffle,
	                validation_data=(val, val), 
	                callbacks=[early_stopping])

	return history 

def print_model(model):
	stringlist = []
	model.summary(print_fn=lambda x: stringlist.append(x))
	short_model_summary = "\n".join(stringlist)
	print(short_model_summary)

# def visualise_model(model): 
# 	font = ImageFont.load_default()  # using comic sans is strictly prohibited!
# 	visualkeras.layered_view(model, legend=True, font=font, to_file='../reports/figures/model.png') # write to disk
