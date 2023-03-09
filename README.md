# pico
Contains HW projects predominantly built over RP2040.

1. RGB_LED_Intensity_w_pot_and_LCD: A RBG LED (whose intensity can be controlled by a potentiometer) binks in a predefined order. 
Current color of the RGB LED and its intensity is displayed on the LCD. 
  The folder contains:
    1. pico micro-python code. 
    2. Fritzzing circuit diagram. 
    3. Circuit diagram png. 

2. Motor_ctrl_w_pot_and_LCD: A simple DC motor is controlled using an H-Bridge. Its speed can be controlled by a potentiometer. Its speed and direction is displayed on an LCD. 
  The folder contains: 
    1. pico micro-python code. 
    2. Fritzzing circuit diagram. 
    3. Circuit diagram png. 
    
3. Temperature_sensor_w_RGB_LED: Temperature and humidity sensor DHT11 detects temperature and humidity. 
Light of RGB LED varies from red to blue depending upon the humidity level. Humidity < 10, RED. Humidity > 60, BLUE. 
Intensity can be controlled by potentiometer. LCD shows current temp and humidity, and warns if humidity <10. 
  The folder contains:
    1. pico mocro-python code. 
    2. Fritzzing circuit diagram. 
    3. Circuit diagram png. 
    
 4. Distance Sensor: Intention is to detect the continuous distance of an object. In progress.. 


