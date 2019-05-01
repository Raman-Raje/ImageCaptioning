#inception input image size format
TARGET_SIZE = (299,299)

# code for image imbedding i.e converting image to 300 dimentional

train_image_extracted = dict()
with open("data/Flickr8k_text/Flickr_8k.trainImages.txt","r") as f:
    data = f.read()
    
try:
    for el in data.split("\n"):
        tokens = el.split(".")
        image_id = tokens[0]
        img = load_img("data/Flicker8k_Dataset/{}.jpg".format(image_id),target_size=TARGET_SIZE)
        # Converting image to array
        img_array = img_to_array(img)
        nimage = preprocess_input(img_array)
        # Adding one more dimesion
        nimage = np.expand_dims(nimage, axis=0)    
        fea_vec = final_model.predict(nimage)
        train_image_extracted[image_id] = np.reshape(fea_vec, fea_vec.shape[1]) # reshape from (1, 2048) to (2048, )


except Exception as e:
    print("Exception got :- \n",e)
	
# save the file 
dump(train_image_extracted,open("train_image_extracted.pkl","wb"))	