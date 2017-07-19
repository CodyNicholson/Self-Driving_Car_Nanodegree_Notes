# Localization Vs Sensor Fusion

| Localization  | Sensor Fusion | 
|:------------- |:-------------:|
| Things are in vehicle coordinates OR map coordinates. The entire objective of localization is to find the transformation between vehicle coordinates and map coordinates. In other words, we’re trying to find the position of the car in the map! | Everything is in vehicle coordinates where the x axis points in the direction of the car’s heading and the y axis points to the left of the car. |
| The position of the car is described in map coordinates. | The car is always assumed to be at the origin of the vehicle coordinate system. |
| The sensor measurements are usually described in vehicle coordinates. Vehicle coordinates have the x-axis in the direction of the car’s heading, the y-axis pointing orthogonal to the left of the car, and the z-axis pointing upwards. | Sensor measurements are in vehicle coordinates. |
| Map landmarks are in map coordinates.  | There’s no map involved! |
