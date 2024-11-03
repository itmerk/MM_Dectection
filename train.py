from mmcv import Config

# Load the config file for a Faster R-CNN model (or any other model of choice)
config_path = 'D:/data science/projects/my projects/MM Dect/mmdetection/fast-rcnn_r50_fpn_1x_coco.py'
cfg = Config.fromfile(config_path)

# Update config for the Aquarium Dataset
cfg.dataset_type = 'CocoDataset'
cfg.data_root = 'D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset'
cfg.data.train.ann_file = "D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/train/annotations/train_annotations.json"
cfg.data.train.img_prefix = 'D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/train/image'
cfg.data.val.ann_file = 'D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/valid/annotations/val_annotations.json'
cfg.data.val.img_prefix = 'D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/valid/image'
cfg.data.test.ann_file = 'D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/test/annotations/test_annotations.json'
cfg.data.test.img_prefix = 'D:/data science/projects/my projects/MM Dect/mmdetection/Aquarium-Dataset/test/image'

# Update model-specific parameters
cfg.model.roi_head.bbox_head.num_classes = 10  # Update NUM_CLASSES based on your dataset
cfg.load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco.pth'  # Path to pre-trained weights
cfg.work_dir = './work_dirs/aquarium_faster_rcnn'
cfg.lr_config.warmup = None
cfg.log_config.interval = 10
cfg.evaluation.metric = 'bbox'

# Save updated config
cfg.dump('D:/data science/projects/my projects/MM Dect/mmdetection/configs/custom_aquarium_faster_rcnn.py')
print(cfg.pretty_text)
