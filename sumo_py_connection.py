import os 
import sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("SUMO_HOME environmental variable does not exist.")

import traci

def run_simulation():
    sumo_config_path = os.path.join("data", "modlinska_swiatowida_kolacinska_net.sumocfg")
    sumoBinary = "sumo" # sumo-gui for gui version

    sumoCmd = [
        sumoBinary, 
        "-c", sumo_config_path,
        "--start", "true", # autostart of the simulation
        "--quit-on-end", "true"
    ]

    traci.start(sumoCmd)

    step = 0
    while step < 86400:
        traci.simulationStep()

        if step % 900 == 0:
            vehicles_count = traci.vehicle.getIDCount()
            print(f"H: {step/3600}, vehicles: {vehicles_count}")
        
        step += 1
    
    traci.close()

if __name__ == "__main__":
    run_simulation()