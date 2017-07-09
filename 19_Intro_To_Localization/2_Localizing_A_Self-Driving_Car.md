# Localizing A Self-Driving Car

Assume there is a car that is lost. Also assume that you have a global map of the environment. This map shows the environment around an office building in San Diego. Now localization answers a question: where is our car in a given map with high accuracy? High accuracy means between three and ten centimeters of precision.

In a traditional way, we use global navigation satellite systems to find the car with respect to the map. However, GPS is not precise enough. Most of the time GPS has an accuracy of the width of a lane - about one to three meters. Sometimes it can even be as broad as 1- to 50 meters. This is not reliable enough for a self-driving car.

We can use the onboard sensor data (From lidars and radars) along with out global map to solve the localization issue. With the onboard sensors it is possible to measure distances to static obstacles, like trees, poles, of walls. We measure these distances and the bearing of these static objects in the local coordinate system of our car.

When we are lucky, the same obstacles that were observed by the onboard sensors are also part of the map. The map has its own global coordinate system. To estimate where the car is in the map we have to match the observations with the map information. When this is done correctly, this results in a transformation between both coordinate systems - the local car coordinate system and the global coordinate system of the map. This transformation should be as accurate as possible - a range of 10 centimeters of less.

If we are able to estimate this transformation we can solve the localization issue

##### Localization answers the question: Where is our car in a given map with an accuracy of 10cm or less? Onboard sensors are used to estimate transformation between measurements and a given map.
