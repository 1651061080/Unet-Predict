{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\SoftWare\\Anaconda2\\envs\\python3\\lib\\site-packages\\h5py\\__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.\n",
      "  from ._conv import register_converters as _register_converters\n",
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "from model import *\n",
    "from data import *"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Train your Unet with membrane data\n",
    "membrane data is in folder membrane/, it is a binary classification task.\n",
    "\n",
    "The input shape of image and mask are the same :(batch_size,rows,cols,channel = 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Train with data generator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:34: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge6 = merge([drop4,up6], mode = 'concat', concat_axis = 3)\n",
      "C:\\SoftWare\\Anaconda2\\envs\\python3\\lib\\site-packages\\keras\\legacy\\layers.py:465: UserWarning: The `Merge` layer is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  name=name)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:39: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge7 = merge([conv3,up7], mode = 'concat', concat_axis = 3)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:44: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge8 = merge([conv2,up8], mode = 'concat', concat_axis = 3)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:49: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge9 = merge([conv1,up9], mode = 'concat', concat_axis = 3)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:55: UserWarning: Update your `Model` call to the Keras 2 API: `Model(inputs=Tensor(\"in..., outputs=Tensor(\"co...)`\n",
      "  model = Model(input = inputs, output = conv10)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/5\n",
      "Found 34 images belonging to 1 classes.\n",
      "Found 34 images belonging to 1 classes.\n",
      "2000/2000 [==============================] - 538s 269ms/step - loss: 0.1951 - acc: 0.9140\n",
      "\n",
      "Epoch 00001: loss improved from inf to 0.19511, saving model to unet_membrane.hdf5\n",
      "Epoch 2/5\n",
      "2000/2000 [==============================] - 535s 268ms/step - loss: 0.1210 - acc: 0.9469\n",
      "\n",
      "Epoch 00002: loss improved from 0.19511 to 0.12099, saving model to unet_membrane.hdf5\n",
      "Epoch 3/5\n",
      "2000/2000 [==============================] - 534s 267ms/step - loss: 0.0926 - acc: 0.9596\n",
      "\n",
      "Epoch 00003: loss improved from 0.12099 to 0.09256, saving model to unet_membrane.hdf5\n",
      "Epoch 4/5\n",
      "2000/2000 [==============================] - 534s 267ms/step - loss: 0.0788 - acc: 0.9656\n",
      "\n",
      "Epoch 00004: loss improved from 0.09256 to 0.07882, saving model to unet_membrane.hdf5\n",
      "Epoch 5/5\n",
      "2000/2000 [==============================] - 534s 267ms/step - loss: 0.0707 - acc: 0.9691\n",
      "\n",
      "Epoch 00005: loss improved from 0.07882 to 0.07074, saving model to unet_membrane.hdf5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.History at 0x1e22c6d9898>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_gen_args = dict(rotation_range=0.2,\n",
    "                    width_shift_range=0.05,\n",
    "                    height_shift_range=0.05,\n",
    "                    shear_range=0.05,\n",
    "                    zoom_range=0.05,\n",
    "                    horizontal_flip=True,\n",
    "                    fill_mode='nearest')\n",
    "myGene = trainGenerator(2,'data/membrane/train','image','label',data_gen_args,save_to_dir = None)\n",
    "model = unet()\n",
    "model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)\n",
    "model.fit_generator(myGene,steps_per_epoch=2000,epochs=5,callbacks=[model_checkpoint])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Train with npy file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#imgs_train,imgs_mask_train = geneTrainNpy(\"data/membrane/train/aug/\",\"data/membrane/train/aug/\")\n",
    "#model.fit(imgs_train, imgs_mask_train, batch_size=2, nb_epoch=10, verbose=1,validation_split=0.2, shuffle=True, callbacks=[model_checkpoint])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### test your model and save predicted results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:34: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge6 = merge([drop4,up6], mode = 'concat', concat_axis = 3)\n",
      "C:\\SoftWare\\Anaconda2\\envs\\python3\\lib\\site-packages\\keras\\legacy\\layers.py:465: UserWarning: The `Merge` layer is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  name=name)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:39: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge7 = merge([conv3,up7], mode = 'concat', concat_axis = 3)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:44: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge8 = merge([conv2,up8], mode = 'concat', concat_axis = 3)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:49: UserWarning: The `merge` function is deprecated and will be removed after 08/2017. Use instead layers from `keras.layers.merge`, e.g. `add`, `concatenate`, etc.\n",
      "  merge9 = merge([conv1,up9], mode = 'concat', concat_axis = 3)\n",
      "C:\\Users\\xuhaozhi\\Documents\\Study\\unet\\model.py:55: UserWarning: Update your `Model` call to the Keras 2 API: `Model(inputs=Tensor(\"in..., outputs=Tensor(\"co...)`\n",
      "  model = Model(input = inputs, output = conv10)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\SoftWare\\Anaconda2\\envs\\python3\\lib\\site-packages\\skimage\\transform\\_warps.py:105: UserWarning: The default mode, 'constant', will be changed to 'reflect' in skimage 0.15.\n",
      "  warn(\"The default mode, 'constant', will be changed to 'reflect' in \"\n",
      "C:\\SoftWare\\Anaconda2\\envs\\python3\\lib\\site-packages\\skimage\\transform\\_warps.py:110: UserWarning: Anti-aliasing will be enabled by default in skimage 0.15 to avoid aliasing artifacts when down-sampling images.\n",
      "  warn(\"Anti-aliasing will be enabled by default in skimage 0.15 to \"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30/30 [==============================] - 1s 47ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\SoftWare\\Anaconda2\\envs\\python3\\lib\\site-packages\\skimage\\util\\dtype.py:130: UserWarning: Possible precision loss when converting from float32 to uint16\n",
      "  .format(dtypeobj_in, dtypeobj_out))\n"
     ]
    }
   ],
   "source": [
    "testGene = testGenerator(\"data/membrane/test\")\n",
    "model = unet()\n",
    "model.load_weights(\"unet_membrane.hdf5\")\n",
    "results = model.predict_generator(testGene,30,verbose=1)\n",
    "saveResult(\"data/membrane/test\",results)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
