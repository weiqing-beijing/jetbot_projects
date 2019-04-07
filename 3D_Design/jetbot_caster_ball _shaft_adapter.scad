/*
* Designed by qing.wei@live.com. 
* April 4, 2019.
*
* The 3D print design of the caster ball used in nVidia Jetson Nano's Jetbot project
* the original purchase link: https://www.amazon.com/dp/B01N2S7CX6//ref=cm_sw_su_dp
*
* A "tt-motor to wheel" shaft adopter design is also included. 
* The current dimension is for my own wheel purchased elsewhere. 
* Anyone can modify the variables based on own measurement. 
* May need to try a few times as the allowance of 3D printer precision
* and the flexibility of the materials will be different. 
* I use 1.75mm PLA filament with 200 degree Celsius nozzle temperature
* and a hot bed with 60 degree Celsius temperature.
*/


/*
* Caster ball. print in 2 pieces and glue them together.
*/

wall_thickness = 2;
d_ex = 25.4;
r_ex = d_ex/2;
d_in = d_ex - wall_thickness;
r_in = d_in/2;

/* half-cut ball used in Jetbot caster, need to be glued together beofre usage */
difference(){
    difference(){
        sphere(r_ex, $fn=100);
        translate([0, 0, -r_ex/2]){
            cube(size=[(d_ex+1), (d_ex+1), (r_ex)], center=true);
        }
    }
    #difference(){
        sphere(r_in, $fn=100);
        translate([0,0,-r_in/2]){
            cube(size=[(d_in+1), (d_in+1), (r_in)], center=true);
        }
    }
}


/* 
* Shaft adapter linking tt motor and wheel together:
* - tt has 5.8 diameter with a 5.8x3.6 square-shape cut
* - wheel has 6.2 diameter 
*/

/*
wall_T = 1.6;
wheel_shaft_D = 6.2;
wheel_shaft_L = 5;

motor_shaft_D = 6.0;//5.8 with BLK PLA is too tight, changed to 6.0
motor_shaft_W = 3.8;//3.6 with BLK PLA is too tight, chnaged to 3.8
motor_shaft_L = 9;

connector_L = wheel_shaft_L + motor_shaft_L;


translate([50, 0, connector_L/2]){connector();}

module connector(){
    difference(){
        solid();
        wheel_shaft_holder();
        motor_shaft_holder();
    }
}

module solid(){
    cylinder (h =connector_L, d=wheel_shaft_D + wall_T*2, center = true, $fn=100);
}

module wheel_shaft_holder(){
    #translate([0,0,connector_L/2-wheel_shaft_L/2]){
        cylinder(h=wheel_shaft_L, r=wheel_shaft_D/2, center = true, $fn=100);}
}

module motor_shaft_holder(){
    #translate([0,0,-connector_L/2+motor_shaft_L/2]){
        intersection(){
            motor_shaft_cylinder();
            motor_shaft_cube();
            }
    }
}

module motor_shaft_cylinder(){
    cylinder(h=motor_shaft_L, d=motor_shaft_D, center=true, $fn=100);
}

module motor_shaft_cube(){
    cube(size=[motor_shaft_W, motor_shaft_D, motor_shaft_L], center=true);
}
*/