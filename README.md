# Forest-tree-crown-species-classification-geo-AI

Automated **tree species mapping from high-resolution drone orthomosaics** using **Deep learning foundation models** and translation of species labels to Google Earth for geospatial investigation. 
<img width="613" height="924" alt="overview" src="https://github.com/user-attachments/assets/50f3d498-87e5-43a4-8203-2ddc937955ab" />


This repository provides an automated pipeline aimed at classifying multiple forest tree species using drone data.

The pipeline supports any type of drone georeferenced orthomosaic with a .tif extension. In our application, we identified tree species as either Acacia or Non-Acacia in the tropical forest using dense crown investigation.

Only one inputs are required (georeferenced Drone RGB Orthomosaic) pipeline automatically processes orthomosaic images, extracts tree crowns, predicts species classes, and generates Google Earth compatible KML maps showing tree species distribution across forest landscapes

The framework integrates **computer vision, geospatial processing, and deep learning** to generate spatial outputs that can be visualized directly in **QGIS or Google Earth**.

Automated tree species mapping from high-resolution drone orthomosaics using deep learning foundation models and geospatial processing. The pipeline generates species distribution maps that can be visualized in Google Earth.

---
This repository provides an end-to-end pipeline that:

* Takes a single orthomosaic as input
* Automatically detects tree crowns
* Extracts features and clusters crowns
* Assigns species labels (human-in-the-loop)
* Exports results as KMZ for geospatial analysis


---
# Self-Developed Dataset from our case study

<img width="2892" height="1620" alt="image" src="https://github.com/user-attachments/assets/0db75e45-bdaa-409a-b65c-a5866e4dcb83" />


The biodiversity study carried out in Sanjay Van, a semi-arid urban forest situated in the southern ridge of New Delhi. This forest is part of the Aravalli hill system and is noted for its dry deciduous vegetation, scrubland, and areas of dense canopy mixed with open spaces. The region has a semi-arid climate marked by significant seasonal changes, making it ideal for ecological monitoring concerning vegetation structure and biodiversity trends.

Drone orthomosaic images were collected from four survey locations. Raw drone images were processed using WebODM to generate georeferenced orthomosaics and derived products. These orthomosaics served as the primary input for the end-to-end pipeline.

Site Number of Crowns

S1-656

S2-717

S3-628

S4-155

Total tree crowns extracted: 2156 crowns

Manual species labeling was performed for: 400 crowns (requirements for validation the predicted data)

ClassCount

Acacia= 193

Non-Acacia= 207

---

# Pipeline Overview

---

Orthomosaic imagery is processed through the following workflow:

* 0 - Tree crown detection using Detectree2
* 1 - Tree crown cropping from orthomosaic images
* 2 - Deep feature extraction using DINOv2 Vision Transformer
* 3 - Feature clustering and evaluation
* 4 - Assigning the cluster labels of tree species (human-in-the-loop)
* 5 - Automated prediction of species for all crowns
* 6 - Export of labeled polygons to GeoJSON and KMZ
* 7 - Final output: species distribution map in Google Earth

---

# Inputs

The pipeline requires a single input:

* Drone Orthomosaic (GeoTIFF)

The pipeline automatically detects tree crowns and generates crown polygons internally.

---

# Pipeline Steps

## Step 0: Tree Crown Detection (Detectree2)

* Detects individual tree crowns from orthomosaic imagery
* Uses a pretrained Detectree2 model
* Generates crown polygons automatically

Output:

* tree_crowns.geojson
* overlay.png

---

## Step 1A: Crown Cropping

* Crops each detected crown from the orthomosaic
* Produces individual crown images

---

## Step 1B: Feature Extraction (DINOv2)

* Extracts feature vectors using DINOv2 (ViT backbone)
* Features are normalized and optionally reduced using PCA

---

## Step 1C: Multi-k Clustering

* Applies K-Means clustering with multiple k values
* Helps identify natural groupings of tree crowns

---

## Step 1D: K Selection

* Uses:

  * Silhouette Score
  * Davies-Bouldin Index
  * Elbow Method

* Select optimal k

---

## Step 1E: t-SNE Visualization

* Visualizes clusters in 2D
* Helps manual inspection

---

## Manual Step (Human-in-the-loop)

* Inspect cluster folders
* Assign species labels

Edit:

```
step1_output/clustering/k{chosen_k}_cluster_species_map.csv
```

---

## Step 2: Species Assignment

