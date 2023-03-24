from pylabel import importer

# Specify path to the coco.json file
path_to_annotations = "coco/annotations/instances_val.json"
# Specify the path to the images
path_to_images = "coco/val/"

# Import the dataset into the pylable schema
dataset = importer.ImportCoco(
    path_to_annotations, path_to_images=path_to_images, name="coco_cool2"
)
dataset.df.head(5)
print(f"Number of images: {dataset.analyze.num_images}")
print(f"Number of classes: {dataset.analyze.num_classes}")
print(f"Classes:{dataset.analyze.classes}")
print(f"Class counts:\n{dataset.analyze.class_counts}")
print(f"Path to annotations:\n{dataset.path_to_annotations}")

dataset.path_to_annotations = "./yolo"
dataset.export.ExportToYoloV5()[0]
