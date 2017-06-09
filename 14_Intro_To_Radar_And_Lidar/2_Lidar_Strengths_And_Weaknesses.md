# Lidar Strengths & Weaknesses

Lidar stands for *Light Detection and Ranging* just like radar stands for *Radio Detection and Ranging*

Unlike radar which uses radio waves, lidar uses an infrared laser beam to determine the distance between the sensor and a nearby object

Most current lidars use light in the 900 nanometer wavelength range, although some lidars use longer wavelengths which perform better in rain and fog

In current lidars, a rotating swivel scans the laser beam across the field of view. The lasers are pulsed and the pulses are reflected by objects. These reflections return a point cloud that represents these objects. 

Lidar has a much higher spatial resolution than radar because of the more focused laser beam, the larger number of scan layers in the vertical direction, and the high density of lidar points per layer

The current generation of lidars cannot measure the velocity of objects directly, and have to rely on the differing position between two of more scans

Lidars are more affected by weather conditions and by dirt on the senors, which requires keeping them clean

They are also much bulkier than other sensors and therefore, more difficult to integrate unless one just wants to mount a big scanner on the roof of the vehicle

***

### Footnote on Lidar

There are other possibilities to scan the laser beams. Instead of rotating the lasers or having a rotating mirror, we can scan the lidar with a vibrating micromirror. Those lidars are in development but none are commercially available now (as of March 2017).

Instead of mechanically moving the laser beam, a similar principle to phased array radar can be employed. Dividing a single laser beam into multiple waveguides, the phase relationship between the waveguides can be altered and thereby the direction of the laser beam shifted. A company named Quanergy is working on systems like that. The advantage is that the form factor can be much smaller and that there are no moving parts.

Another possibility is to use the laser as a gigantic flash like with a camera and then measuring the arrival times for all the objects with one big imaging photodiode array. This is in effect a 3D camera. The components are currently very expensive and currently this is used more in space and in terrain mapping applications.
