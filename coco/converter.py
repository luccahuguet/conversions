from pylabel import importer

# Specify path to the coco.json file
path_to_annotations = "coco/annotations/instances_train.json"
# Specify the path to the imgs (if they are in a different folder
path_to_images = "coco/train/"

# Import the dataset into the pylable schema
dataset = importer.ImportCoco(
    path_to_annotations, path_to_images=path_to_images, name="coco_cool"
)
dataset.df.head(5)
