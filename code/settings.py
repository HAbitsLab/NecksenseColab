import os
import pytz

settings = {}
settings["TIMEZONE"] = pytz.timezone("America/Chicago")
settings["ROOT_DIR"] = "/content/NecksenseColab/data"
#====================================================================================================
# SUBJECTS
#====================================================================================================

subjects = {
    "EXPLORATORY": ["P001", "P002", "P003", "P004", "P005","P006", "P007", "P008", "P009", "P010"],
    "FREELIVING": ["P101", "P102", "P103", "P104", "P105","P106", "P107", "P108", "P109", "P110"],
    "FREELIVING_OBESE": ["P101", "P102", "P106", "P109", "P110"],
    "FREELIVING_NONOBESE": ["P103", "P104", "P105", "P107", "P108"]
}
settings["SUBJECTS"] = subjects

#====================================================================================================
# DATETIME
#====================================================================================================
settings["CALENDAR_DAY_AMEND_HOURS"] = 5

#====================================================================================================
# DATA SPECIFICATION
#====================================================================================================
settings["SAMPLING_RATE"] = 20

#====================================================================================================
# DATETIME FORMAT
#====================================================================================================
settings["ABSOLUTE_TIME_FORMAT"] = "%Y-%m-%d %H:%M:%S.%f"
settings["RELATIVE_TIME_FORMAT"] = "%H:%M:%S.%f"

#====================================================================================================
# VALIDATION MODE
#====================================================================================================
settings["VALIDATION_MODE_PREFIX"] = "LOPO_modal_"

#====================================================================================================
# VALIDATION MODE
#====================================================================================================
settings["num_samples_in_FFT"] = 80
settings["window_start1_shift"] = 2
settings["window_start2_shift"] = 3
settings["window_end1_shift"] = 2
settings["window_end2_shift"] = 1

#====================================================================================================
# XGBOOST SETTINGS
#====================================================================================================
xgb_param = {}
xgb_param["seed"] = 123
xgb_param["objective"] = "multi:softmax"
xgb_param["lambda"] = 0.8
xgb_param["eta"] = 0.05
xgb_param["max_depth"] = 1
xgb_param["subsample"] = 0.8
xgb_param["min_child_weight"] = 5
xgb_param["silent"] = 0
xgb_param["num_class"] = 2
xgb_param["nthread"] = 32

settings["xgb_param"] = xgb_param
settings["xgb_training_num_boost_round"] = 1000
settings["xgb_training_early_stopping_rounds"] = 200
settings["xgb_training_maximize"] = False
settings["xgb_training_verbose_eval"] = False

#====================================================================================================
# SENSOR COMBINATION
#====================================================================================================
settings["mode_P_inclusions"] = ["proximity"]
settings["mode_PA_inclusions"] = ["proximity", "amb"]
settings["mode_PLE_inclusions"] = ["proximity", "lean", "energy"]

#====================================================================================================
# CLUSTERING
#====================================================================================================
settings["DBSCAN_PARAM_EPS_RANGE"] = list(range(20, 220, 20))
settings["DBSCAN_PARAM_MINPTS_RANGE"] = list(range(20, 220, 20))

#====================================================================================================
# EPISODE DEFINITION
#====================================================================================================
settings["episode_gap_threshold_minutes"] = 15
# episode evaluation overlap threshold, a prediction with overlap with groundtruth greater than which is a true positive
settings["overlap_threshold"] = 0.5
