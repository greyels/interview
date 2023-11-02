### Usage
python main.py <magnitude_threshold>

### Data model for MongoDB:

{
   "_id": ObjectId,
   "type": "FeatureCollection",
   "features": [
      {
         "type": "Feature",
         "geometry": {
            "type": "Point",
            "coordinates": [longitude, latitude]
         },
         "properties": {
            "name": "Location Name",
            "description": "Description of the location",
            "category": "Category of the location",
            "magnitude": 5.2,
            "timestamp": ISODate("2023-10-22T10:30:00Z"),
            "other_properties": "Other valuable attributes"
         }
      },
      // More Feature objects representing other locations
   ]
}