* Applies species labels to all crowns
* Generates:

  * crown_master.csv
  * polygon_species.csv

---

## Step 3: Validation (Optional)

* Compares predictions with ground truth
* Generates metrics and confusion matrix

---

## Step 4: KMZ Export

* Exports results to Google Earth

Final Output:

```
species_map.kmz
```
---

#Repository files


---

# Installation

## clone the repo
```bash
git clone https://github.com/jayakrishnascientist/automated_tree_species_classification_drone_to_google_earth.git
```
---
folder structure 
```
tree-crown-pipeline/
│
├── examples/
│   ├── S3C.tif                # Sample orthomosaic input
│   └── s3_tree.geojson       # Sample tree crown annotations
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── config.py                 # Configuration settings
├── end_to_end_pipeline.py    # Full pipeline execution script
├── tree_crown_pipeline.py    # Core pipeline logic
├── predict.py                # Prediction script (model inference)

```
---
edit config.py file only and run end_to_end_pipeline.py only (make all files in single folder)
---

## Step 1: Create Environment (MAC/LINUX)

```bash
rm -rf venv
python3.10 -m venv venv
source venv/bin/activate
```

---

## : Step 1: Create Environment (Windows powershell)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

## Step 2: Upgrade Tools

```bash
pip install --upgrade pip setuptools wheel
```

---

## Step 3: Install PyTorch

```bash
pip install torch torchvision torchaudio
```

Verify:

```bash
python -c "import torch; print(torch.__version__)"
```

---

## Step 4: Install Detectron2

```bash
pip install --no-build-isolation 'git+https://github.com/facebookresearch/detectron2.git@v0.6'
```

---

## Step 5: Install Detectree2

```bash
pip install detectree2
```

---

## Step 6: Install Remaining Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 7: Fix Pillow Compatibility

```bash
pip install Pillow==9.5.0
```

---

# Configuration

Edit `config.py`:

```python
ORTHO_PATH = "/path/to/orthomosaic.tif"
DETECTREE_MODEL = "/path/to/model.pth"
CHOSEN_K = 6
```

---

# Running the Pipeline

## Step 0: Crown Detection

```bash
python end_to_end_pipeline.py --step 0
```

---

## Step 1: Clustering

```bash
python end_to_end_pipeline.py --step 1
```

After this:

1. Open:

```
project_output/step1_output/clustering/
```

2. Choose best k

3. Edit:

```
k{chosen_k}_cluster_species_map.csv
```

4. Update:

```
CHOSEN_K in config.py
```

---

## Step 2: Species Assignment

```bash
python end_to_end_pipeline.py --step 2
```

---

## Step 3: Validation (Optional)

```bash
python end_to_end_pipeline.py --step 3
```

---

## Step 4: KMZ Export

```bash
python end_to_end_pipeline.py --step 4
```

Final output:

```
species_map.kmz
```

---

# Output Structure

```
project_output/
├── detectree/
├── step1_output/
├── step2_output/
└── step4_output/
```

---

# Troubleshooting

## Detectron2 Pillow Error

```
AttributeError: Image.LINEAR
```

Fix:

```bash
pip install Pillow==9.5.0
```

---

## No tiles generated

* Check orthomosaic validity
* Reduce nan_threshold

---

## Poor crown predictions

* Adjust confidence threshold
* Improve model weights

---

# Summary

This pipeline automates tree crown detection, clustering, and species mapping from drone imagery, providing geospatial outputs for visualization in Google Earth. 

Our analysis of clustered crowns revealed significant variation in canopy composition across four monitoring spots. Certain areas exhibited more Acacia-classified crowns, while others showed a diverse presence of Non-Acacia species, aligning with field observations. Spot-wise analysis indicated species composition variability: Spot S1 had 656 trees (169 Acacia, 487 non-Acacia), highlighting non-Acacia dominance. Spot S2 included 717 trees (277 Acacia, 440 non-Acacia), also dominated by non-Acacia. In Spot S3, 628 trees were observed (325 Acacia, 303 non-Acacia), showing slight Acacia dominance. Spot S4 had 178 trees (114 Acacia, 64 non-Acacia), indicating clear Acacia dominance. Overall, a transition from non-Acacia dominance in S1 and S2 to Acacia dominance in S3 and S4 illustrates spatial heterogeneity in species distribution.

Link: https://earth.google.com/earth/d/1vleAAaXRyX-5CcqPvqja8ZGZ0DBPTBvz?usp=sharing 

