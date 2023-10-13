import geopandas
import numpy as np

def IOU(box1, box2):

    x1, x2, y1, y2 = box1
    x3, x4, y3, y4 = box2
    x_inter1 = max(x1, x3)
    y_inter1 = max(y1, y3)
    x_inter2 = min(x2, x4)
    y_inter2 = min(y2, y4)
    width_inter = abs(x_inter2 - x_inter1)
    height_inter = abs(y_inter2 - y_inter1)
    area_inter = width_inter * height_inter
    width_box1 = abs(x2 - x1)
    height_box1 = abs(y2 - y1)
    width_box2 = abs(x4 - x3)
    height_box2 = abs(y4 - y3)
    area_box1 = width_box1 * height_box1
    area_box2 = width_box2 * height_box2
    area_union = area_box1 + area_box2 - area_inter
    iou = area_inter / area_union

    if iou > 0 and iou < 1:
        return iou
    else:
        return 0

def calculations(shp1, shp2):
    
    iou_values = [] #highest overlap ious

    for i in shp1:
        current_ious = [] #ious of i w.r.t each individual polygon in shp2
        for j in shp2:
            current_ious.append(IOU(i,j))
        print(current_ious)
        iou_values.append(max(current_ious)) #incase of multiple overlapping we need the closest measurements w.r.t overlaps

    return np.mean(iou_values)


if __name__ == '__main__':
    
    shivam_shp = geopandas.read_file('./test/DJI_20220712133408_0902.geojson') #read shp or geojson
    polygons = [i.exterior.coords.xy for i in shivam_shp['geometry']] #get the xy coordinates in each polygon
    shivam_annotations = [[max(i[0]), min(i[0]),max(i[1]), min(i[1])] for i in polygons] #get the max and min x y values of the boxes

    rudraksh_shp = geopandas.read_file('./examples/single/gis2img_test.shp') #read shp or geojson
    polygons = [i.exterior.coords.xy for i in rudraksh_shp['geometry']] #get the xy coordinates in each polygon
    rudraksh_annotations = [[max(i[0]), min(i[0]),max(i[1]), min(i[1])] for i in polygons] #get the max and min x y values of the boxes

    # Testing:
    # shivam_annotations = [[-1,-10,5,10],[-20,-25,10,22]]
    # rudraksh_annotations = [[-2,-6,4,8],[-19,-22,12,18]]
    
    iou = calculations(shivam_annotations, rudraksh_annotations)
    
    print(iou)
    
    