class Config:

    # INPUT
    # Update this to the folder containing your multiple ortho images
    ORTHO_PATH = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/examples/s4_tree.tif"  # <-- new path
    WORKDIR = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/output"

    # DETECTREE
    DETECTREE_MODEL = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/urban_trees_Cambridge_20230630.pth"
    

    TILE_SIZE = 40
    BUFFER = 5
    IOU_THRESHOLD = 0.5
    CONF_THRESHOLD = 0.35


    # FEATURES + CLUSTERING
    STEP1_OUTPUT = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/output/step1_output"

    MODEL_NAME = "vit_base_patch14_dinov2.lvd142m"
    IMG_SIZE = 224
    BATCH_SIZE = 16
    PCA_COMPONENTS = 50

    K_LIST = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    COPY_TO_CLUSTER_FOLDERS = True

    # SPECIES
    CHOSEN_K = 4
    STEP2_OUTPUT = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/output/step2_output"


    # VALIDATION
    GROUND_TRUTH_CSV = "/Users/Shared/Files From d.localized/Guide_IITD/data_set_sanjayvan/Data/sanjay_van/Sanjay_Van_Drone/spot1_8_10/final key/all/8_10_s123ortho/ortho/automated_tree_species_classification_drone_to_google_earth/labels"
    STEP3_VALIDATION_OUTPUT = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/output/step3_output"


    # KMZ
    STEP4_OUTPUT = "/home/anunay/automated_tree_species_classification_drone_to_google_earth/output/step4_output"
    SOURCE_EPSG = 32643

    COLOR_PALETTE = [
        "990000ff",
        "9900ff00",
        "99ff0000",
        "9900ffff",
        "99ff00ff",
        "99ff8800",
        "9900ffff",
        "99ffffff",
    ]
