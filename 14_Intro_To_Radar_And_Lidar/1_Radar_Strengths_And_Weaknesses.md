# Radar Strengths & Weaknesses

Radar sensors have been in the auto industry for years. You can find them in systems like adaptive cruise control, blind spot warning, and collision avoidance. 

Even though radar is a mature technology, it still gets improved all the time to make it even more powerful.

While other sensors measure velocity by calculating the difference between two readings, radar uses something called the **Doppler effect** to measure speed directly. The Doppler effect measures the change in frequency of the radar waves based on whether the object is moving away from you or toward you. Think about how a fire engine siren sounds differently if it is coming toward you vs going away from you.

The Doppler effect is important for sensor fusion because it gives us the velocity as an independent measure parameter, and makes the fusion algorithms converge much faster

Radar can also be used for localization by generating radar maps of the environment. Since radar waves bounce off hard surfaces, they can provide measurements to objects without direct line of sight. Radar can see underneath other vehicles, and spot buildings and objects that would otherwise be obscured. Of all of the sensors on the car, radar is the least affected by rain or fog and can have a wide field of view (about 150 degrees) or a long range of about 200 plus meters. 

Compared to lidars and cameras, radars have a low resolution, especially in the vertical direction where the resolution is very limited. The lower resolution also means that reflections from static objects can cause problems. For example, manhole covers or a soda can lying on the street can have high radar reflectivity even through they are relatively small. This is called radar clutter and it's why current automotive radars usually disregard static objects.
