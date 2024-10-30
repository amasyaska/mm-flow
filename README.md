# mm-flow

# architecture
The question of architecture is quite complicated and ambiguous in this case.

The main goal of the program is to model the modernization project by simulating the interactions between the "actors" of the project, described by classes.

## the approach chosen for modeling

We have entity Task, that requires some amount of Resource of some type to complete. We have entity Resource, that can be exhausted and required to complete Task.

We'll use observer design pattern.
